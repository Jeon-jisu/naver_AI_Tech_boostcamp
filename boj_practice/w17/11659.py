import sys

input = sys.stdin.readline
n, m = map(int, input().split())
numlist = [0] + list(map(int, input().split()))

ssum = 0
for idx in range(n + 1):
    ssum += numlist[idx]
    numlist[idx] = ssum
for k in range(m):
    i, j = map(int, input().split())
    print(numlist[j] - numlist[i - 1])
