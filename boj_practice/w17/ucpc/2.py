import sys

input = sys.stdin.readline
n, k = map(int, input().split())
numlst = list(map(int, input().split()))
originnum = numlst[:]
copynum = list()
mmin = numlst[0]
maxx = numlst[0]
ans = 0
for i in range(1, len(numlst)):
    if maxx > numlst[i]:
        ans = max(maxx - numlst[i] - k, ans)
        copynum.append(ans)
        print("max", ans)
    elif mmin < numlst[i]:
        ans = min(numlst[i] - mmin - k, ans)
        copynum.append(ans)
        print("min", ans)
    maxx = max(maxx - k, numlst[i])
    mmin = min(mmin - k, numlst[i])
print("fianl", copynum)
