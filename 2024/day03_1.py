import re

with open('input.txt') as input_obj:
    txt = input_obj.read()

#regex my beloved
muls = re.findall(r"mul\((\d+),(\d+)\)", txt)
ans = sum(int(mul[0])*int(mul[1]) for mul in muls)
print(ans)
