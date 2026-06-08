# experiment

## 运行 1

命令：

```bash
python -m gpt_lab.train --config configs/dev.yaml --stage gpt
```

- `n_layer` / `n_head` / `n_embd`: 4 / 4 / 64
- `max_steps`: 500
- `device`: cpu
- 参数量（日志里有）: 208,320
- 最后 train_loss / val_loss: 2.4186 / 2.4079
- 备注：loss 从 step=0 的 4.19/4.07 持续下降，checkpoint 写入 `checkpoints/dev/latest.pt`

## 采样

命令：

```bash
python -m gpt_lab.sample --config configs/dev.yaml --ckpt checkpoints/dev/latest.pt --prompt "ROMEO:"
```

- 生成片段（贴一小段）:

```
ROMEO:
Noud mere that buths for CAtingher d, sus inowiu m gheran'gh be he
Rout acs'tor pthoweo e w uyothe the'mern
Sond t prer is mY mashod oricld to wen f toures y hinonp stotgy ath'd, ste ar thice
tout th
```

- 备注：500 步 mini GPT 已能输出可读字符（仍较乱，符合预期）；加载 checkpoint step=500

## 观察

- mini GPT（4 层、4 头、64 维）参数量约 20 万，500 步后 val loss ~2.41，明显低于 week03 MLP 最佳（~2.39 接近，但 GPT 用 attention 建模长程依赖，后续加层/步数会继续改善）。
- `Block` = LayerNorm → CausalSelfAttention → 残差 → LayerNorm → MLP → 残差；`GPT` 含 token/pos embedding、多层 Block、lm_head（与 token_emb 权重共享）。
- 训练 loss 全程单调下降，满足完成标准。
