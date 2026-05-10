# Tiny GPT Lab

一个小型 GPT/LLM research workflow 仓库。目标不是把概念一次讲完，而是每周完成一点真实动作：运行、观察、记录、提交、讨论。

项目地址：https://github.com/inhalc/tiny-gpt-lab

## 现在只需要做三件事

1. 配环境
2. 跑通第一个训练循环
3. 用 PR 提交本周工作记录

## 第一次打开仓库，按这个顺序看

1. [`README.md`](README.md)
2. [`docs/setup.md`](docs/setup.md)
3. [`week01_bootstrap/tasks.md`](week01_bootstrap/tasks.md)

当前阶段：**Week 1 Bootstrap**

本周入口：[`week01_bootstrap/tasks.md`](week01_bootstrap/tasks.md)

本周真正工作的地方：[`week01_bootstrap/workspace/`](week01_bootstrap/workspace/)

## 本周要完成什么

- 配好 Python / PyTorch / Git 环境
- 跑通 `starter_code/train.py`
- 把 starter code 复制到 `workspace/` 后再修改
- 记录一次 learning rate 对 loss 的影响
- 开一个 PR，里面包含工作记录、实验日志和代码改动

## 最小 Git 工作流

不要直接改 `main`。每周先开自己的 branch。

```bash
git clone https://github.com/inhalc/tiny-gpt-lab.git
cd tiny-gpt-lab
git checkout -b week1-bootstrap

mkdir -p week01_bootstrap/workspace
cp week01_bootstrap/submission_template/README.md week01_bootstrap/workspace/README.md
cp week01_bootstrap/submission_template/experiment.md week01_bootstrap/workspace/experiment.md
cp week01_bootstrap/starter_code/train.py week01_bootstrap/workspace/train.py

python week01_bootstrap/workspace/train.py

git add week01_bootstrap/workspace
git commit -m "week1 bootstrap"
git push -u origin week1-bootstrap
```

然后在 GitHub 上打开 Pull Request：

- Base branch：`main`
- Compare branch：`week1-bootstrap`
- PR 标题：`Week 1 Bootstrap`
- PR 说明：写清楚你运行了什么、改了什么、观察到了什么、卡在哪里

## 这次 PR 里应该有什么

这里不需要写成正式文档，重点是留下这周实际做事的轨迹。

PR 至少包含：

- `week01_bootstrap/workspace/README.md`：本周工作记录
- `week01_bootstrap/workspace/experiment.md`：实验日志
- `week01_bootstrap/workspace/train.py`：你实际运行和修改的代码

## 遇到问题怎么记

卡住时先记录下来，不需要等完全解决：

- 我运行了什么命令
- 我看到了什么输出或错误
- 我改过什么
- 我猜可能是什么原因
- 我想周五讨论什么

记录得越具体，我们讨论时越容易定位问题。

## 仓库地图

- [`docs/setup.md`](docs/setup.md)：环境配置
- [`docs/workflow.md`](docs/workflow.md)：日常 Git / PR 工作流
- [`week01_bootstrap/tasks.md`](week01_bootstrap/tasks.md)：Week 1 操作手册
- [`week01_bootstrap/starter_code/train.py`](week01_bootstrap/starter_code/train.py)：原始 starter code，不直接改
- [`week01_bootstrap/submission_template/`](week01_bootstrap/submission_template/)：工作记录和实验日志模板
- [`week01_bootstrap/workspace/`](week01_bootstrap/workspace/)：本周真正工作的地方
