# 2023.05.09(화)
n = int(input())
numlist = input().split()
for i in numlist:
    i = int(i)
anslist = []
for i in range(n):
    upleftangle , uprightangle = 0 ,0
    leftangle , rightangle = 0 ,0
    for j in range(0,i,-1):
        if numlist[i]-numlist[j]<0: #옆에 건물이 더 크다면
            val = (numlist[j]-numlist[i])/(i-j)
            if upleftangle < val: #가장 큰 각도를 갱신하자
                upleftangle = val
        else:
            val = (i-j)/(numlist[i]-numlist[j])
            if leftangle < val: 
                leftangle = val
    for t in range(i+1,n):
        if numlist[i]-numlist[t]<0: #옆에 건물이 더 크다면
            val = (numlist[t]-numlist[i])/(t-i)
            if uprightangle < val: #가장 큰 각도를 갱신하자
                uprightangle = val
        else:
            val = (t-i)/(numlist[i]-numlist[t])
            if rightangle < val: 
                rightangle = val
    anslist.append([upleftangle , uprightangle,leftangle , rightangle])
print(anslist)