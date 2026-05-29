"""Week03: MLP language model with context window.

Uses the last `block_size` tokens as context to predict the next token.
"""

from __future__ import annotations

import torch
import torch.nn as nn
import torch.nn.functional as F


class MLPLM(nn.Module):
    def __init__(
        self,
        vocab_size: int,
        block_size: int,
        n_embd: int = 64,
        n_hidden_layers: int = 1,
    ):
        super().__init__()
        self.block_size = block_size
        self.token_emb = nn.Embedding(vocab_size, n_embd)
        hidden = 4 * n_embd
        layers: list[nn.Module] = [nn.Linear(block_size * n_embd, hidden), nn.ReLU()]
        for _ in range(n_hidden_layers - 1):
            layers.extend([nn.Linear(hidden, hidden), nn.ReLU()])
        layers.append(nn.Linear(hidden, vocab_size))
        self.mlp = nn.Sequential(*layers)

    def _context_flat(self, idx: torch.Tensor) -> torch.Tensor:
        B, T = idx.shape
        if T > self.block_size:
            idx = idx[:, -self.block_size :]
            T = self.block_size
        emb = self.token_emb(idx)
        flat = emb.reshape(B, T * emb.size(-1))
        if T < self.block_size:
            pad = torch.zeros(
                B, (self.block_size - T) * emb.size(-1), device=idx.device, dtype=emb.dtype
            )
            flat = torch.cat([pad, flat], dim=1)
        return flat

    def forward(self, idx: torch.Tensor) -> torch.Tensor:
        # idx: (B, T) -> logits (B, vocab)
        return self.mlp(self._context_flat(idx))

    def loss(self, idx: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
        logits = self.forward(idx)
        return F.cross_entropy(logits, targets[:, -1])

    @torch.no_grad()
    def sample(self, start_ids: list[int], max_new: int) -> list[int]:
        out = list(start_ids)
        for _ in range(max_new):
            ctx = out[-self.block_size :]
            x = torch.tensor([ctx], dtype=torch.long)
            probs = F.softmax(self.forward(x)[0], dim=-1)
            next_id = torch.multinomial(probs, num_samples=1).item()
            out.append(next_id)
        return out
