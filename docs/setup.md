# 环境配置

目标：让 Python、Git、PyTorch 都能跑起来。

## 需要先安装

- VS Code 或其他编辑器
- Python（推荐 3.10+）
- Conda (Miniconda or Anaconda)
- Git

## 创建 Python 环境

```bash
conda create -n tiny-gpt-lab python=3.10 -y
conda activate tiny-gpt-lab
pip install torch
```

## 最小检查命令

在 terminal 里运行：

```bash
python --version
git --version
python -c "import torch; print(torch.__version__); print(torch.cuda.is_available())"
```

你需要看到：

- Python 能输出版本号
- Git 能输出版本号
- PyTorch 能正常 import
- `torch.cuda.is_available()` 能输出 `True` 或 `False`

`CUDA False` 不一定是错误。  
如果你在普通 CPU 机器上运行，`False` 很正常。只有在你明确使用 GPU/CUDA 机器时，才需要进一步检查。

## Git 身份

如果还没配置 Git 身份，运行：

```bash
git config --global user.name "your-name"
git config --global user.email "you@example.com"
```

这里的 name 和 email 用你自己的 GitHub 信息即可。
