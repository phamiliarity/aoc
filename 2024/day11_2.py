STONE_CACHE = {} #{(stone_val, blink):n_stones}
def blink_recursive(stone, blink):
    if (stone, blink) in STONE_CACHE:
        return STONE_CACHE[(stone, blink)]

    sstone = str(stone)
    lstone = len(sstone)

    if blink == 0: #base case
        return 1
    if stone == 0:
        result = blink_recursive(1, blink - 1)
    elif len(sstone)%2 == 0:
        s1, s2 = sstone[:lstone//2], sstone[lstone//2:]
        result = sum((blink_recursive(s, blink - 1) for s in [int(s1), int(s2)]))
    else:
        result = blink_recursive(stone * 2024, blink - 1)

    STONE_CACHE[(stone, blink)] = result #add calcs to cache for later
    return result

stones = open('input.txt').read()
stones = list(map(int, stones.strip().split()))

ans = 0
n_blinks = 75
for stone in stones:
    ans += blink_recursive(stone, n_blinks)
print(ans)