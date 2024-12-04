import re

pattern = r"don't\(\).+?do\(\)|don't\(\).*$"
txt = re.sub(pattern, "", open('input.txt').read(), flags=re.DOTALL)
muls = re.findall(r"mul\((\d+),(\d+)\)", txt)
ans = sum(int(a)*int(b) for a,b in muls)
print(ans)
