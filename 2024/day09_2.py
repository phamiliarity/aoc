def parse_diskmap(diskmap_dense):
    file_map = {}
    free_spaces = []

    file_nr = 0
    pos = 0
    for idx, size in enumerate(diskmap_dense):
        size = int(size)
        if idx % 2 == 0:
            file_map[file_nr] = (pos, size)
            file_nr += 1
        else:
            free_spaces.append((pos, size))
        pos += size
    return file_map, free_spaces

def rearrange_files(file_map, free_spaces):
    #note: makes in place changes

    #loop through each file from right to left
    for file_nr in reversed(file_map.keys()):
        file_pos, file_size = file_map[file_nr]

        #inspect free spaces from left to right
        for space_idx in range(len(free_spaces)):
            space_pos, space_size = free_spaces[space_idx] 

            if file_pos < space_pos:
                continue
            if file_size <= space_size:
                file_map[file_nr] = (space_pos, file_size)

                #determine how much space is left:
                #if entire space is filled, remove space from the list
                if file_size == space_size:
                    free_spaces.pop(space_idx)
                #if space is left, update the value in the list.
                else:
                    free_spaces[space_idx] = (space_pos + file_size, space_size - file_size)
                #stop analysing the file, move to the next
                break
    return file_map

diskmap = open('input.txt').read().strip()

file_map, free_spaces = parse_diskmap(diskmap)
rearrange_files(file_map, free_spaces)

ans = 0
for file_nr in file_map:
    file_pos, file_size = file_map[file_nr]
    for i in range(file_pos, file_pos+file_size):
        ans += i * file_nr
print(ans)

#defo should revisit p1 sometime