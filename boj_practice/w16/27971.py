import sys

n, m, a, b = map(int, sys.stdin.readline().split())
dp = [0 for i in range(n + 1)]
for i in range(m):
    start, end = map(int, sys.stdin.readline().split())
    for j in range(start, end + 1):
        dp[j] = -1
if dp[n] == -1:
    ans = -1
else:
    ans = 0
for i in range(1, n + 1):
    tmpa, tmpb, tmp = n + 1, n + 1, -1
    if (i - a >= 0) and (dp[i - a] != -1):
        if ((dp[i - a] != 0) and (dp[i - a] != -1)) or (i - a == 0):
            tmpa = dp[i - a] + 1
    elif (i - b >= 0) and (dp[i - b] != -1):
        if ((dp[i - b] != 0) and (dp[i - b] != -1)) or (i - b == 0):
            tmpb = dp[i - b] + 1
    elif (dp[i - a] == -1) and (dp[i - b] == -1):
        tmp = -1
    else:
        tmp = 0

    if dp[i] == -1:
        continue
    elif tmp == -1:
        if (tmpa == n + 1) and (tmpb == n + 1):
            dp[i] = -1
        else:
            dp[i] = min(tmpa, tmpb)
    else:
        dp[i] = 0

if ans == -1:
    print("-1")
elif dp[n] == 0:
    print("-1")
else:
    print(dp[n])
