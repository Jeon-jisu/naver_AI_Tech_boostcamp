import itertools

outlist = list()
n, m = map(int, input().split())
numlist = list(map(int, input().split()))
nPr = itertools.permutations(numlist, m)
for i in sorted(set(list(nPr))):
    # if list(i) not in outlist:
    outlist.append(list(i))
for i in outlist:
    print(*i)
