# notes

## 环境

- Python: 3.12.10
- PyTorch: 2.12.0+cpu
- CUDA: False
- GPU: 无（CPU）

## 改动

- `gpt_lab/sample.py`：若指定 ckpt 不存在则回退 `best.pt`；打印 prompt / temperature / top_k。
- `week08_generate/experiment.md`：两种 temperature 采样对比。

## 观察

- checkpoint `checkpoints/dev/best.pt`（week07 训练）可正常加载生成。
- temp=0.8 输出相对平稳；temp=1.2 更发散、标点和大写更多。
- 项目终点：`gpt_lab` 具备 GPT-2 架构 + 训练环 + 采样。

## 卡住的问题

- 无

## PR 备注

- 命令：`python -m gpt_lab.sample --config configs/dev.yaml --ckpt checkpoints/dev/best.pt --prompt "ROMEO:" --temperature 0.8`
- 设备：cpu
- 代码：`sample.py` 小幅增强
- 现象：两种 temperature 生成风格可区分
- 实验记录：`week08_generate/experiment.md`
