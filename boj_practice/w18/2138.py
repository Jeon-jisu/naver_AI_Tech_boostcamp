import sys 
input = sys.stdin.readline
n = int(input())
visited = [0 for i in range(n)]
state = [int(i) for i in list(input().rstrip())]
want = [int(i) for i in list(input().rstrip())]
def switch(i,light):
    if (i == 0) :
        light[i] = (light[i]+1)%2
        light[i+1] = (light[i+1]+1)%2
    elif (i == n-1):
        light[i] = (light[i]+1)%2
        light[i-1] = (light[i-1]+1)%2
    else:
        light[i] = (light[i]+1)%2
        light[i-1] = (light[i-1]+1)%2
        light[i+1] = (light[i+1]+1)%2
    return light
cnt = 0
cur = 0
while (cur < n):
    if (state[cur]!=want[cur]) and (visited[cur]==0):
        state = switch(cur,state)
        visited[cur]=1
        print(cur)
        cnt += 1
        cur = 0
    else:
        cur+=1
    if state == want:
        break
print(cnt,state)