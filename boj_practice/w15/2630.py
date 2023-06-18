# 23. 06. 18
import sys

n = int(sys.stdin.readline())
colormap = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
stack = [colormap]
blue, white = 0, 0


def check(eachmap):
    maplen = len(eachmap)
    eachmap = sum(eachmap, [])
    onecount = eachmap.count(1)
    zerocount = eachmap.count(0)
    if (onecount == maplen**2) or (zerocount == maplen**2):
        return 1
    else:
        return 0


def half(eachmap):
    lenmap = len(eachmap)

    y1 = eachmap[: lenmap // 2]
    y2 = eachmap[lenmap // 2 :]
    x1y1, x2y1, x1y2, x2y2 = [], [], [], []
    for i in y1:
        x1y1.append(i[: lenmap // 2])
        x2y1.append(i[lenmap // 2 :])
    for i in y2:
        x1y2.append(i[: lenmap // 2])
        x2y2.append(i[lenmap // 2 :])
    return x1y1, x2y1, x1y2, x2y2


while stack:
    curmap = stack.pop()
    if (check(curmap) == 1) or (len(curmap) == 1):
        if curmap[0][0] == 1:
            blue += 1
        else:
            white += 1
    else:
        t1, t2, t3, t4 = half(curmap)
        stack.append(t1)
        stack.append(t2)
        stack.append(t3)
        stack.append(t4)
print(white)
print(blue)
