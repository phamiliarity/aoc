import re
import numpy as np

txt = open("input.txt").read().strip().split("\n\n")
claw_machines = []
for claw_machine in txt:
    match = re.search("Button A: X\+(\d+), Y[\+=](\d+)\nButton B: X\+(\d+), Y[\+=](\d+)\nPrize: X=(\d+), Y=(\d+)", claw_machine)
    
    a = tuple(map(int, [match.group(1), match.group(2)]))
    b = tuple(map(int, [match.group(3), match.group(4)]))
    prize = tuple(map(int, [match.group(5), match.group(6)]))
    claw_machines.append((a,b,prize))

ans = 0
for a, b, prize in claw_machines:
    #rewrite to linear equations and solve
    x = [a[0], b[0]]
    y = [a[1], b[1]]
    
    A = np.array([x,y])
    z = np.array(prize)
    
    q = np.linalg.solve(A,z)
    
    #valid solution if value for x and y are integers
    sol = tuple(map(round, (q)))
    if sol[0]*a[0] + sol[1]*b[0] == prize[0] and sol[0]*a[1] + sol[1]*b[1] == prize[1]: #check if the solution is correct after rounding
        cost = sol[0]*3 + sol[1]
        ans += cost
print(ans)