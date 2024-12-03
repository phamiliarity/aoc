ans = 0
with open('input.txt') as input_obj:
    for line in input_obj:
        l, w, h = map(int, line.strip().split("x"))
        wrap = sum(sorted([l,w,h])[:2])*2
        bow = l*w*h
        ans += wrap + bow
print(ans)
