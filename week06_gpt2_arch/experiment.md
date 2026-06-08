# experiment

## dev 配置

命令：

```bash
make train CONFIG=dev STAGE=gpt2
```

- `n_layer` / `n_head` / `n_embd`: 4 / 4 / 64
- `vocab`: char（65）
- `max_steps`: 500
- `device`: cpu
- 参数量: **208,320**
- 末步 train_loss / val_loss: 2.4070 / 2.4353
- 备注：GPT-2 命名重构后（`wte`/`wpe`/`h`/`c_fc`/`c_proj`/`c_attn`）dev 配置 forward + backward 正常，loss 从 ~4.2 降至 ~2.4

## gpt2_124m 初始化

命令：

```bash
python -c "
from gpt_lab.config import load_config, resolve_device
from gpt_lab.data import build_dataloader
from gpt_lab.models.gpt import GPT
cfg = load_config('configs/gpt2_124m.yaml')
device = resolve_device(cfg.device)
corpus, get_batch = build_dataloader(cfg, device)
model = GPT(cfg, corpus.vocab_size).to(device)
print(f'params={model.num_params:,}')
x, y = get_batch('train')
logits, loss = model(x, y)
loss.backward()
print(f'logits={tuple(logits.shape)} loss={loss.item():.4f}')
"
```

- 打印的参数量: **124,439,808**（≈ 124M）
- logits shape: `(8, 1024, 50257)` — batch × block_size × vocab
- `vocab`: bpe（tiktoken gpt2，50257）
- 是否 OOM: 否（CPU，单步 forward+backward ~32s）
- 备注：124M 全量短训在 CPU 上极慢，本周仅做结构初始化与 shape 检查

## 观察

- `gpt.py` 已对齐 GPT-2 模块命名：`wte`/`wpe`（embedding）、`h`（Block 列表）、`ln_f`、`c_attn`/`c_proj`（attention）、`c_fc`/`c_proj`（MLP）。
- `data.py` 新增 `BPECorpus`，`vocab: bpe` 时用 tiktoken 编码 tiny_shakespeare，词表 50257。
- 参数量公式验证：124M ≈ 12 层 × (attn + MLP) + embedding(50257×768 + 1024×768) + ln，与 OpenAI GPT-2 small 一致。
