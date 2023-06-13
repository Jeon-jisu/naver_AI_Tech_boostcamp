# 06 12 월
from itertools import combinations
n, m = map(int, input().split())
tmp = list()
for i in range(n):
    tmp.append(list(map(int, input().split())))
# print(tmp)
chickenlist = list()
homelist = list()

for i in range(n):
    for j in range(n):
        if tmp[i][j] == 2:
            chickenlist.append([i, j])
        elif tmp[i][j] == 1:
            homelist.append([i, j])
print(chickenlist)
homekeylist = []
for home in homelist:
    i, j = home
    mind = abs(chickenlist[0][0] - i) + abs(chickenlist[0][1] - j)
    homekey = list()
    homekey = chickenlist[0][:2]
    # print("homekey0", homekey)
    for chicken in chickenlist:
        chicken = chicken[:2]
        # print("home", home, "chicken", chicken, "mind :", mind)
        if abs(chicken[0] - i) + abs(chicken[1] - j) < mind:
            mind = min(abs(chicken[0] - i) + abs(chicken[1] - j), mind)
            homekey = 0
            homekey = chicken
            # print(homekey)
    homekey.append(mind)  # [1, 0, mind]
    # print("homekey2", homekey)
    homekeylist.append(homekey) # [[1, 0, mind], [1, 2, mind]]
# # print("homekeylist", homekeylist)
# dlist = [0 for i in range(len(chickenlist))]
# survivenum = [0 for i in range(len(chickenlist))]
# for idx, chicken in enumerate(chickenlist):
#     for t in homekeylist:
#         if t[:2] == chicken:
#             dlist[idx] += t[2]
#             survivenum[idx] += 1
# dlist.sort(reverse=True)
# print(sum(dlist[:m]))
# # print(dlist)
total_dists = []
for selected in combinations(range(len(chickenlist)), m):
    total_dists.append(sum([min([dists[i][j] for j in selected]) for i in range(len(houses))]))

print(min(total_dists))