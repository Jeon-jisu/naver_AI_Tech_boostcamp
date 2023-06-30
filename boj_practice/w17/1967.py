import sys
from collections import deque

sys.setrecursionlimit(10**9)

input = sys.stdin.readline
n = int(input())
xvisit = [[] for i in range(n + 1)]

for i in range(n - 1):
    tmplst = list(map(int, input().split()))
    hang = tmplst[0] - 1
    yeol = tmplst[1] - 1
    dist = tmplst[2]
    xvisit[hang].append([yeol, dist])
    xvisit[yeol].append([hang, dist])


def dfs(x, sumdist):
    for a, b in xvisit[x]:
        if visited[a] == -1:
            visited[a] = b + sumdist
            dfs(a, b + sumdist)


visited = [-1] * (n)
visited[0] = 0
dfs(0, 0)
start = visited.index(max(visited))

visited = [-1] * (n)
visited[start] = 0
dfs(start, 0)

print(max(visited))
