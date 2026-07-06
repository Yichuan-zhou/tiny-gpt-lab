## Summary

- 验证 `gpt_lab/models/gpt.py` 中 `Block` + `GPT` 端到端训练与采样（pre-norm、CausalSelfAttention、MLP 残差、权重共享）。
- 500 步 mini GPT（4 layer / 4 head / 64 embd）val loss 从 ~4.07 降至 ~2.41。
- 更新 `week05_mini_gpt/experiment.md`、`notes.md`。

## Test plan

- [x] `python -m gpt_lab.train --config configs/dev.yaml --stage gpt` — loss 下降，checkpoint 写入 `checkpoints/dev/latest.pt`
- [x] `python -m gpt_lab.sample --config configs/dev.yaml --prompt "ROMEO:"` — 能生成字符

## 命令

```bash
python -m gpt_lab.train --config configs/dev.yaml --stage gpt
python -m gpt_lab.sample --config configs/dev.yaml --ckpt checkpoints/dev/latest.pt --prompt "ROMEO:"
```

## 设备

- cpu（208,320 参数）

## 代码改动

- 无功能性代码改动；验证已有 `gpt.py` 实现
- `week05_mini_gpt/experiment.md`、`notes.md`

## 观察

- step=0: train 4.19 / val 4.07 → step=499: train 2.42 / val 2.41
- 采样 prompt `ROMEO:` 可输出字符（500 步仍较乱，符合预期）

## 卡住的问题

- 无
