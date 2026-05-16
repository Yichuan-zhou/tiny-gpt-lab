import torch

torch.manual_seed(0)

device = "cuda" if torch.cuda.is_available() else "cpu"

# 模拟数据：y = 2x + 1，再加一点噪声
x = torch.linspace(-3, 3, 100, device=device).unsqueeze(1)
noise = 0.3 * torch.randn(100, 1, device=device)
y = 2 * x + 1 + noise

train_x, eval_x = x[:80], x[80:]
train_y, eval_y = y[:80], y[80:]

# 需要学习的参数
w = torch.randn(1, device=device, requires_grad=True)
b = torch.randn(1, device=device, requires_grad=True)

lr = 0.1
steps = 200
batch_size = 16

print(f"device={device}")
print(f"start: w={w.item():.4f}, b={b.item():.4f}, lr={lr}")

for step in range(steps):
    idx = torch.randint(0, train_x.shape[0], (batch_size,), device=device)
    batch_x = train_x[idx]
    batch_y = train_y[idx]

    pred = w * batch_x + b
    train_loss = ((pred - batch_y) ** 2).mean()

    train_loss.backward()

    with torch.no_grad():
        w -= lr * w.grad
        b -= lr * b.grad

        w.grad.zero_()
        b.grad.zero_()

    if step % 20 == 0 or step == steps - 1:
        with torch.no_grad():
            eval_pred = w * eval_x + b
            eval_loss = ((eval_pred - eval_y) ** 2).mean()

        print(
            f"step={step:03d} "
            f"train_loss={train_loss.item():.4f} "
            f"eval_loss={eval_loss.item():.4f} "
            f"w={w.item():.4f} b={b.item():.4f}"
        )
