# notes

## 环境

- Python: 3.12.10
- PyTorch: 2.12.0+cpu
- CUDA: False
- GPU: 无（CPU）

## 改动

- 对照 `tests/test_attention.py` 阅读并验证 `gpt_lab/models/attention.py` 中 `CausalSelfAttention`。
- 核心流程：`qkv` 线性层 → 拆成 Q/K/V → reshape 为 `(B, n_head, T, head_dim)` → scaled dot-product attention → 输出投影。

## 观察

- **Mask 的作用**：`torch.tril` 生成下三角 mask，把「看见未来 token」的 attention 分数设为 `-inf`，softmax 后权重为 0，保证位置 t 的输出只依赖 `0..t` 的上下文（自回归语言模型必需）。
- 两个测试均通过；改序列最后一个 token 不影响前面位置输出，与 mask 语义一致。

## 卡住的问题

- 命令：`pytest tests/test_attention.py -q`
- 输出 / 报错：首次 `No module named pytest`
- 试过什么：`pip install pytest`
- 猜测：按 `requirements.txt` 一次性安装依赖可避免缺包

## PR 备注

- 命令：`python -m pytest tests/test_attention.py -q`
- 设备：cpu
- 代码：验证 `attention.py`（无功能性改动）
- 现象：2/2 测试通过；因果 mask 行为符合预期
- 实验记录：`week04_attention/experiment.md`
