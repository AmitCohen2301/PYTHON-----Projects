# ----- composeStr -----
def composeStr(L1, L2):
    return "".join([L1[i - 1] for i in L2])

# Checks for composeStr
L1 = ['a', 'h', 'f', 'e', 'y', 'u']
L2 = [1, 5, 3, 6, 2, 4]
assert(composeStr(L1, L2) == "ayfuhe")

# ----- composeLst -----
def composeLst(L):
    return [dict(L)[i] if i in list(dict(L).keys()) else -1000 for i in range(max(list(dict(L).keys())) + 1)]

# Checks for composeLst
lst2 = [(4, 9), (0, 2), (1, 4), (3, 2)]
assert(composeLst(lst2) == [2, 4, -1000, 2, 9])