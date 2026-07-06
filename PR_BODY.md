## Summary

- 实现字符级 `BigramLM`（`forward` + `sample`），理解 `nn.Embedding(vocab, vocab)` 作 bigram 查表。
- 在 `tiny_shakespeare` 上完成两次训练（`lr=3e-4` 与 `lr=1e-3`），val loss 均下降。
- 更新 `week02_bigram/experiment.md`、`notes.md`；新增 `configs/dev_bigram_lr1e3.yaml` 用于运行 2。

## 命令

```bash
python -m gpt_lab.train --config configs/dev.yaml --stage bigram
python -m gpt_lab.train --config configs/dev_bigram_lr1e3.yaml --stage bigram
```

## 设备

- cpu（`torch.cuda.is_available()` 为 False）

## 代码改动

- `gpt_lab/models/bigram.py`：bigram forward / sample
- `configs/dev_bigram_lr1e3.yaml`：运行 2 学习率
- `week02_bigram/experiment.md`、`notes.md`：实验记录

## 观察

- 运行 1：val_loss 4.81 → 4.58（lr=3e-4）
- 运行 2：val_loss 4.58 → 3.94（lr=1e-3，同 500 步下降更快）
- 采样 200 字符仍为随机风格（bigram 无长程依赖，符合预期）

## 卡住的问题

- 首次缺 `yaml`：`pip install pyyaml numpy` 后正常
- 推送时若 git 配置了 `http.https://github.com.proxy`，需先启动本地代理，或单次命令覆盖代理（见下方）

## Test plan

- [x] `python -m gpt_lab.train --config configs/dev.yaml --stage bigram` 能跑通
- [x] val loss 相对 step 0 有下降
- [x] `experiment.md` / `notes.md` 已填写
