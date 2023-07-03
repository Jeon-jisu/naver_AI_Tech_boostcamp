import sys

n = int(sys.stdin.readline().rstrip())
lists = set()
for i in range(n):
    a = list(map(str, sys.stdin.readline().rstrip().split()))
    if len(a) != 1:
        say, num = a[0], a[1]
        num = int(num)
    elif a[0] == "all":
        say = "all"
    elif a[0] == "empty":
        say = "empty"

    if say == "add":
        lists.add(num)
    elif say == "check":
        if num not in lists:
            print("0")
        else:
            print("1")
    elif say == "remove":
        lists.discard(num)
    elif say == "toggle":
        if num in lists:
            lists.discard(num)
        else:
            lists.add(num)
    elif say == "all":
        lists = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
    elif say == "empty":
        lists = set()
