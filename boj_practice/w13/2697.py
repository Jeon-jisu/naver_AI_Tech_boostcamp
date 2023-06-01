n = int(input())


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)


for i in range(n):
    keey = 0
    num = list(map(int, input()))
    last = len(num) - 1
    front = len(num) - 2
    if len(num) - 1 <= 0:
        keey = 1
    if len(num) == 2:
        if num[0] >= num[1]:
            keey = 1
    while (num[last] <= num[front]) and (keey == 0):
        front -= 1
        last -= 1
        if front == 0:
            keey = 1
            break
    if keey == 0:
        static = num[:front]
        for i in range(len(static)):
            static[i] = str(static[i])
        tmpprint = "".join(static)
        tmp = num[front]
        focus = num[front:]
        credent = quick_sort(focus)
        credentset = set(credent)
        credentlist = list(credentset)
        nextnum = credentlist[credentlist.index(tmp) + 1]
        nextnumidx = focus.index(nextnum) + len(static)  # nextnum은 무조건 있는 숫자. 아까 tmp하고 바꿔야 한다.
        num[front] = nextnum
        num[nextnumidx] = tmp
        sortlist = num[front + 1 :]
        sortedlist = quick_sort(sortlist)  # 최소 수 찾기
        blist = []
        for i in range(len(sortedlist)):
            blist.append(str(sortedlist[i]))  # 바꾼 수 찾기
        print(tmpprint + str(nextnum) + "".join(blist))
    elif keey == 1:
        print("BIGGEST")
