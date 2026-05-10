# 环境配置

## 必备工具

请先安装：

- VS Code
- Python（推荐 3.10+）
- Conda (Miniconda or Anaconda)
- Git

## 可选但推荐

- tmux
- GitHub 和远程服务器使用的 SSH key

## 创建 Python 环境

```bash
conda create -n tiny-gpt-lab python=3.10 -y
conda activate tiny-gpt-lab
pip install torch
```

## Git + SSH 快速检查

1. 配置 Git 身份：

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

2. 如果还没有 SSH key，可以生成一个：

```bash
ssh-keygen -t ed25519 -C "you@example.com"
```

3. 把 public key 添加到 GitHub。

## 检查环境

在 Python 中运行：

```python
import torch
print(torch.__version__)
print(torch.cuda.is_available())
```

你需要确认：

- `torch` 可以正常 import
- `torch.cuda.is_available()` 的输出符合你的机器环境  
  - 如果机器配置了可用 GPU/CUDA，通常应该是 `True`
  - 如果是普通 CPU 环境，看到 `False` 也可以接受

## 第 1 周需要熟悉的 terminal 命令

至少要知道这些命令在做什么：

- `ssh`
- `tmux`
- `pwd`
- `ls`
- `cd`
- `mkdir`
