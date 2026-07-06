## Summary

- 完善 GPT 训练管线：线性 lr warmup（前 10% 步）、按 val loss 保存 `best.pt`、日志打印当前 lr。
- 两组超参对比：dev（lr=3e-4）best val **2.45**；dev_gpt_lr6e4（lr=6e-4）best val **2.29**。

## Test plan

- [x] `python -m gpt_lab.train --config configs/dev.yaml --stage gpt2` — checkpoint 写入 `checkpoints/dev/`
- [x] `python -m gpt_lab.train --config configs/dev_gpt_lr6e4.yaml --stage gpt2` — 更高 lr 收敛更快
- [x] 两组 loss 整体下降

## 命令

```bash
python -m gpt_lab.train --config configs/dev.yaml --stage gpt2
python -m gpt_lab.train --config configs/dev_gpt_lr6e4.yaml --stage gpt2
```

## 设备

- cpu

## 代码改动

- `gpt_lab/train.py`：warmup、best checkpoint
- `configs/dev_gpt_lr6e4.yaml`
- `week07_train_loop/experiment.md`、`notes.md`

## 观察

- lr=6e-4 在 500 步末 val loss 比 3e-4 低约 0.17
- warmup 减少训练初期震荡

## 卡住的问题

- 无
