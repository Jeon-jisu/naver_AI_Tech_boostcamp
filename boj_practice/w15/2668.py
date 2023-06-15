import itertools

n = int(input())
graph = [int(input()) for i in range(n)]
graph = [0] + graph
twgraph = [[] for j in graph]
ad = []


def dfs(cur, visited_graph):  # visited graph 만들기,
    vigr = visited_graph
    vigr[cur] = True
    if vigr[graph[cur]] == True:
        ad.append(vigr)
        return vigr
    else:
        if graph[cur] != cur:
            dfs(graph[cur], vigr)
        else:
            # print(vigr)
            ad.append(vigr)
            return vigr


ttmp = []
for i in range(1, n + 1):
    tmp = []
    visited = [False for i in range(n + 1)]
    dfs(i, visited)

newad = []
cnt = 0
anslist = []
for i in ad:
    tmp = []
    for idx, j in enumerate(i):
        if j == True:
            tmp.append(idx)
    if len(tmp) == 1:
        anslist.append(tmp[0])
        cnt += 1
    newad.append(tmp)
newadst = set(list(map(tuple, newad)))
numl = [0]
update = []
for i in newadst:
    if newad.count(list(i)) > max(numl):
        update = list(i)
    numl.append(newad.count(list(i)))

dupdate = []
ccnt = 0
for i in newadst:
    if newad.count(list(i)) >= 2:
        dupdate.append(list(i))
        ccnt += len(list(i))

if max(numl) == 1:
    print(cnt)
    for i in anslist:
        print(i)
else:
    print(ccnt + cnt)
    a = sorted(anslist + list(itertools.chain(*dupdate)))
    for i in a:
        print(i)
