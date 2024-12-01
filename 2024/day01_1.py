def parse_input(input_path):
    with open(input_path) as input_obj:
        n1, n2 = [], []
        for line in input_obj:
            n = line.split(' ')
            n1.append(int(n[0]))
            n2.append(int(n[-1]))
    return n1, n2

def calc_sorted_differences(n1, n2):
    diff = 0
    for pair in zip(sorted(n1), sorted(n2)):
        diff += abs(pair[0]-pair[1])
    return diff

n1, n2 = parse_input('input.txt')
diff = calc_sorted_differences(n1, n2)
print(diff)
