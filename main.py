from pathlib import Path
import anytree.cachedsearch
from anytree import AnyNode
import time

def set_cover(U, S, submap, current):
    global min_node
    if not U:
        if min_node == root or current.depth < min_node.depth:
            min_node = current
        return

    for s in min_of_map(submap):
        temp_u = list(filter(lambda n: n not in S[s - 1], U))
        temp_s = list(map(lambda n: [] if n in S[s - 1] else submap[n], range(len(submap))))
        temp_node = AnyNode(u=temp_u, set=s)

        temp_node.parent = current
        if current.depth + 1 == min_node.depth:
            temp_node.parent = None
            return
        elif anytree.cachedsearch.findall(current.root, lambda node: node.u == temp_u and temp_node.depth > node.depth) != ():
            temp_node.parent = None
            return
        current = temp_node

        set_cover(temp_u, S, temp_s, current)
        current = current.parent

    return min_node.iter_path_reverse()


def map_subsets(U, S):
    mapped = [[] for i in range(len(U) + 1)]
    for i, set in enumerate(S, 1):
        for val in set:
            mapped[val].append(i)
    return mapped


def min_of_map(submap):
    submap_mins = [len(m) for m in submap]
    min = max(submap_mins)
    for m in submap_mins:
        if m == 0:
            continue
        else:
            min = m if m < min else min
    return submap[submap_mins.index(min)]


def check_subsets(S):
    for ind, s in enumerate(S):
        if True in [set(s).issubset(set(sets)) for sets in S[:ind] + S[ind + 1:]]:
            S[ind] = []
    return S


def format_cover(obj):
    return [node.set for node in obj if node.set != 0]


def readFile(file):
    s_loc = Path(file).absolute().parent
    f_loc = s_loc / "datasets" / file
    fileObj = open(f_loc, "r")
    data = fileObj.read().splitlines()
    fileObj.close()
    return data


while True:
    try:
        filename = input("file: ")
        data_arr = readFile(filename)
    except FileNotFoundError:
        print("doesn't exist")
    else:
        break
    
start = time.time()
universal = [x for x in range(1, int(data_arr[0]) + 1)]
subsets = [s.split() for s in data_arr[2:len(data_arr)]]
subsets = [[int(x) for x in s] for s in subsets]
submap = map_subsets(universal, check_subsets(subsets))
root = AnyNode(u=universal, set=0)
min_node = root

s_cover = format_cover(set_cover(universal, subsets, submap, root))

print("set cover: ", ["S" + str(s) for s in s_cover])
print(*[subsets[s - 1] for s in s_cover], sep="\n")
print("cover size: ", len(s_cover))
print("Runtime ------ %s seconds ------" % (time.time()-start))
