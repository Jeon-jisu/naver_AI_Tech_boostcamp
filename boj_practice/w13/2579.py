situation = [0]
n = int(input())
for i in range(n):
    situation.append(int(input()))
# situation의 개수는 n+1개
dp = [0 for i in range(303)]
if n == 1:
    print(situation[1])
else:
    dp[1] = situation[1]
    dp[2] = situation[2] + dp[1]
    if n >= 3:
        for i in range(3, n + 1):
            dp[i] = max(dp[i - 2] + situation[i], dp[i - 3] + situation[i - 1] + situation[i])

    print(dp[n])
