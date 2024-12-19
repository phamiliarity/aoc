cache = {}
def find_match(design):
    global patterns
    if design in cache:
        return cache[design]
    
    if len(design) == 0:
        return 1
   
    match = 0
    for pattern in patterns:
        if design.startswith(pattern):
            match += find_match(design[len(pattern):])
    cache[design] = match
    return cache[design]

patterns, designs = open("input.txt").read().split("\n\n")
patterns = patterns.split(", ")
patterns.sort(key=lambda x:len(x), reverse=True)
designs = designs.split()

ans = 0
for design in designs:
    ans += 1 if find_match(design) > 0 else 0
print(ans)
