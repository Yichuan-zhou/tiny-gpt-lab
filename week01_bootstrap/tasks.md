# Week 1 Bootstrap 操作手册

## 本周目标

这周只做三件事：

1. 配好环境
2. 跑通第一个 PyTorch 训练循环
3. 用 PR 提交本周工作记录、实验日志和代码改动

## 本周最终产出

所有本周修改都放在：

```text
week01_bootstrap/workspace/
```

最终 PR 至少包含：

- `week01_bootstrap/workspace/README.md`
- `week01_bootstrap/workspace/experiment.md`
- `week01_bootstrap/workspace/train.py`

不要直接改 `main`，也不要直接改 `starter_code/`。`starter_code/` 只作为原始参考。

## 一次性准备命令

从仓库根目录运行：

```bash
git checkout -b week1-bootstrap
mkdir -p week01_bootstrap/workspace
cp week01_bootstrap/submission_template/README.md week01_bootstrap/workspace/README.md
cp week01_bootstrap/submission_template/experiment.md week01_bootstrap/workspace/experiment.md
cp week01_bootstrap/starter_code/train.py week01_bootstrap/workspace/train.py
```

准备好以后，本周只在 `week01_bootstrap/workspace/` 里修改。

---

## 任务 1：检查环境

做什么：

- 确认 Python、Git、PyTorch 能正常运行。

怎么做：

```bash
python --version
git --version
python -c "import torch; print(torch.__version__); print(torch.cuda.is_available())"
```

产出是什么：

- 把 Python 版本、PyTorch 版本、CUDA 是否可用写进 `workspace/README.md`。
- `CUDA False` 不一定是错误，取决于你是不是在 GPU 机器上运行。

## 任务 2：跑通第一个训练循环

做什么：

- 运行复制到 `workspace/` 里的训练脚本。

怎么做：

```bash
python week01_bootstrap/workspace/train.py
```

产出是什么：

- 在 `workspace/experiment.md` 里记录这次运行的命令。
- 记录 loss 大致是下降、震荡，还是没有明显变化。

## 任务 3：改一次 learning rate

做什么：

- 在 `week01_bootstrap/workspace/train.py` 里改一次 learning rate。
- 不要改 `week01_bootstrap/starter_code/train.py`。

怎么做：

1. 打开 `week01_bootstrap/workspace/train.py`
2. 找到参数更新里的 `0.1`
3. 改成另一个值，比如 `0.01` 或 `1.0`
4. 再运行一次：

```bash
python week01_bootstrap/workspace/train.py
```

产出是什么：

- 在 `workspace/experiment.md` 里记录两个实验：
  - 原始 learning rate
  - 修改后的 learning rate
- 对比两次 loss 变化，并写一句你的观察。

## 任务 4：整理本周工作记录

做什么：

- 填写 `workspace/README.md`。

怎么做：

- 写清楚本周完成了什么。
- 写清楚你修改了什么。
- 写清楚你观察到了什么。
- 写清楚你卡在哪里。
- 写下周五想讨论的问题。

产出是什么：

- 一个能让我快速了解你本周过程的 `workspace/README.md`。

## 任务 5：提交并打开 PR

做什么：

- commit 当前 `workspace/` 内容，push 到 GitHub，然后打开 PR。

怎么做：

```bash
git add week01_bootstrap/workspace
git commit -m "week1 bootstrap"
git push -u origin week1-bootstrap
```

然后在 GitHub 上打开 Pull Request：

- Base branch：`main`
- Compare branch：`week1-bootstrap`
- PR 标题：`Week 1 Bootstrap`
- PR 说明：写你运行了什么、改了什么、观察到了什么、卡在哪里

产出是什么：

- 一个可以讨论的 PR。

## 周五我们会围绕这些问题讨论

- 为什么 loss 会下降？
- `backward()` 做了什么？
- 为什么要调用 `zero_grad()`？
- 为什么 `w` 和 `b` 要设置 `requires_grad=True`？
- learning rate 太大或太小时，loss 可能会有什么变化？
