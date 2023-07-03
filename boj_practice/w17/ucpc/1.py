import sys

input = sys.stdin.readline
summ = 0
for i in range(10):
    n = int(input())
    summ += n
if summ % 4 == 0:
    print("N")
elif summ % 4 == 1:
    print("E")
elif summ % 4 == 2:
    print("S")
else:
    print("W")
