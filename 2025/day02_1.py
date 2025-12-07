text = open("input.txt").read().split((","))

ans = 0

for p in text:
    p1, p2 = map(int, p.split("-"))

    for id in range(p1, p2+1):
        id = str(id)
        hl = len(id)//2
        id1 = id[:hl]
        id2 = id[hl:]

        if id1 == id2:
            ans += int(id)

print(ans)
