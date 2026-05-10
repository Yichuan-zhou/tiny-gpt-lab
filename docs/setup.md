# setup

## Requirements

- VS Code
- Python 3.10+
- Conda
- Git

## Python Environment

```bash
conda create -n tiny-gpt-lab python=3.10 -y
conda activate tiny-gpt-lab
pip install torch
```

## Verification

```bash
python --version
git --version
python -c "import torch; print(torch.__version__); print(torch.cuda.is_available())"
```

`CUDA False` is expected on CPU-only machines.

## Git Identity

```bash
git config --global user.name "your-name"
git config --global user.email "you@example.com"
```
