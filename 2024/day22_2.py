def process(n, steps):
    processed = [n]

    for _ in range(steps):
        n ^= (n * 64)
        n %= 16777216

        n ^= int((n/32) // 1)
        n %= 16777216

        n ^= n * 2048
        n %= 16777216
        processed.append(n)

    return processed
 
all_n = [int(l) for l in open("input.txt").read().splitlines()]

price_changes = {} #{secret_number : {prices : [...], changes : [...]}}
for n in all_n:
    processed = process(n, 2000)
    prices = [nn % 10 for nn in processed]
    changes = [b-a for a,b in zip(prices, prices[1:])]
    price_changes[n] = {"prices":prices, "changes":changes}

all_patterns = {}  # {pattern: {secret number: price}}
for n, data in price_changes.items():
    prices, changes = data.values()
    for i in range(len(changes) - 4):
        pattern = tuple(changes[i:i+4])
        if pattern not in all_patterns:
            all_patterns[pattern] = {}
        if n not in all_patterns[pattern]:
            all_patterns[pattern][n] = prices[i+4]

max_pattern = max(all_patterns, key=lambda p: sum(all_patterns[p].values()))
print(max_pattern, sum(all_patterns[max_pattern].values()))
