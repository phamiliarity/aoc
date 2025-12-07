text = open("input.txt").read().split("\n\n")
fresh = text[0].strip().split("\n")

ranges = [tuple(map(int, line.strip().split('-'))) 
          for line in fresh]
ranges.sort(key=lambda x: x[0])

merged = []
for start, end in ranges:
    if not merged:
        merged.append([start, end])
        continue
    prev_start, prev_end = merged[-1]
    if start <= prev_end:
        merged[-1][1] = max(prev_end, end)
    else:
        merged.append([start, end])

ans = 0
for r in merged:
    start, end = r
    n = end - start + 1
    ans += n
print(ans)
