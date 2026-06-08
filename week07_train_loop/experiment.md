# experiment

## 运行 1

命令：

```bash
python -m gpt_lab.train --config configs/dev.yaml --stage gpt2
```

- `lr`: 3.0e-4（前 10% 步线性 warmup）
- `max_steps`: 500
- `device`: cpu
- checkpoint 路径: `checkpoints/dev/latest.pt`、`checkpoints/dev/best.pt`
- 末步 train_loss / val_loss: 2.4272 / 2.4546
- 备注：新增 lr warmup、grad clip(1.0)、best checkpoint 保存；loss 从 ~4.2 降至 ~2.45

## 运行 2

命令：

```bash
python -m gpt_lab.train --config configs/dev_gpt_lr6e4.yaml --stage gpt2
```

- 改动项: `lr=6.0e-4`（其余与 dev 相同）
- 末步 train_loss / val_loss: 2.2869 / **2.2893**（best val）
- 备注：更大学习率收敛更快，500 步 val loss 比运行 1 低约 0.17

## 观察

- 两组超参 loss 均整体下降；运行 2（lr=6e-4）末步 val **2.29** 优于运行 1（**2.45**）。
- warmup 使 step=0 有效 lr 很小（3e-4 配置下 6e-6），避免初期震荡。
- `best.pt` 按 val loss 保存，便于后续采样选用最优权重。
