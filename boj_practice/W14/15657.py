import sys
from itertools import combinations_with_replacement

n, m = map(int, sys.stdin.readline().split())
numlist = list(set(map(int, sys.stdin.readline().split())))
numlist.sort()
alist = list()

for cwr in combinations_with_replacement(numlist, m):
    alist.append(cwr)
for i in alist:
    print(*i)
