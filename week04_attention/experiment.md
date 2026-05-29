# experiment

## 测试运行

命令：

```bash
python -m pytest tests/test_attention.py -q
```

- 是否全部通过: **是**（2 passed in ~2s）
- 若失败，失败用例名: 无
- 修改了 attention.py 哪些部分: 代码库中 `CausalSelfAttention.forward` 已完整实现；本次对照测试核对 QKV 投影、多头 reshape、因果 mask、softmax 与输出投影流程，未改代码
- 备注：全量 `pytest tests/ -q` 同样 2 passed

## 手算核对（可选）

- 固定 `B=1,T=3,C=4`，记下某一位置的 attention 权重和是否只依赖过去:
  - `tril` mask 使位置 t 只能 attend 到 `0..t`；改 `x[:, -1, :]` 不影响 `y[:, :-1, :]`（`test_causal_mask_future_is_zero` 已验证）

## 观察

- `test_causal_self_attention_shape`：输出形状 `(B, T, C)` 与输入一致。
- `test_causal_mask_future_is_zero`：最后一个 token 被篡改后，前面位置的输出不变，说明因果 mask 生效。
- 多头：通道 C 拆成 `n_head` 组，每组独立算 attention 再拼回。
