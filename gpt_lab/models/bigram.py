"""Week02: neural bigram language model.

TODO: 理解并必要时改写 forward / sample，不要只会调用。
"""

from __future__ import annotations

import torch
import torch.nn as nn
import torch.nn.functional as F


class BigramLM(nn.Module):
    def __init__(self, vocab_size: int):
        super().__init__()
        self.token_emb = nn.Embedding(vocab_size, vocab_size)

    def forward(self, idx: torch.Tensor) -> torch.Tensor:
        # Each token id indexes a row of (vocab, vocab) -> logits for the next char.
        # idx: (B, T) -> logits (B, T, vocab)
        logits = self.token_emb(idx)
        return logits

    @torch.no_grad()
    def loss(self, idx: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
        logits = self.forward(idx)
        B, T, C = logits.shape
        return F.cross_entropy(logits.view(B * T, C), targets.view(B * T))

    @torch.no_grad()
    def sample(self, start_id: int, max_new: int) -> list[int]:
        out = [start_id]
        for _ in range(max_new):
            x = torch.tensor([[out[-1]]], dtype=torch.long)
            logits = self.forward(x)
            probs = F.softmax(logits[0, -1], dim=-1)
            next_id = torch.multinomial(probs, num_samples=1).item()
            out.append(next_id)
        return out
