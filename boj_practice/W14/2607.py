import sys

n = int(sys.stdin.readline())
strlist = list(map(str, sys.stdin.readline().rstrip()))
strlist.sort()
cnt = 0
for i in range(n - 1):
    tmplist = list(map(str, sys.stdin.readline().rstrip()))
    tmplist.sort()
    ttmplist = tmplist[:]
    if strlist == tmplist:
        cnt += 1
        continue
    copyl = strlist[:]
    copyr = strlist[:]
    for i in range(len(copyl)):
        if copyl[i] in tmplist:
            tmplist.remove(copyl[i])
            copyl[i] = "0"
    for i in range(len(ttmplist)):
        if ttmplist[i] in copyr:
            copyr.remove(ttmplist[i])
            ttmplist[i] = "0"
    copycnt = 0
    for i in copyl:
        if i != "0":
            copycnt += 1
    ttmpcnt = 0
    for i in ttmplist:
        if i != "0":
            ttmpcnt += 1
    if copycnt * ttmpcnt == 1:
        cnt += 1
    elif copycnt * ttmpcnt == 0:
        if copycnt == 1:
            cnt += 1
        elif ttmpcnt == 1:
            cnt += 1

print(cnt)
