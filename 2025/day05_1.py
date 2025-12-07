text = open("input.txt").read().split("\n\n")
fresh = text[0].split("\n")
avail = text[1].split("\n")

ans = 0

for a in avail:
    for f in fresh:
        f1, f2 = map(int, f.split("-"))
        if f1 <= int(a) <= f2:
            ans +=1
            break

print(ans)
