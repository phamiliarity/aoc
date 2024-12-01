n1, n2 = zip(*(map(int, line.split()) for line in open('input.txt')))
ans = sum(i*n2.count(i) for i in n1)
print(ans)