n = int(input())
song = []
down = []
songsum = []
for i in range(n):
    s, d = map(int, input().split())
    if i == 0:
        down.append(d)
        songsum.append(s)
        song.append(s)
    else:
        down.append(down[i - 1] + d)
        songsum.append(songsum[i - 1] + i)
        song.append(s)
start = down[0]
state = down[0]
last = 0
print(down)
print(song)
# for i in range(n):
