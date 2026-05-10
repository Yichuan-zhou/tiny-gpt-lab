# git / PR

Branch：

```bash
git checkout -b week1-bootstrap
```

如果已经在 `week1-bootstrap` 上，不用重复执行这一行。

看一下当前改了什么：

```bash
git status
```

Commit：

```bash
git add week01_bootstrap
git commit -m "week1 bootstrap"
```

Push：

```bash
git push -u origin week1-bootstrap
```

如果这个 branch 之前已经 push 过，也可以直接：

```bash
git push
```

PR：

- base：`main`
- branch：`week1-bootstrap`
- title：`Week 1 Bootstrap`

写：

- 跑了什么
- 改了什么
- 看到什么
- 卡在哪里
