import sys

input = sys.stdin.readline
N, r, c = map(int, input().split())
r += 1
c += 1
cnt = 0
n = N
cccc = 0
while (r > 1) or (c > 1):
    if r > 2 ** (n - 1):
        next_r = 1
    else:
        next_r = 0

    if c > 2 ** (n - 1):
        next_c = 1
    else:
        next_c = 0
    summ = next_r * 2 + next_c
    cnt += summ * 2 ** (2 * n - 2)

    if next_r == 1:
        r = r - (2 ** (n - 1))
    if next_c == 1:
        c = c - (2 ** (n - 1))
    cccc += 1
    n = n - 1
print(cnt)
