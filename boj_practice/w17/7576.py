import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())
farm = [list(map(int, input().split())) for i in range(n)]
visited = [[0 for j in range(m)] for i in range(n)]
cnt_zero = sum(farm, []).count(0)
stack = deque()
for i in range(n):
    for j in range(m):
        if farm[i][j] == 1:
            stack.append([i, j])
        if farm[i][j] == -1:
            visited[i][j] = 1
change = 1
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

cccc = 0
tmpvisited = [[0 for j in range(m)] for i in range(n)]
while cnt_zero != 0:
    tmp = deque()

    while stack:
        top = stack.pop()
        visited[top[0]][top[1]] = 1
        # tmpvisited[ndot[0]][ndot[1]] = 1

        for i in range(4):
            ndot = [top[0] + dy[i], top[1] + dx[i]]
            if (ndot[0] >= n) or (ndot[0] < 0):
                continue
            if (ndot[1] >= m) or (ndot[1] < 0):
                continue
            if (
                (farm[ndot[0]][ndot[1]] == 0)
                and (tmpvisited[ndot[0]][ndot[1]] == 0)
                and (visited[ndot[0]][ndot[1]] == 0)
            ):
                tmp.append([ndot[0], ndot[1]])
                tmpvisited[ndot[0]][ndot[1]] = 1

    cccc += 1
    # print("stack", stack)
    # print(tmpvisited)
    stack.extend(tmp)
    # print("tmp", tmp, "cnt_zero", cnt_zero)
    cnt_zero -= len(tmp)
    if len(tmp) == 0:
        cccc = -1
        break
if cccc == -1:
    print("-1")
else:
    print(cccc)
