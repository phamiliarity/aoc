import copy, re

def uncompress_dense_diskmap(diskmap_dense):
    """determine free and filled up space from diskmap
    """
    diskmap = [] 
    file_nr = 0
    for idx, nr in enumerate(diskmap_dense):
        if idx % 2 == 0:
            diskmap += [file_nr]*int(nr)
            file_nr += 1
        else:
            diskmap += ["."]*int(nr)
    return diskmap

def rearrange_files(diskmap):
    #im sorry for brute forcing this
    moved_diskmap = copy.deepcopy(diskmap)

    for idx1, ele1 in enumerate(moved_diskmap):

        #check if all gaps have been filled
        blocks = re.split(r"\.+", "".join(map(str, moved_diskmap)))
        n_free_blocks = len(blocks) - 1 #1 block contains files
        if n_free_blocks == 1:
            return moved_diskmap

        #fill gaps with files by swapping "." with file ids.
        if ele1 == ".":
            for idx_rev, ele2 in enumerate(moved_diskmap[::-1]):
                if ele2 == ".": continue

                idx2 = (len(moved_diskmap) - 1) - idx_rev
                moved_diskmap[idx1], moved_diskmap[idx2] = ele2, ele1
                break

diskmap_dense = open('input.txt').read().strip()

diskmap = uncompress_dense_diskmap(diskmap_dense)
moved_diskmap = rearrange_files(diskmap)

ans = 0
for idx, ele in enumerate(moved_diskmap):
    if type(ele) == int:
        ans += ele * idx
    else: break
print(ans)