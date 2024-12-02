def is_safe(nn):
    diffs = [nn[idx] - nn[idx+1] for idx in range(len(nn)-1)]
    return all(d in [1, 2, 3] for d in diffs) \
        or all(d in [-1, -2, -3] for d in diffs)

n = [list(map(int, line.split())) for line in open('input.txt')]
ans = sum(any(is_safe(nn[:idx] + nn[idx+1:]) for idx in range(len(nn))) \
            for nn in n)
print(ans)
