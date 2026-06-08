# notes

## 环境

- Python: 3.12.10
- PyTorch: 2.12.0+cpu
- CUDA: False
- GPU: 无（CPU）

## 改动

- `gpt_lab/train.py`：线性 lr warmup（前 10% 步）、按 val loss 保存 `best.pt`、日志打印当前 lr。
- `configs/dev_gpt_lr6e4.yaml`：运行 2 对比配置（lr=6e-4）。

## 观察

- dev（lr=3e-4）：500 步 best val **2.45**
- dev_gpt_lr6e4（lr=6e-4）：500 步 best val **2.29**，同步数下更优
- checkpoint 位于 `checkpoints/dev/` 与 `checkpoints/dev_gpt_lr6e4/`

## 卡住的问题

- 无

## PR 备注

- 命令：`python -m gpt_lab.train --config configs/dev.yaml --stage gpt2`；`configs/dev_gpt_lr6e4.yaml`
- 设备：cpu
- 代码：训练管线增强（warmup、best checkpoint）
- 现象：两组超参 loss 均下降；lr=6e-4 更优
- 实验记录：`week07_train_loop/experiment.md`
