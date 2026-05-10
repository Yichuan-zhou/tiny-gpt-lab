# Environment Setup

## Required Tools
Install the following:
- VS Code
- Python (recommended: 3.10+)
- Conda (Miniconda or Anaconda)
- Git

## Optional but Recommended
- tmux
- SSH key pair for GitHub and remote servers

## Create Python Environment
```bash
conda create -n tiny-gpt-lab python=3.10 -y
conda activate tiny-gpt-lab
pip install torch
```

## Git + SSH Quick Checklist
1. Configure Git identity:
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```
2. Generate SSH key (if needed):
```bash
ssh-keygen -t ed25519 -C "you@example.com"
```
3. Add public key to GitHub.

## Verify Environment
Run this in Python:

```python
import torch
print(torch.__version__)
print(torch.cuda.is_available())
```

Expected:
- Torch imports successfully
- CUDA availability reflects your machine/driver setup (`True` on configured GPU environments)

## Terminal Basics (Week 1)
Must be comfortable with:
- `ssh`
- `tmux`
- `pwd`
- `ls`
- `cd`
- `mkdir`
