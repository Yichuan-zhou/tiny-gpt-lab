# experiment

## 运行 1

命令：

```bash
python -m gpt_lab.train --config configs/dev.yaml --stage mlp
```

- `block_size`: 64
- `n_embd`: 64
- `lr`: 3.0e-4
- `max_steps`: 500
- `batch_size`: 32
- `device`: cpu
- 结构：单层 hidden（`4*n_embd` → vocab），参数量 1,069,697
- week02 最佳 val_loss（对比用）: **3.9419**（bigram，`lr=1e-3`）
- 开始几步的 `train_loss / val_loss`:
  - step=0000: 4.2034 / 4.0962
- 最后几步的 `train_loss / val_loss`:
  - step=0300: 2.7887 / **2.6496**（本次最低 val）
  - step=0499: 2.8668 / 2.8789
- 备注：修复 forward/loss 后，MLP 用 64 字符上下文，val loss 已明显低于 week02 bigram

## 运行 2

命令：

```bash
python -m gpt_lab.train --config configs/dev_mlp_lr1e3.yaml --stage mlp
```

- 改动项: 增加一层 hidden（`256→256→vocab`）；`lr=1e-3`（与 week02 最佳 run 对齐）
- `block_size`: 64
- `n_embd`: 64
- `max_steps`: 500
- `device`: cpu
- 参数量: 1,135,489
- 开始几步的 `train_loss / val_loss`:
  - step=0000: 4.1633 / 4.0241
- 最后几步的 `train_loss / val_loss`:
  - step=0200: 2.7657 / **2.6081**
  - step=0499: 2.6885 / **2.3918**（本次最低 val）
- val_loss: 最低 **2.3918**（step 499）
- 备注：大 lr + 双层 MLP 收敛更快，500 步末 val 优于运行 1

## 观察

- 同数据、同 `block_size=64` 下，MLP val loss（~2.4–2.9）**显著低于** week02 bigram 最佳（3.94），满足完成标准。
- 原因：bigram 只看 1 个字符，MLP 拼接 `block_size` 个 embedding 作上下文，容量与信息都更大。
- 运行 2 双层 + 大 lr 最低 val 约 2.39，优于运行 1 单层（~2.65）。
- 后期 val 有震荡：小语料 + 固定 500 步下常见，后续 week 用 attention/GPT 会进一步改善。
