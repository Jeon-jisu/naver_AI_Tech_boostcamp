t = int(input())
for i in range(t):
    new = []
    old = []
    n,m,k = map(int, input().split())
    cnt = 0
    newcnt = k
    dellist = []
    batlist = [[0 for t in range(n)] for i in range(m)]
    for j in range(k):
        x, y = map(int, input().split())
        # batlist[x][y] = 1
        new.append([x,y])
        old.append([x,y])
    for t in range(k):
        if [new[t][0]+1,new[t][1]] in new:
            if [new[t][0]+1,new[t][1]] not in dellist:
                newcnt-=1#오른쪽 한칸 검사
                dellist.append([new[t][0]+1,new[t][1]])
        if [new[t][0],new[t][1]+1] in new:
            if [new[t][0],new[t][1]+1] not in dellist:
                newcnt-=1#오른쪽 한칸 검사
                dellist.append([new[t][0],new[t][1]+1])
    print(newcnt)
