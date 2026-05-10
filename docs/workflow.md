# 日常 Git / PR 工作流

这个仓库已经存在，不需要重新创建 remote。日常只需要围绕一个节奏走：

```text
clone -> branch -> edit -> commit -> push -> PR
```

## 1. Clone

第一次拿到仓库时：

```bash
git clone https://github.com/inhalc/tiny-gpt-lab.git
cd tiny-gpt-lab
```

## 2. Branch

不要直接改 `main`。每周工作先开一个 branch：

```bash
git checkout -b week1-bootstrap
```

## 3. Edit

本周所有修改都放在：

```text
week01_bootstrap/workspace/
```

先复制模板和 starter code：

```bash
mkdir -p week01_bootstrap/workspace
cp week01_bootstrap/submission_template/README.md week01_bootstrap/workspace/README.md
cp week01_bootstrap/submission_template/experiment.md week01_bootstrap/workspace/experiment.md
cp week01_bootstrap/starter_code/train.py week01_bootstrap/workspace/train.py
```

然后只改 `workspace/` 里的文件。

## 4. Commit

把本周工作记录下来：

```bash
git add week01_bootstrap/workspace
git commit -m "week1 bootstrap"
```

## 5. Push

把 branch 推到 GitHub：

```bash
git push -u origin week1-bootstrap
```

## 6. PR

在 GitHub 上打开 Pull Request：

- Base branch：`main`
- Compare branch：`week1-bootstrap`
- PR 标题：`Week 1 Bootstrap`

PR 说明里写四件事：

- 我运行了什么
- 我修改了什么
- 我观察到了什么
- 我卡在哪里，想讨论什么

PR 是我们讨论的地方，不只是提交结果的地方。
