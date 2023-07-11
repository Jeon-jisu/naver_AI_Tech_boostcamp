import sys
input = sys.stdin.readline
n = int(input())
card = list(map(int,input().split()))
jung = 0
for i in range(n//2):
    jung+=card[2*i]
originjung = jung
best1card = card[:] #밑장을 내가 갖는 경우
best1 = list()
best2card = card[:]
best2 = list()
for i in range(n//2):
    idx = ((n//2)-1-i)
    best1card[idx]=jung-card[-2-2*i]+card[-1-2*i]
    best1.append(best1card[idx])
    jung = best1card[idx]
best1 = list(reversed(best1))


for i in range(n//2 -1):
    idx = ((n//2)-i)
    if len(best2)==0:
        best2.append(originjung)
    else:
        originjung = best2[-1]
        best2card[idx]=originjung-card[-2*i]+card[-1-2*i]
        # print("출력",originjung,card[-2-2*(i-1)],card[-1-2*i] )
        # originjung = best2card[idx]
        best2.append(best2card[idx])
if n>=3:
    a = max(best1)
    b = max(best2)
    best2 = list(reversed(best2))
    # print(best1,best2)
    print(max(a,b))
else:
    print(max(card))