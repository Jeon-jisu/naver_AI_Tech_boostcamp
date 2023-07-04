import sys

input = sys.stdin.readline
n = int(input())
numlst = list()
nolst = list()
for i in range(n):
    numlst.append(int(input()))
numlst.sort()
for i in range(n):
    cnt = 0
    for j in range(numlst[i], numlst[i] + 5):
        if j not in numlst:
            cnt += 1
    nolst.append(cnt)
print(min(nolst))
