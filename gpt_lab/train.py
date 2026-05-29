from __future__ import annotations

import argparse
from pathlib import Path

import torch

from gpt_lab.config import load_config, resolve_device
from gpt_lab.data import build_dataloader
from gpt_lab.models.bigram import BigramLM
from gpt_lab.models.gpt import GPT
from gpt_lab.models.mlp_lm import MLPLM


def save_checkpoint(path: Path, model: torch.nn.Module, step: int, cfg_name: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    torch.save({"model": model.state_dict(), "step": step, "config": cfg_name}, path)


@torch.no_grad()
def evaluate(model, get_batch, device: str) -> float:
    model.eval()
    x, y = get_batch("val")
    if hasattr(model, "forward") and isinstance(model, GPT):
        _, loss = model(x, y)
        return loss.item()
    if hasattr(model, "loss"):
        return model.loss(x, y).item()
    logits = model(x)
    return torch.nn.functional.cross_entropy(
        logits.view(-1, logits.size(-1)), y.view(-1)
    ).item()


def train_bigram(cfg, device: str) -> None:
    corpus, get_batch = build_dataloader(cfg, device)
    model = BigramLM(corpus.vocab_size).to(device)
    opt = torch.optim.AdamW(model.parameters(), lr=cfg.lr)
    print(f"device={device} stage=bigram params={sum(p.numel() for p in model.parameters())}")

    for step in range(cfg.max_steps):
        x, y = get_batch("train")
        opt.zero_grad()
        logits = model(x)
        loss = torch.nn.functional.cross_entropy(
            logits.view(-1, corpus.vocab_size), y.view(-1)
        )
        loss.backward()
        opt.step()

        if step % cfg.eval_interval == 0 or step == cfg.max_steps - 1:
            val = evaluate(model, get_batch, device)
            print(f"step={step:04d} train_loss={loss.item():.4f} val_loss={val:.4f}")


def train_mlp(cfg, device: str) -> None:
    corpus, get_batch = build_dataloader(cfg, device)
    n_hidden_layers = 2 if cfg.name == "dev_mlp_lr1e3" else 1
    model = MLPLM(
        corpus.vocab_size, cfg.block_size, cfg.n_embd, n_hidden_layers=n_hidden_layers
    ).to(device)
    opt = torch.optim.AdamW(model.parameters(), lr=cfg.lr)
    print(f"device={device} stage=mlp params={sum(p.numel() for p in model.parameters())}")

    for step in range(cfg.max_steps):
        x, y = get_batch("train")
        opt.zero_grad()
        loss = model.loss(x, y)
        loss.backward()
        opt.step()

        if step % cfg.eval_interval == 0 or step == cfg.max_steps - 1:
            val = evaluate(model, get_batch, device)
            print(f"step={step:04d} train_loss={loss.item():.4f} val_loss={val:.4f}")


def train_gpt(cfg, device: str, stage: str) -> None:
    corpus, get_batch = build_dataloader(cfg, device)
    vocab_size = corpus.vocab_size if corpus is not None else 50257
    if corpus is None:
        raise NotImplementedError("week06: implement BPE dataloader for vocab=bpe")

    model = GPT(cfg, vocab_size).to(device)
    opt = torch.optim.AdamW(model.parameters(), lr=cfg.lr, betas=(0.9, 0.95), weight_decay=0.1)
    ckpt_dir = cfg.ckpt_dir
    print(f"device={device} stage={stage} params={model.num_params:,}")

    for step in range(cfg.max_steps):
        x, y = get_batch("train")
        opt.zero_grad(set_to_none=True)
        _, loss = model(x, y)
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        opt.step()

        if step % cfg.eval_interval == 0 or step == cfg.max_steps - 1:
            val = evaluate(model, get_batch, device)
            print(f"step={step:04d} train_loss={loss.item():.4f} val_loss={val:.4f}")
            save_checkpoint(ckpt_dir / "latest.pt", model, step, cfg.name)

    save_checkpoint(ckpt_dir / "latest.pt", model, cfg.max_steps, cfg.name)
    print(f"checkpoint -> {ckpt_dir / 'latest.pt'}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="configs/dev.yaml")
    parser.add_argument("--stage", choices=["bigram", "mlp", "gpt", "gpt2"], default="gpt")
    args = parser.parse_args()

    cfg = load_config(args.config)
    device = resolve_device(cfg.device)
    stage = "gpt" if args.stage == "gpt2" else args.stage

    data_path = Path(cfg.data_path)
    if not data_path.exists():
        raise FileNotFoundError(
            f"Missing {data_path}. See data/README.md to download tiny_shakespeare.txt"
        )

    if stage == "bigram":
        train_bigram(cfg, device)
    elif stage == "mlp":
        train_mlp(cfg, device)
    elif stage in ("gpt", "gpt2"):
        train_gpt(cfg, device, stage)
    else:
        raise ValueError(stage)


if __name__ == "__main__":
    main()
