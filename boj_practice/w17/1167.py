import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
xvisit = [[] for i in range(n)]
for i in range(n):
    tmplst = list(map(int, input().split()))
    hang = tmplst[0] - 1
    k = (len(tmplst) - 2) // 2
    for j in range(k):
        yeol = tmplst[j * 2 + 1] - 1
        dist = tmplst[j * 2 + 2]
        xvisit[hang].append([yeol, dist])


def dfs(x, sumdist):
    for a, b in xvisit[x]:
        if visited[a] == -1:
            visited[a] = b + sumdist
            dfs(a, b + sumdist)


visited = [-1] * (n + 1)
visited[1] = 0
dfs(1, 0)

start = visited.index(max(visited))
visited = [-1] * (n + 1)
visited[start] = 0
dfs(start, 0)

print(max(visited))
