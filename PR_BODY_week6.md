## Summary

- 将 `gpt.py` 对齐 GPT-2 结构命名：`wte`/`wpe`/`h`/`ln_f`、`c_attn`/`c_proj`（attention）、`c_fc`/`c_proj`（MLP）。
- `data.py` 新增 `BPECorpus`（tiktoken gpt2），支持 `vocab: bpe`。
- dev 配置 500 步训练正常；gpt2_124m 初始化参数量 **124,439,808**，logits shape `(8, 1024, 50257)`。

## Test plan

- [x] `python -m pytest tests/test_attention.py -q` — 2 passed
- [x] `python -m gpt_lab.train --config configs/dev.yaml --stage gpt2` — loss 4.08 → 2.44
- [x] gpt2_124m 初始化检查 — params ≈124M，forward+backward 无 OOM

## 命令

```bash
python -m gpt_lab.train --config configs/dev.yaml --stage gpt2
python -c "..."  # gpt2_124m shape check（见 experiment.md）
```

## 设备

- cpu

## 代码改动

- `gpt_lab/models/gpt.py`：GPT-2 命名重构
- `gpt_lab/models/attention.py`：`c_attn`/`c_proj`
- `gpt_lab/data.py`：`BPECorpus` + `build_dataloader` bpe 分支
- `gpt_lab/train.py`：移除 BPE stub
- `week06_gpt2_arch/experiment.md`、`notes.md`

## 观察

- dev（208k）重构后 val loss ~2.44，与 week05 接近
- 124M 单步 backward CPU ~26s，本周仅做结构/shape 检查

## 卡住的问题

- 无
