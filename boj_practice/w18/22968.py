import sys
input = sys.stdin.readline
n = int(input())
keylist = list()
for i in range(n):
    keylist.append(int(input()))
dp = [0 for i in range(10000)]
dp[0]=1
dp[1]=2
for i in range(len(dp)-2):
    dp[i+2]=dp[i]+dp[i+1]
summ = 0
for i in range(len(dp)):
    summ += dp[i]
    dp[i]=summ
    
for key in keylist:
    for j in range(len(dp)):
        if dp[j]>=key:
            print(j+1)
            break