"""Week04: causal self-attention.

Students implement or verify against tests in tests/test_attention.py.
"""

from __future__ import annotations

import math

import torch
import torch.nn as nn
import torch.nn.functional as F


def causal_self_attention(
    x: torch.Tensor,
    n_head: int,
    head_dim: int | None = None,
) -> torch.Tensor:
    """
    x: (B, T, C)
    returns: (B, T, C)
    """
    B, T, C = x.shape
    if head_dim is None:
        assert C % n_head == 0
        head_dim = C // n_head

    qkv = nn.Linear(C, 3 * C, bias=False).to(x.device)
    q, k, v = qkv(x).split(C, dim=-1)
    q = q.view(B, T, n_head, head_dim).transpose(1, 2)
    k = k.view(B, T, n_head, head_dim).transpose(1, 2)
    v = v.view(B, T, n_head, head_dim).transpose(1, 2)

    att = (q @ k.transpose(-2, -1)) / math.sqrt(head_dim)
    mask = torch.tril(torch.ones(T, T, device=x.device, dtype=torch.bool))
    att = att.masked_fill(~mask, float("-inf"))
    att = F.softmax(att, dim=-1)
    out = att @ v
    out = out.transpose(1, 2).contiguous().view(B, T, C)
    return out


class CausalSelfAttention(nn.Module):
    def __init__(self, n_embd: int, n_head: int, dropout: float = 0.0):
        super().__init__()
        assert n_embd % n_head == 0
        self.n_head = n_head
        self.head_dim = n_embd // n_head
        self.c_attn = nn.Linear(n_embd, 3 * n_embd)
        self.c_proj = nn.Linear(n_embd, n_embd)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        B, T, C = x.shape
        qkv = self.c_attn(x)
        q, k, v = qkv.split(C, dim=2)
        q = q.view(B, T, self.n_head, self.head_dim).transpose(1, 2)
        k = k.view(B, T, self.n_head, self.head_dim).transpose(1, 2)
        v = v.view(B, T, self.n_head, self.head_dim).transpose(1, 2)

        att = (q @ k.transpose(-2, -1)) / math.sqrt(self.head_dim)
        mask = torch.tril(torch.ones(T, T, device=x.device, dtype=torch.bool))
        att = att.masked_fill(~mask, float("-inf"))
        att = F.softmax(att, dim=-1)
        att = self.dropout(att)
        y = att @ v
        y = y.transpose(1, 2).contiguous().view(B, T, C)
        return self.c_proj(y)
