# experiment

## 运行 1

命令：

```bash
python week01_bootstrap/train.py
```

- `lr`: 0.1
- `steps`: 200
- `noise`: 0.3
- `batch_size`: 16
- `device`: cpu
- 开始几步的 `train_loss / eval_loss`:
  - step=000: train_loss=1.7009 / eval_loss=3.3268
  - step=020: train_loss=0.0663 / eval_loss=0.0725
- 最后几步的 `train_loss / eval_loss`:
  - step=180: train_loss=0.0822 / eval_loss=0.0843
  - step=199: train_loss=0.0534 / eval_loss=0.1001
- 最后的 `w / b`: w=2.0579, b=0.9949
- 变化：下降（loss 从约 1.7 降到约 0.05；eval_loss 同步下降）
- 备注：w、b 接近真实值 2 和 1；中间有小幅波动属正常

## 运行 2

命令：

```bash
python week01_bootstrap/train.py
```

（运行前将 `train.py` 中 `lr` 改为 `0.01`，其余参数不变）

- `lr`: 0.01
- `steps`: 200
- `noise`: 0.3
- `batch_size`: 16
- `device`: cpu
- 开始几步的 `train_loss / eval_loss`:
  - step=000: train_loss=1.7009 / eval_loss=6.2691
  - step=020: train_loss=0.6894 / eval_loss=2.3777
- 最后几步的 `train_loss / eval_loss`:
  - step=180: train_loss=0.0952 / eval_loss=0.0668
  - step=199: train_loss=0.0601 / eval_loss=0.0683
- 最后的 `w / b`: w=2.0061, b=0.9794
- 变化：下降（整体趋势向下，但比 lr=0.1 慢）
- 备注：同样 200 步时 w、b 已接近 2 和 1，但前期 eval_loss 更高、收敛更慢

## 观察

- `lr=0.1` 时约 20 步后 loss 就明显变小；`lr=0.01` 前几十步 eval_loss 仍较高，说明学习率小则每步更新慢。
- 两次运行最终 w、b 都接近 2 和 1，说明在合适步数下两种 lr 都能学到直线关系。
- 若把 lr 再加大（如 0.5）可能出现震荡，可作为后续可选实验。
