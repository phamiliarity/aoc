ans = 0
with open('input.txt') as input_obj:
    for line in input_obj:
        l, w, h = map(int, line.strip().split("x"))
        ans += (2*l*w + 2*w*h + 2*h*l) + min(l*w,l*h, h*w)
print(ans)
