# notes

## 环境

- Python: 3.12.10（`C:\Users\39546\AppData\Local\Programs\Python\Python312\python.exe`）
- PyTorch: 2.12.0+cpu（pip 安装）
- CUDA: False（`torch.cuda.is_available()`）
- GPU: 无（本机用 CPU 训练）

说明：系统 PATH 里的 `python` 是 Windows 商店占位符，实际使用完整路径的 Python 3.12 运行脚本。

## 改动

- 运行 1：默认参数（`lr=0.1`, `steps=200`, `noise=0.3`, `batch_size=16`）
- 运行 2：仅将 `lr` 改为 `0.01`，其余不变
- `train.py` 已恢复为默认 `lr=0.1`

## 观察

- 两次运行 `device=cpu`，脚本正常结束。
- `lr=0.1` 收敛更快；`lr=0.01` 同样 200 步也能接近 w≈2、b≈1，但前期 loss 更高。
- 训练 loss 与 eval loss 总体同向下降，符合预期。

## 卡住的问题

- 命令：直接输入 `python` / `conda`
- 输出 / 报错：命令找不到，或 Windows 商店 Python 占位符
- 试过什么：改用 `C:\Users\39546\AppData\Local\Programs\Python\Python312\python.exe`；用 pip 安装 `torch`
- 猜测：需把 Python 3.12 加入 PATH，或按 `docs/setup.md` 用 Conda 建 `tiny-gpt-lab` 环境

## PR 备注

- 命令：`python week01_bootstrap/train.py`（两次，第二次前改 `lr=0.01`）
- 设备：cpu
- 现象：loss 下降，w→2、b→1；小 lr 收敛更慢
- 无阻塞性错误（有 NumPy 相关 warning，不影响训练）
