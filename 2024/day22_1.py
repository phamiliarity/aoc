def process(n):
    n ^= (n * 64)
    n %= 16777216

    n ^= int((n/32) // 1)
    n %= 16777216

    n ^= n * 2048
    n %= 16777216

    return n

all_n = [int(l) for l in open("input.txt").read().splitlines()]

ans = 0
for n in all_n:
    new_n = n
    for i in range(2000):
        new_n = process(new_n)
    ans += new_n
print(ans)