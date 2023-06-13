import sys

n = int(sys.stdin.readline())
lines = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
lines.sort()
keymap = [line[1] for line in lines]
dp = [1 for _ in lines]
for i in range(1, n):
    tmp = []
    for j in range(i):
        if keymap[i] > keymap[j]:
            tmp.append(dp[j])
    if len(tmp) != 0:
        dp[i] = max(tmp) + 1
    else:
        dp[i] = 1
print(n - max(dp))
