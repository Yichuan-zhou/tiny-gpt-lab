## Summary

- 对照 `tests/test_attention.py` 验证 `gpt_lab/models/attention.py` 中 `CausalSelfAttention`（QKV 投影、多头 reshape、因果 mask、softmax、输出投影）。
- 2/2 单元测试通过；`tril` mask 保证位置 t 只 attend 到 `0..t`。
- 更新 `week04_attention/experiment.md`、`notes.md`。

## Test plan

- [x] `python -m pytest tests/test_attention.py -q` — 2 passed
- [x] `test_causal_mask_future_is_zero`：篡改最后 token 不影响前面位置输出

## 命令

```bash
python -m pytest tests/test_attention.py -q
```

## 设备

- cpu（PyTorch 2.12.0+cpu）

## 代码改动

- 无功能性代码改动；验证已有 `CausalSelfAttention` 实现
- `week04_attention/experiment.md`、`notes.md`

## 观察

- Mask 作用：`torch.tril` 将未来位置 attention 分数设为 `-inf`，softmax 后权重为 0
- 输出形状 `(B, T, C)` 与输入一致

## 卡住的问题

- 首次缺 `pytest`：`pip install pytest` 后正常
