t = int(input())
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def BFS(x,y):
    queue = [(x,y)]
    nong[x][y] = 0 
    while queue:
        x,y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny <0 or ny >=n:
                continue
            if nong[nx][ny] == 1:
                queue.append((nx,ny))
                nong[nx][ny] = 0
for i in range(t):
    m,n,k = map(int,input().split())
    nong = [[0 for a in range(n)]for b in range(m)]
    cnt = 0
    for ek in range(k):
        ix,iy = map(int,input().split())
        nong[ix][iy] = 1
    for a in range(m):
        for b in range(n):
            if nong[a][b] == 1:
                BFS(a,b)
                cnt+=1
    print(cnt)
