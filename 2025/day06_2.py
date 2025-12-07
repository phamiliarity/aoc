def process_block(block, ans):
    ns = ["".join(c[:-1]).strip() for c in block]
    equation = block[0][-1].join(ns)
    ans += eval(equation) #eval my beloved <3
    return ans

grid = open("input.txt").read().split(("\n"))
transposed_grid = [list(row) for row in zip(*grid)]

ans = 0
block = []
for g in transposed_grid:    
    if set(g) == {" "}:
        ans = process_block(block, ans)
        block = []
    else:
        block.append(g)

ans = process_block(block, ans)
print(ans)
