# 23.06.08
import sys

n = int(sys.stdin.readline())
dp = [1 for _ in range(10)]

for j in range(n - 1):
    newdp = list()
    esum = 0
    for i in range(10):
        esum += dp[i]
        newdp.append(esum)
    dp = newdp[:]
print(sum(dp) % 10007)
