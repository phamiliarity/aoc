text = open("input.txt").read().split(("\n"))

ans = []

for b in text:
    b = list(enumerate(b))
    b1 = sorted(b, key=lambda x: x[-1], reverse=True) 

    if b1[0][0] != len(b)-1:
        bb1 = b1[0]
    else:
        bb1 = b1[1]

    b2 = b[bb1[0]+1:]
    b2 = sorted(b2, key=lambda x: x[-1], reverse=True) 
    bb2 = b2[0]

    ans.append(int(bb1[1] + bb2[1]))

print(sum(ans))
