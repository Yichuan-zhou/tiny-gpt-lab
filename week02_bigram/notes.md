# notes

## 环境

- Python: 3.12.10
- PyTorch: 2.12.0+cpu
- CUDA: False
- GPU: 无（CPU 训练）

运行前需安装依赖：`pip install torch pyyaml numpy`（见 `requirements.txt`）。

## 改动

- `gpt_lab/models/bigram.py`：实现 `forward`（`nn.Embedding(vocab, vocab)` 作 bigram 查表）与 `sample`（对最后一位置 logits 做 softmax + multinomial）。
- 新增 `configs/dev_bigram_lr1e3.yaml`：运行 2 使用 `lr=1e-3`，其余与 `dev.yaml` 一致。
- 理解 `gpt_lab/data.py` 中 `get_batch`：`x` 为 `[i:i+T]`，`y` 为 `[i+1:i+T+1]`，即预测下一字符。

## 观察

- `device=cpu`，`params=4225`（65×65 字符词表），训练约 9s/500 步。
- 运行 1（lr=3e-4）：val_loss 4.81 → 4.58。
- 运行 2（lr=1e-3）：val_loss 4.58 → 3.94，下降更快。
- `BigramLM.sample` 生成 200 字符仍为随机风格，符合模型容量限制。

## 卡住的问题

- 命令：`python -m gpt_lab.train ...`
- 输出 / 报错：首次 `ModuleNotFoundError: No module named 'yaml'`
- 试过什么：`pip install pyyaml numpy`
- 猜测：按 `docs/setup.md` 一次性安装 `requirements.txt` 可避免缺包

## PR 备注

- 命令：`python -m gpt_lab.train --config configs/dev.yaml --stage bigram` 与 `--config configs/dev_bigram_lr1e3.yaml`
- 设备：cpu
- 代码：`bigram.py` forward/sample；实验记录见 `week02_bigram/experiment.md`
- 现象：val loss 下降；大 lr 收敛更快；采样仍为乱码
- 无阻塞性错误（安装依赖后正常）
