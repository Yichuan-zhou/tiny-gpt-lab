import torch

# x/y 是一组模拟数据：目标关系是 y = 2x + 1
x = torch.randn(100, 1)
y = 2 * x + 1

# w/b 是模型要从数据里学出来的参数
w = torch.randn(1, requires_grad=True)
b = torch.randn(1, requires_grad=True)

for step in range(100):
    pred = w * x + b
    loss = ((pred - y) ** 2).mean()

    # 根据 loss 计算 w/b 的梯度
    loss.backward()

    with torch.no_grad():
        w -= 0.1 * w.grad
        b -= 0.1 * b.grad

        # 清空旧梯度，避免下一步重复累加
        w.grad.zero_()
        b.grad.zero_()

    print(step, loss.item())
