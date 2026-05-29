# notes

## 环境

- Python: 3.12.10
- PyTorch: 2.12.0+cpu
- CUDA: False
- GPU: 无（CPU 训练）

## 改动

- `gpt_lab/models/mlp_lm.py`：
  - 修正 `forward`：用最后 `block_size` 个 token 的 embedding 拼成向量，输出 `(B, vocab)`（预测序列末尾的下一字符），不再对全序列 `expand` 同一组 logits。
  - 修正 `loss`：对 `targets[:, -1]` 做 cross entropy（与 `get_batch` 中 `y` 末位对齐）。
  - 新增 `sample`：滑动窗口上下文 + multinomial 采样。
  - 支持 `n_hidden_layers`：默认 1 层；`dev_mlp_lr1e3` 配置使用 2 层。
- `gpt_lab/train.py`：`dev_mlp_lr1e3` 时传入 `n_hidden_layers=2`。
- 新增 `configs/dev_mlp_lr1e3.yaml`：MLP 运行 2 使用 `lr=1e-3` + 双层 hidden。

## 观察

- `device=cpu`，参数量约 1.07M（单层）/ 1.14M（双层），500 步约 6–7s。
- 运行 1（lr=3e-4，单层）：val_loss 4.10 → 最低 **2.65**，最终 2.88。
- 运行 2（lr=1e-3，双层）：val_loss 4.02 → 最低 **2.39**，最终 2.39。
- week02 bigram 最佳 val_loss 为 3.94，MLP 约低 1.0–1.5。
- 原骨架 `logits.unsqueeze(1).expand(B, T, -1)` 会导致 `view` 报错且语义错误（全位置共享同一预测）。

## 卡住的问题

- 命令：`python -m gpt_lab.train --config configs/dev.yaml --stage mlp`
- 输出 / 报错：`RuntimeError: view size is not compatible with input tensor's size and stride`
- 试过什么：改为 `reshape` 仍不合理；改为单步预测 `targets[:, -1]` 并去掉 `expand`
- 猜测：expand 产生非连续 tensor；且 MLP 应按整块上下文预测**一个**下一字符，而非 T 个位置共用 logits

## PR 备注

- 命令：`python -m gpt_lab.train --config configs/dev.yaml --stage mlp` 与 `--config configs/dev_mlp_lr1e3.yaml`
- 设备：cpu
- 代码：`mlp_lm.py` forward/loss/sample + 可配置 hidden 层数；`configs/dev_mlp_lr1e3.yaml`
- 现象：val loss 明显优于 week02 bigram（最低 2.39 vs 3.94）
- 实验记录：`week03_mlp_lm/experiment.md`
