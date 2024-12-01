def parse_input(input_path):
    with open(input_path) as input_obj:
        n1, n2 = [], []
        for line in input_obj:
            n = line.split(' ')
            n1.append(int(n[0]))
            n2.append(int(n[-1]))
    return n1, n2

def calc_similarity(n1, n2):
    score = 0
    for i in n1:
        n_occurrence = n2.count(i)
        score += i*n_occurrence
    return score
    
n1, n2 = parse_input('input.txt')
score = calc_similarity(n1, n2)
print(score)