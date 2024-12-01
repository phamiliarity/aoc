n1, n2 = zip(*(map(int, line.split()) for line in open('input.txt')))
ans = sum(abs(a-b) for a,b in zip(sorted(n1), sorted(n2)))
print(ans)