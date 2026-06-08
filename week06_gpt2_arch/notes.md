# notes

## 环境

- Python: 3.12.10
- PyTorch: 2.12.0+cpu
- tiktoken: 已安装（week06+）
- CUDA: False
- GPU: 无（CPU）

## 改动

- `gpt_lab/models/gpt.py`：GPT-2 命名重构（`wte`/`wpe`/`h`/`ln_f`；MLP 拆为 `c_fc`+`c_proj`）。
- `gpt_lab/models/attention.py`：`qkv`/`proj` → `c_attn`/`c_proj`。
- `gpt_lab/data.py`：新增 `BPECorpus`（tiktoken gpt2 编码），`build_dataloader` 支持 `vocab: bpe`。
- `gpt_lab/train.py`：移除 BPE stub 的 `NotImplementedError`。

## 观察

- dev（208k 参数）500 步训练正常，val loss ~2.41，与 week05 重构前接近。
- gpt2_124m 初始化参数量 124,439,808；logits shape `(8, 1024, 50257)`；单步 backward 在 CPU 约 32s。
- 后续 week07/08 仍在同一 `gpt.py` 上演进。

## 卡住的问题

- 无

## PR 备注

- 命令：`make train CONFIG=dev STAGE=gpt2`；gpt2_124m 用 Python 脚本做初始化检查
- 设备：cpu
- 代码：GPT-2 结构对齐 + BPE 数据管线
- 现象：dev 训练 loss 下降；124M 参数量与 shape 正确
- 实验记录：`week06_gpt2_arch/experiment.md`
