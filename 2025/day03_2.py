text = open("input.txt").read().split(("\n"))

ans = []

for b in text:
    joltage = ""

    while len(joltage) < 12:
        n_to_fit = 12 - len(joltage)
        n_options = len(b) - n_to_fit

        options = enumerate(b[: n_options + 1])
        sorted_opts = sorted(options, key=lambda x: x[-1], reverse=True)
        best = sorted_opts[0][1]
        idx = sorted_opts[0][0]
        joltage += best

        b = b[idx + 1:]

    ans.append(int(joltage))

print(sum(ans))
