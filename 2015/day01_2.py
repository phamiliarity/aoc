txt = open('input.txt').read()

curr = 0
for pos, floor in enumerate(txt, 1):
    curr += {"(" : 1, ")" : -1}.get(floor)
    if curr < 0:
        print(pos)
        break
