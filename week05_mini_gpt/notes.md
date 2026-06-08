# notes

## 环境

- Python: 3.12.10
- PyTorch: 2.12.0+cpu
- CUDA: False
- GPU: 无（CPU）

## 改动

- 实现/验证 `gpt_lab/models/gpt.py` 中 `Block`（pre-norm + CausalSelfAttention + MLP 残差）与 `GPT`（embedding、多层 Block、lm_head 权重共享、generate）。
- 配置沿用 `configs/dev.yaml`：`n_layer=4`, `n_head=4`, `n_embd=64`, `max_steps=500`。

## 观察

- 208k 参数 mini GPT 在 500 步后 val loss 从 ~4.07 降至 ~2.41，趋势稳定下降。
- `make sample` / `gpt_lab.sample` 能基于 `checkpoints/dev/latest.pt` 生成字符；未训很久时文本乱是正常的。
- 从本周起后续 week 都在同一 `gpt.py` 上演进，不再新建独立模型文件。

## 卡住的问题

- 无

## PR 备注

- 命令：`python -m gpt_lab.train --config configs/dev.yaml --stage gpt`；`python -m gpt_lab.sample --config configs/dev.yaml --prompt "ROMEO:"`
- 设备：cpu
- 代码：`gpt.py` Block/GPT 完整；`attention.py` 因果 self-attention 已通过测试
- 现象：500 步 train/val loss ~2.42；采样可输出字符
- 实验记录：`week05_mini_gpt/experiment.md`
