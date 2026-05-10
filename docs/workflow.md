# git / PR

## Branch

```bash
git checkout -b week1-bootstrap
```

Skip this if already on `week1-bootstrap`.

## Inspect

```bash
git status
```

## Commit

```bash
git add week01_bootstrap
git commit -m "week1 bootstrap"
```

## Push

First push:

```bash
git push -u origin week1-bootstrap
```

Later pushes:

```bash
git push
```

## PR

- base: `main`
- branch: `week1-bootstrap`
- title: `Week 1 Bootstrap`

Include:

- command run
- code change
- observed behavior
- blocker, if any
