def uncompress_dense_diskmap(diskmap_dense):
    diskmap = [] 
    file_nr = 0
    for idx, nr in enumerate(diskmap_dense):
        if idx % 2 == 0:
            diskmap += [file_nr]*int(nr)
            file_nr += 1
        else:
            diskmap += ["."]*int(nr)
    return diskmap

def rearrange_files(diskmap, free_spaces):
    """fill gaps by looping through gaps, rather than looping through every 
    single element and comparing it with all elements in the map like my first
    attempt. 
    
    note: in-place changes"""
    for space_pos in free_spaces:
        #check if diskmap is as small as possible
        if space_pos > len(diskmap): #e.g. this would expand the thingy again
            return None
        #find first file fragment from right to left
        while type(diskmap[-1]) != int:
            diskmap.pop(-1)

        diskmap[space_pos] = diskmap[-1]
        diskmap.pop(-1)

diskmap_dense = open('input.txt').read().strip()
diskmap = uncompress_dense_diskmap(diskmap_dense)

free_spaces = [i for i, ele in enumerate(diskmap) if ele == "."]
rearrange_files(diskmap, free_spaces)

ans = 0
for idx, ele in enumerate(diskmap):
    if type(ele) == int:
        ans += ele * idx
    else: break
print(ans)