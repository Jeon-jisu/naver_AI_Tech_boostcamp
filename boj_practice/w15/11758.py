# 06 13
coor = list()
for i in range(3):
    x, y = map(int, input().split())
    coor.append([x, y])
key = (coor[1][0] - coor[0][0]) * (coor[2][1] - coor[1][1]) - (coor[2][0] - coor[1][0]) * (coor[1][1] - coor[0][1])
if key == 0:
    print("0")
elif key > 0:
    print("1")
else:
    print("-1")
