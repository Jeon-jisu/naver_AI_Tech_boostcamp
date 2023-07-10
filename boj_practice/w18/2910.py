import sys
from collections import Counter
input = sys.stdin.readline
n, c = map(int, input().split())
numlst = list(map(int,input().split()))
counter = Counter(numlst)
counter = sorted(counter.items(), key = lambda item: item[1], reverse = True)
keylst = list()
while counter:
    ttmp = counter[0]
    for i in range(ttmp[1]):
        keylst.append(ttmp[0])
    counter.remove(ttmp)
print(*keylst)