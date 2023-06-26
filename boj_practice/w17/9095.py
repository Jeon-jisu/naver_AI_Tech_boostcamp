import sys

n = int(sys.stdin.readline())
dp = [0 for i in range(4)]
dp[1] = 1
dp[2] = 2
dp[3] = 4
num = []
for i in range(n):
    num.append(int(sys.stdin.readline()))
if max(num) + 1 < 4:
    for i in range(n):
        print(dp[num[i]])
else:
    for j in range(4, max(num) + 1):
        dp.append(dp[j - 1] + dp[j - 2] + dp[j - 3])
    for i in range(n):
        print(dp[num[i]])
