text = open("input.txt").read().split(("\n"))

p = 50
ans = 0

for ii in text:
    d = ii[0]
    t = int(ii[1:])

    for _ in range(t):
        p = (p + 1) % 100 if d == "R" else (p - 1) % 100
        if p == 0:
            ans += 1

print(ans)
