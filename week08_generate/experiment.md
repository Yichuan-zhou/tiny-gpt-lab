# experiment

## 采样 A

命令：

```bash
python -m gpt_lab.sample --config configs/dev.yaml --ckpt checkpoints/dev/best.pt --prompt "ROMEO:" --temperature 0.8 --top-k 40
```

- `temperature`: 0.8
- `top_k`: 40
- 生成片段:

```
ROMEO:

Doy gtey turmy dsae he she mot fe w lofr me
Woou siur gn p inirt ind ss che foutheis s dee
Go the y,
Tbud ng l; the ien me ardelin  for s, fan, merprer thinsTht seeot wou at llmeeu ase t

kerse men'
```

## 采样 B（改 temperature）

命令：

```bash
python -m gpt_lab.sample --config configs/dev.yaml --ckpt checkpoints/dev/best.pt --prompt "ROMEO:" --temperature 1.2 --top-k 40
```

- 生成片段:

```
ROMEO:;p Sore?
Lil:
Al, se awn the?N
 inwe shhein f l toglet,

D hef t:eart hanegt 
A'ta kit fe! cy thal uradhrou rrys atgs
h. meaifow bndthens


LANTho sbe fol ll Mil a,Aximerwer sy theurtther t:? epor,
Th
```

- 与 A 的差异: temperature 更高（1.2）时分布更平，采样更随机，出现更多标点/大写/非常规拼写；0.8 时更保守、重复模式略多。

## 观察

- 采样流程（每步）：`idx` → model forward → 取最后位置 `logits` → 除以 `temperature` → `top_k` 截断 → softmax → `multinomial` 抽下一个 token → 拼到序列末尾，重复 `max_new_tokens` 次。
- `temperature < 1` 锐化分布（更确定）；`temperature > 1`  flatten 分布（更随机）。
- `top_k=40` 只保留概率最高的 40 个 token 再采样，避免极低概率乱码 token。
- 同一 checkpoint（best.pt, step=499），两种 temperature 输出风格明显不同，满足对比要求。
