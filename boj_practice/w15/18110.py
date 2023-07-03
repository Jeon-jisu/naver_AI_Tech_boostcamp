import sys

n = int(sys.stdin.readline())
lst = [int(sys.stdin.readline()) for i in range(n)]
lst.sort()


def rfun(a):
    if a - int(a) >= 0.5:
        return int(a) + 1
    else:
        return int(a)


cut = rfun(n * 0.15)
nlst = lst[cut : n - cut]
if n == 0:
    print("0")
else:
    t = sum(nlst) / len(nlst)
    print(rfun(t))
