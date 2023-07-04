n = int(input())
k = list(map(int, input().split()))
dp = [1 for i in range(1001)]

for i in range(n):
    for j in range(i):