"""Week05–08: GPT / GPT-2 style transformer.

Week05: mini config works end-to-end.
Week06: align module names & shapes with GPT-2 (refactor in place).
Week07–08: same file; training & sampling use checkpoints.
"""

from __future__ import annotations

import torch
import torch.nn as nn
import torch.nn.functional as F

from gpt_lab.config import TrainConfig
from gpt_lab.models.attention import CausalSelfAttention


class MLP(nn.Module):
    """GPT-2 feed-forward: c_fc -> GELU -> c_proj."""

    def __init__(self, n_embd: int, dropout: float):
        super().__init__()
        self.c_fc = nn.Linear(n_embd, 4 * n_embd)
        self.c_proj = nn.Linear(4 * n_embd, n_embd)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.c_fc(x)
        x = F.gelu(x)
        x = self.c_proj(x)
        return self.dropout(x)


class Block(nn.Module):
    """GPT-2 transformer block: ln_1 -> attn -> residual -> ln_2 -> mlp -> residual."""

    def __init__(self, cfg: TrainConfig):
        super().__init__()
        self.ln_1 = nn.LayerNorm(cfg.n_embd)
        self.attn = CausalSelfAttention(cfg.n_embd, cfg.n_head, cfg.dropout)
        self.ln_2 = nn.LayerNorm(cfg.n_embd)
        self.mlp = MLP(cfg.n_embd, cfg.dropout)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = x + self.attn(self.ln_1(x))
        x = x + self.mlp(self.ln_2(x))
        return x


class GPT(nn.Module):
    """GPT-2 LM: wte + wpe + h (blocks) + ln_f + tied lm_head."""

    def __init__(self, cfg: TrainConfig, vocab_size: int):
        super().__init__()
        self.cfg = cfg
        self.block_size = cfg.block_size
        self.wte = nn.Embedding(vocab_size, cfg.n_embd)
        self.wpe = nn.Embedding(cfg.block_size, cfg.n_embd)
        self.drop = nn.Dropout(cfg.dropout)
        self.h = nn.ModuleList([Block(cfg) for _ in range(cfg.n_layer)])
        self.ln_f = nn.LayerNorm(cfg.n_embd)
        self.lm_head = nn.Linear(cfg.n_embd, vocab_size, bias=False)
        self.wte.weight = self.lm_head.weight

        self.apply(self._init_weights)

    def _init_weights(self, module: nn.Module) -> None:
        if isinstance(module, nn.Linear):
            torch.nn.init.normal_(module.weight, mean=0.0, std=0.02)
            if module.bias is not None:
                torch.nn.init.zeros_(module.bias)
        elif isinstance(module, nn.Embedding):
            torch.nn.init.normal_(module.weight, mean=0.0, std=0.02)

    def forward(self, idx: torch.Tensor, targets: torch.Tensor | None = None):
        B, T = idx.shape
        if T > self.block_size:
            idx = idx[:, -self.block_size :]
            T = self.block_size
            if targets is not None:
                targets = targets[:, -self.block_size :]

        pos = torch.arange(0, T, device=idx.device)
        x = self.wte(idx) + self.wpe(pos)
        x = self.drop(x)
        for block in self.h:
            x = block(x)
        x = self.ln_f(x)
        logits = self.lm_head(x)

        loss = None
        if targets is not None:
            loss = F.cross_entropy(
                logits.view(B * T, -1),
                targets.view(B * T),
            )
        return logits, loss

    @torch.no_grad()
    def generate(
        self,
        idx: torch.Tensor,
        max_new_tokens: int,
        temperature: float = 1.0,
        top_k: int | None = None,
    ) -> torch.Tensor:
        for _ in range(max_new_tokens):
            idx_cond = idx[:, -self.block_size :]
            logits, _ = self(idx_cond)
            logits = logits[:, -1, :] / max(temperature, 1e-8)
            if top_k is not None:
                v, _ = torch.topk(logits, min(top_k, logits.size(-1)))
                logits[logits < v[:, [-1]]] = float("-inf")
            probs = F.softmax(logits, dim=-1)
            next_id = torch.multinomial(probs, num_samples=1)
            idx = torch.cat([idx, next_id], dim=1)
        return idx

    @property
    def num_params(self) -> int:
        return sum(p.numel() for p in self.parameters())
