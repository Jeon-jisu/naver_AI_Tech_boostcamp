import sys
from collections import Counter

wlen, strlen = map(int, sys.stdin.readline().split())
wlst = list(sys.stdin.readline().rstrip())
slist = list(sys.stdin.readline().rstrip())


def search(wsetlist, curslist):
    if curslist == wsetlist:
        return 1
    else:
        return 0


wsetlist = Counter(wlst)
cnt = 0
start = 0
end = start + wlen
tmpdict = Counter(slist[start:end])
while end <= strlen:
    a = search(wsetlist, tmpdict)
    if a == 1:
        cnt += 1
    if end == strlen:
        break
    tmpdict[slist[start]] -= 1
    if tmpdict[slist[start]] == 0:
        tmpdict.pop(slist[start])
    tmpdict[slist[end]] += 1
    start += 1
    end += 1
print(cnt)
