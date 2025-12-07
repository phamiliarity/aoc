grid = open("input.txt").read().split(("\n"))
for idx, g in enumerate(grid):
    grid[idx] = list(g)
m = len(grid)
n = len(grid[0])

ans = 0

start = next(((ii, jj) for ii in range(m)
              for jj in range(n) if grid[ii][jj] == "S"))
q = [start]
seen = set()
while q:
    ipos, jpos = q.pop(0)
    if (ipos, jpos) in seen:
        continue
    seen.add((ipos, jpos))

    nipos = ipos + 1
    njpos = jpos

    try:
        nchar = grid[nipos][njpos]
        if nchar == "^":
            q.append((ipos, njpos-1))
            q.append((ipos, njpos+1))
            ans += 1
        else:
            q.append((nipos, jpos))
            grid[nipos][njpos] = "|"

    except IndexError:
        continue

for g in grid: print("".join(g))

print(ans)
