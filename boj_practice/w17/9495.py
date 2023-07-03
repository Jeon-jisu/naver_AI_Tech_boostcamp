import sys

input = sys.stdin.readline
n = int(input())
dp = [0 for i in range(n)]
for i in range(n):
    k = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    nlst = []
    if k == 1:
        print(max(a[0], b[0]))
    else:
        a[1] = b[0] + a[1]
        b[1] = a[0] + b[1]
        for i in range(2, k):
            a[i] = max(a[i] + b[i - 1], a[i] + b[i - 2])
            b[i] = max(b[i] + a[i - 1], b[i] + a[i - 2])
        nlst.append(a[-1])
        nlst.append(a[-2])
        nlst.append(b[-1])
        nlst.append(b[-2])
        print(max(nlst))
