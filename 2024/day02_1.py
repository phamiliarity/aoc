def parse_input(input_path):
    with open(input_path) as input_obj:
        n = [list(map(int, line.split())) for line in input_obj]
    return n

def check_consistent_change(nn):
    if nn == sorted(nn) or nn == sorted(nn, reverse=True):
        return True
    return False

def check_diff(nn):
    for idx in range(len(nn)-1):
        if abs(nn[idx] - nn[idx+1]) not in [1,2,3]:
            return False
    return True

n = parse_input('input.txt')
ans = 0
for nn in n:
    if check_consistent_change(nn) and check_diff(nn):
        ans+=1
print(ans)
