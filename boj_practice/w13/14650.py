# 0602
n = int(input())
if n == 1:
    print("0")
else:
    print((3 ** (n - 2) * 2) % ((10**9 + 9)))
