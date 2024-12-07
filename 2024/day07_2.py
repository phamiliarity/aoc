def make_permutation_masks(length, current=""):
    if length == 0:
        return [current]
    return (make_permutation_masks(length - 1, current + "+") +
            make_permutation_masks(length - 1, current + "*") +
            make_permutation_masks(length - 1, current + "|"))

data = [line.split(": ") for line in open('input.txt').read().splitlines()]
data = [(int(ans), list(map(int, values.split()))) for ans, values in data]

ans = 0
for ans_check, values in data:
    n_vals = len(values)
    masks = make_permutation_masks(n_vals-1, current="")
    
    for mask in masks:
        ans_calc = values[0]

        for i in range(len(mask)):
            if mask[i] == "*":
                ans_calc = ans_calc * values[i+1]
            if mask[i] == "+":
                ans_calc = ans_calc + values[i+1]
            if mask[i] == "|":
                ans_calc = int("".join([str(ans_calc), str(values[i+1])]))

        if ans_calc == ans_check:
            ans = ans + ans_check
            break
print(ans)
