# 23. 06. 07
n = int(input())
numlist = list(map(int,input().split()))
dp = [0 for i in range(n)]
dp[0] = 1
for i in range(1,n):
    tmp = []
    for j in range(i):
        if (numlist[i]<numlist[j]):
            tmp.append(dp[j])
    if len(tmp)!=0:
        dp[i]= max(tmp)+1
    else:
        dp[i]=1
print(max(dp))