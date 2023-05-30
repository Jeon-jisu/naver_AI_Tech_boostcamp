n = int(input())
song = []
down = []
ans = []
for i in range(n):
    s, d = map(int, input().split())
    song.append(s)
    down.append(d)
sum = down[0]
delsum = 0
for i in range(n - 1):
    sum += down[i + 1]
    delsum += song[i]
    ans.append(sum - delsum)
if n == 1:
    print(down[0])
else:
    print(max(ans))
