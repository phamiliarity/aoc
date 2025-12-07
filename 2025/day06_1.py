text = open("input.txt").read().split(("\n"))
grid = [t.split() for t in text]
transposed_grid = [list(row) for row in zip(*grid)]

ans = 0
for g in transposed_grid:
    equation = g[-1].join(g[:-1])
    ans += eval(equation) #eval my beloved <3
print(ans)
