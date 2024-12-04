
coords_to_check = ((-1,-1), (-1,1), (0,0), (1,-1), (1,1)) #hard-coded but would be nice to make it refer to a given word..


ans = 0
with open('input.txt') as input_obj:
    grid = input_obj.read().strip().split("\n")

#loop through each character
for i, row in enumerate(grid):
    for j, _ in enumerate(row):
        #get the neighbouring letters in range of searched word
        neighbours = {}

        for direction in coords_to_check:
            x, y = direction
            
            try:
                new_i = i+x
                new_j = j+y
                
                
                #position has to stay within bounds
                if new_i < 0 or new_i > len(grid) -1 \
                    or new_j < 0 or new_j > len(row)-1:
                    continue
                    
                neighbours[direction] = grid[new_i][new_j]
            except IndexError:
                continue
        
        #no X pattern could be made
        if len(neighbours.keys()) != len(coords_to_check): 
            continue
        
        #invalid when centre is not 'A'
        if neighbours[(0,0)] != "A":
            continue
        
        #check left-to-right diagonal
        if [neighbours[(-1,-1)], neighbours[(1,1)]] not in [["M", "S"], ["S", "M"]]:
            continue
            
        #check right-to-left diagonal
        if [neighbours[(-1,1)], neighbours[(1,-1)]] not in [["M", "S"], ["S", "M"]]:
            continue
            
        ans += 1
print(ans)
