import sys

input = sys.stdin.readline
n, m = map(int, input().split())
numlst = [[i] for i in range(n + 1)]
visited = [0 for i in range(n + 1)]
for i in range(m):
    d1, d2 = map(int, input().split())
    if d2 not in numlst[d1]:
        numlst[d1].append(d2)
    if d1 not in numlst[d2]:
        numlst[d2].append(d1)
cnt = 0
for i in range(1, n + 1):
    if visited[i] == 1:
        continue  # 방문했으면 다음 걸로..
    visited[i] = 1
    stack = numlst[i]  # stack = [1,2,5]
    # print(stack)
    key = 1
    while stack:
        key = 0
        top = stack[-1]
        stack.pop()
        if visited[top] == 1:
            continue
        else:
            stack = list(set(stack + numlst[top]))
            visited[top] = 1
    if key == 0:
        cnt += 1
print(cnt)
