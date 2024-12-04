import re

txt = open('input.txt').read()
muls = re.findall(r"mul\((\d+),(\d+)\)", txt)
ans = sum(int(a)*int(b) for a,b in muls)
print(ans)
