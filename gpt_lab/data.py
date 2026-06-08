from __future__ import annotations

import torch

from gpt_lab.config import TrainConfig


class CharCorpus:
    """Character-level encode/decode for tiny_shakespeare."""

    def __init__(self, text: str):
        chars = sorted(set(text))
        self.stoi = {ch: i for i, ch in enumerate(chars)}
        self.itos = {i: ch for ch, i in self.stoi.items()}
        self.vocab_size = len(chars)
        self.data = torch.tensor([self.stoi[c] for c in text], dtype=torch.long)

    def encode(self, s: str) -> list[int]:
        return [self.stoi[c] for c in s]

    def decode(self, ids: list[int]) -> str:
        return "".join(self.itos[i] for i in ids)


class BPECorpus:
    """GPT-2 BPE encode/decode via tiktoken."""

    def __init__(self, text: str, encoding_name: str = "gpt2"):
        import tiktoken

        self.enc = tiktoken.get_encoding(encoding_name)
        self.vocab_size = self.enc.n_vocab
        self.data = torch.tensor(self.enc.encode(text), dtype=torch.long)

    def encode(self, s: str) -> list[int]:
        return self.enc.encode(s)

    def decode(self, ids: list[int]) -> str:
        return self.enc.decode(ids)


def load_char_corpus(path: str) -> CharCorpus:
    text = open(path, encoding="utf-8").read()
    return CharCorpus(text)


def load_bpe_corpus(path: str) -> BPECorpus:
    text = open(path, encoding="utf-8").read()
    return BPECorpus(text)


def get_batch(
    corpus: CharCorpus | BPECorpus,
    block_size: int,
    batch_size: int,
    device: str,
    split: str = "train",
) -> tuple[torch.Tensor, torch.Tensor]:
    data = corpus.data
    n = int(0.9 * len(data))
    split_data = data[:n] if split == "train" else data[n:]
    ix = torch.randint(len(split_data) - block_size, (batch_size,))
    x = torch.stack([split_data[i : i + block_size] for i in ix])
    y = torch.stack([split_data[i + 1 : i + block_size + 1] for i in ix])
    return x.to(device), y.to(device)


def build_dataloader(cfg: TrainConfig, device: str):
    if cfg.vocab == "char":
        corpus = load_char_corpus(cfg.data_path)
    elif cfg.vocab == "bpe":
        corpus = load_bpe_corpus(cfg.data_path)
    else:
        raise ValueError(f"unknown vocab: {cfg.vocab}")
    return corpus, lambda split="train": get_batch(
        corpus, cfg.block_size, cfg.batch_size, device, split
    )
