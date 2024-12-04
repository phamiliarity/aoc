directions = {"upleft":(-1,-1), "up":(-1,0), "upright":(-1,1),
              "left":(0,-1), "right":(0,1),
              "downleft":(1,-1), "down":(1,0), "downright":(1,1)}

word = list("XMAS")

with open('input.txt') as input_obj:
    grid = input_obj.read().strip().split("\n")

ans = 0

#loop through each character
for i, row in enumerate(grid):
    for j, _ in enumerate(row):

        #get the chars to inspect in range of searched word
        neighbours = {}
        steps = range(len(word))

        for direction in directions:
            x, y = directions.get(direction)
            
            for step in steps:
                try:
                    new_i = i+x*step
                    new_j = j+y*step
                    
                    #inspecting coords should stay in grid limits
                    if new_i < 0 or new_i > len(row) \
                        or new_j < 0 or new_j > len(grid):
                        continue
                        
                    neighbours[direction].append(grid[i+x*step][j+y*step])
                
                except KeyError:
                    neighbours[direction] = [grid[i+x*step][j+y*step]]
                except IndexError:
                    continue
    
        ans += list(neighbours.values()).count(word)
print(ans)
