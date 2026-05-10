# Week 1

工作目录：

```text
week01_bootstrap/workspace/
```

本周文件：

- `workspace/README.md`
- `workspace/experiment.md`
- `workspace/train.py`

不改：

- `main`
- `starter_code/`

## 1. 环境

看：

- [`../docs/setup.md`](../docs/setup.md)

记到：

- `workspace/README.md`

## 2. 跑代码

```bash
python week01_bootstrap/workspace/train.py
```

记到：

- `workspace/experiment.md`

## 3. 改 learning rate

改：

```text
week01_bootstrap/workspace/train.py
```

不要改：

```text
week01_bootstrap/starter_code/train.py
```

至少跑两次：

- 原始 learning rate
- 修改后的 learning rate

记到：

- `workspace/experiment.md`

## 4. 补工作记录

填：

- `workspace/README.md`

写：

- 完成了什么
- 改了什么
- 看到什么
- 卡在哪里
- 周五想讨论什么

## 5. 提交

看：

- [`../docs/workflow.md`](../docs/workflow.md)

PR 里带上：

- `workspace/README.md`
- `workspace/experiment.md`
- `workspace/train.py`

## 周五讨论

- loss 为什么会下降
- `backward()` 做了什么
- 为什么要 `zero_grad()`
- 为什么 `w` / `b` 要 `requires_grad=True`
- learning rate 变大或变小时，loss 怎么变
