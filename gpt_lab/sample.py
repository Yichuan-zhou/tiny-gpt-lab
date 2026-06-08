from __future__ import annotations

import argparse
from pathlib import Path

import torch

from gpt_lab.config import load_config, resolve_device
from gpt_lab.data import load_char_corpus
from gpt_lab.models.gpt import GPT


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="configs/dev.yaml")
    parser.add_argument("--ckpt", default="checkpoints/dev/latest.pt")
    parser.add_argument("--prompt", default="ROMEO:")
    parser.add_argument("--max-new-tokens", type=int, default=200)
    parser.add_argument("--temperature", type=float, default=0.8)
    parser.add_argument("--top-k", type=int, default=40)
    args = parser.parse_args()

    cfg = load_config(args.config)
    device = resolve_device(cfg.device)
    corpus = load_char_corpus(cfg.data_path)

    model = GPT(cfg, corpus.vocab_size).to(device)
    ckpt_path = Path(args.ckpt)
    if not ckpt_path.exists():
        best = ckpt_path.parent / "best.pt"
        if best.exists():
            ckpt_path = best
    if ckpt_path.exists():
        state = torch.load(ckpt_path, map_location=device, weights_only=False)
        model.load_state_dict(state["model"])
        print(f"loaded {ckpt_path} step={state.get('step', '?')}")
    else:
        print(f"warning: {ckpt_path} not found, using random weights")

    print(f"prompt={args.prompt!r} temperature={args.temperature} top_k={args.top_k}")
    start = torch.tensor([corpus.encode(args.prompt)], dtype=torch.long, device=device)
    out = model.generate(start, args.max_new_tokens, args.temperature, args.top_k)
    print(corpus.decode(out[0].tolist()))


if __name__ == "__main__":
    main()
