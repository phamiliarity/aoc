txt = open('input.txt').read()
ans = txt.count("(") - txt.count(")")
print(ans)
