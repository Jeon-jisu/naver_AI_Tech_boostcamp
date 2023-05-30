n = int(input())
lst = list(map(int, input().split()))
k = int(input())
cnt = 0
intsum = lst[0]
b = 0
for a in range(n):
    while (intsum <= k) and (b < n - 1):
        b += 1
        intsum += lst[b]
    if intsum <= k:
        break
    else:
        cnt += n - b
        intsum -= lst[a]

print(cnt)
