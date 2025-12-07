text = open("input.txt").read().split((","))

ans = set()

for p in text:
    p1, p2 = map(int, p.split("-"))

    for id in range(p1, p2+1):
        id = str(id)
        hl = len(id)//2
        id1 = id[:hl]
        id2 = id[hl:]

        for idx in range(1, len(id)):
            substr = id[:idx]
            repeat = int(len(id) / idx)

            test = substr*repeat
            if test == id:
                ans.add(int(id))
            
print(sum(ans))
