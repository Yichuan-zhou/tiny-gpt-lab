# git / PR

## 分支

```bash
git checkout -b week1-bootstrap
```

已经在 `week1-bootstrap` 上就不用再执行。

## 查看状态

```bash
git status
```

## 提交 commit

```bash
git add week01_bootstrap
git commit -m "week1 bootstrap"
```

## 推送

第一次推这个分支：

```bash
git push -u origin week1-bootstrap
```

后面继续推：

```bash
git push
```

## PR

- base: `main`
- branch: `week1-bootstrap`
- title: `Week 1 Bootstrap`

PR 里写：

- 跑了什么命令
- 改了什么代码
- 观察到什么现象
- 有没有卡住的问题
