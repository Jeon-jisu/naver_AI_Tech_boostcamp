import sys  # sys.stdin.readline()

n, m = map(int, sys.stdin.readline().split())
tmp = []
for i in range(n):
    origin = list(map(int, sys.stdin.readline().split()))
    sum = 0
    newtmp = [0]
    for t in origin:
        sum += t
        newtmp.append(sum)
    tmp.append(newtmp)
for j in range(m):
    y1, x1, y2, x2 = map(int, sys.stdin.readline().split())
    ans = 0
    if x2 != x1:
        for k in range(y1 - 1, y2):
            ans += tmp[k][x2] - tmp[k][x1 - 1]
    else:
        for k in range(y1 - 1, y2):
            ans += tmp[k][x2] - tmp[k][x1 - 1]
    print(ans)
