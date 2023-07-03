# 23. 06. 20
import sys

n = int(sys.stdin.readline())
colormap = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
stack = [colormap]
blue, white, green = 0, 0, 0


def check(eachmap):
    maplen = len(eachmap)
    eachmap = sum(eachmap, [])
    onecount = eachmap.count(1)
    zerocount = eachmap.count(0)
    minuscount = eachmap.count(-1)
    if (onecount == maplen**2) or (zerocount == maplen**2) or (minuscount == maplen**2):
        return 1
    else:
        return 0


def triple(eachmap):
    lenmap = len(eachmap)
    # print(eachmap)
    y1 = eachmap[: lenmap // 3]
    y2 = eachmap[lenmap // 3 : lenmap * 2 // 3]
    y3 = eachmap[lenmap * 2 // 3 :]
    x1y1, x2y1, x3y1, x1y2, x2y2, x3y2, x1y3, x2y3, x3y3 = [], [], [], [], [], [], [], [], []

    for i in y1:
        x1y1.append(i[: lenmap // 3])
        x2y1.append(i[lenmap // 3 : lenmap * 2 // 3])
        x3y1.append(i[2 * lenmap // 3 :])
    for i in y2:
        x1y2.append(i[: lenmap // 3])
        x2y2.append(i[lenmap // 3 : lenmap * 2 // 3])
        x3y2.append(i[2 * lenmap // 3 :])
    for i in y3:
        x1y3.append(i[: lenmap // 3])
        x2y3.append(i[lenmap // 3 : lenmap * 2 // 3])
        x3y3.append(i[2 * lenmap // 3 :])
    return x1y1, x2y1, x3y1, x1y2, x2y2, x3y2, x1y3, x2y3, x3y3


while stack:
    curmap = stack.pop()
    if (check(curmap) == 1) or (len(curmap) == 1):
        if curmap[0][0] == 1:
            blue += 1
        elif curmap[0][0] == 0:
            white += 1
        else:
            green += 1
    else:
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = triple(curmap)
        stack.append(t1)
        stack.append(t2)
        stack.append(t3)
        stack.append(t4)
        stack.append(t5)
        stack.append(t6)
        stack.append(t7)
        stack.append(t8)
        stack.append(t9)


print(green)
print(white)
print(blue)
