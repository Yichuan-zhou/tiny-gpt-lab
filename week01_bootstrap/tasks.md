# Week 1 - Bootstrap Checklist

Start here after reading:

1. [`../README.md`](../README.md)
2. [`../docs/setup.md`](../docs/setup.md)

Goal for Week 1: get your environment working, practice the GitHub workflow, run a simple PyTorch training loop, and record what you observe.

---

## Checklist

### 1. Environment Setup

- [ ] Install Git
- [ ] Install VS Code or another editor
- [ ] Install Conda or another Python environment manager
- [ ] Create a Python environment for this lab
- [ ] Install PyTorch
- [ ] Run the environment check from [`../docs/setup.md`](../docs/setup.md)

Clear deliverable:

- In your submission `README.md`, record your Python version, PyTorch version, and whether CUDA is available.

### 2. GitHub Workflow Practice

- [ ] Clone the repository
- [ ] Create a branch named `week1-yourname`
- [ ] Make a small edit in your Week 1 submission files
- [ ] Commit your changes
- [ ] Push your branch
- [ ] Open a pull request into `main`

Clear deliverable:

- A pull request from your Week 1 branch to `main`.

### 3. Run The Starter Training Loop

- [ ] Open [`starter_code/train.py`](starter_code/train.py)
- [ ] Run the script
- [ ] Confirm that the loss changes over time
- [ ] Change the learning rate once
- [ ] Run the script again
- [ ] Compare the two runs

Clear deliverable:

- In `experiment.md`, record the command you ran, the learning rates you tried, and what happened to the loss.

### 4. Write An Experiment Log

- [ ] Copy [`submission_template/experiment.md`](submission_template/experiment.md) into your own submission folder
- [ ] Fill in the goal
- [ ] Fill in the setup
- [ ] Record at least one result
- [ ] Write one observation
- [ ] Write one question or next step

Clear deliverable:

- A completed `experiment.md` included in your pull request.

### 5. Prepare Your Week 1 Submission

- [ ] Copy [`submission_template/README.md`](submission_template/README.md) into your own submission folder
- [ ] Fill in your name
- [ ] Summarize what you completed
- [ ] Link or mention your experiment log
- [ ] List any problems you hit

Clear deliverable:

- A completed submission `README.md` included in your pull request.

---

## Final Submission Checklist

Before opening your pull request, make sure it includes:

- [ ] Your completed submission `README.md`
- [ ] Your completed `experiment.md`
- [ ] Any small changes you made to [`starter_code/train.py`](starter_code/train.py)
- [ ] A PR description that says what you ran, what changed, what you observed, and what questions you still have

## Discussion Questions

Be ready to discuss:

- Why does loss decrease?
- What does `backward()` do?
- Why do we call `zero_grad()`?
- Why do `w` and `b` use `requires_grad=True`?
- What can happen if the learning rate is too large?
