# experiment

## 运行 1

命令：

```bash
python -m gpt_lab.train --config configs/dev.yaml --stage bigram
```

- `lr`: 3.0e-4
- `max_steps`: 500
- `batch_size`: 32
- `block_size`: 64
- `device`: cpu
- 开始几步的 `train_loss / val_loss`:
  - step=0000: 4.7665 / 4.8065
- 最后几步的 `train_loss / val_loss`:
  - step=0400: 4.6046 / 4.6267
  - step=0499: 4.5868 / 4.5828
- 采样片段（如有）: 未单独保存（见运行 2 采样）
- 变化：下降（val_loss 4.81 → 4.58，约降 0.23）
- 备注：lr 较小，500 步内下降平缓但稳定

## 运行 2

命令：

```bash
python -m gpt_lab.train --config configs/dev_bigram_lr1e3.yaml --stage bigram
```

- `lr`: 1.0e-3
- `max_steps`: 500
- `batch_size`: 32
- `block_size`: 64
- `device`: cpu
- 开始几步的 `train_loss / val_loss`:
  - step=0000: 4.5750 / 4.5780
- 最后几步的 `train_loss / val_loss`:
  - step=0400: 4.0772 / 4.0468
  - step=0499: 3.9762 / 3.9419
- 采样片段（200 字符，prompt 首字 `R`）:

```text
RN
XyYRZG,zrye$LRWJ?J?V'HRuZfaZE , :ko:dYCltV-VuckYyiwcP!QOV
r;?nf jYWez
rdEacXLDZu$LM'Ft,UC, vGFfY-p;?DsogeYBwnpw!QklndYvD.eC3XGopnDLDGtV.rVH:hwY?w J-QDIVXBUoIUgfPRa&MKhS'yu?3RZww RWOnpxQBUOGHXXrT&Np
```

- 变化：下降（val_loss 4.58 → 3.94，降幅明显大于运行 1）
- 备注：同 500 步下大 lr 收敛更快；采样仍接近随机字符（bigram 无长程依赖）

## 观察

- 两次运行 val loss 均下降，满足完成标准。
- `lr=1e-3` 比 `3e-4` 在同步数下 val loss 低约 0.6；若 lr 过大可能出现震荡（未在本实验验证）。
- Bigram 只看上一字符，无法学语法，采样乱码属预期；week03 MLP 应能明显改进。
