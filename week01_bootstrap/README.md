# week01_bootstrap

## 文件

- `train.py`：可直接运行的训练脚本
- `experiment.md`：记录 `loss`、`lr` 和观察
- `notes.md`：记录环境、改动和卡住的问题

## 运行

```bash
python week01_bootstrap/train.py
```

脚本会自动选择：

- 有 CUDA：`cuda`
- 没有 CUDA：`cpu`

先确认输出里的 `device=`。

## 修改

先改这些：

- `lr`
- 训练步数
- `noise` 大小

改动放在：

```text
week01_bootstrap/
```

## 记录

更新：

- `experiment.md`
- `notes.md`

记录这些信息：

- 运行命令
- `device`
- 改了什么值
- `loss` 怎么变化
- 报错或卡住的地方

## 提交

按这里走：

- [`../docs/workflow.md`](../docs/workflow.md)

PR 里写清楚：

- 跑了什么命令
- 用的是 `cpu` 还是 `cuda`
- 改了什么代码
- 观察到什么现象
- 有没有卡住的问题
