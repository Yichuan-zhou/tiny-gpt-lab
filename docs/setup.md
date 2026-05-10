# setup

安装：

- VS Code
- Python 3.10+
- Conda
- Git

Python：

```bash
conda create -n tiny-gpt-lab python=3.10 -y
conda activate tiny-gpt-lab
pip install torch
```

检查：

```bash
python --version
git --version
python -c "import torch; print(torch.__version__); print(torch.cuda.is_available())"
```

`CUDA False` 不一定有问题。CPU 机器上就是 `False`。

Git 身份：

```bash
git config --global user.name "your-name"
git config --global user.email "you@example.com"
```

SSH：

```bash
ssh-keygen -t ed25519 -C "you@example.com"
```
