def blink(stone):
    new_stones = []
    sstone = str(stone)
    length = len(sstone)

    if stone == 0:
        new_stones.append(1)
    elif len(sstone)%2 == 0:
        s1, s2 = sstone[:length//2], sstone[length//2:]
        new_stones += [int(s1), int(s2)]
    else:
        new_stones.append(stone * 2024)

    return new_stones

stones = list(map(int, open('input.txt').read().strip().split()))
n_blinks = 25
for i in range(n_blinks):
    new_stones = []
    for stone in stones:
        new_stones += blink(stone)
    stones = new_stones
print(len(new_stones))

