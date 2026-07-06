## Summary

- 用 week07 训练的 `checkpoints/dev/best.pt` 完成文本生成；对比 temperature=0.8 vs 1.2。
- `sample.py` 增强：ckpt 不存在时回退 `best.pt`，打印采样参数。

## Test plan

- [x] `python -m gpt_lab.sample ... --temperature 0.8` — 生成字符
- [x] `python -m gpt_lab.sample ... --temperature 1.2` — 风格更随机
- [x] `experiment.md` 记录两种采样结果与流程说明

## 命令

```bash
python -m gpt_lab.sample --config configs/dev.yaml --ckpt checkpoints/dev/best.pt --prompt "ROMEO:" --temperature 0.8 --top-k 40
python -m gpt_lab.sample --config configs/dev.yaml --ckpt checkpoints/dev/best.pt --prompt "ROMEO:" --temperature 1.2 --top-k 40
```

## 设备

- cpu

## 代码改动

- `gpt_lab/sample.py`
- `week08_generate/experiment.md`、`notes.md`

## 观察

- 采样：logits → /temperature → top_k → softmax → multinomial
- 更高 temperature 输出更发散

## 卡住的问题

- 无
