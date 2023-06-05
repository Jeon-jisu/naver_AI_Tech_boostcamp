# 23. 06. 05
n = int(input())
order = list()
for i in range(n):
    order.append(int(input()))
cnt = 0
sortorder = sorted(order)
nonorderkey = n - 1
orderkey = n - 1
for j in range(n):
    compare = order[nonorderkey]
    standard = sortorder[orderkey]
    if compare < standard:
        cnt += 1
        nonorderkey -= 1
    else:
        orderkey -= 1
        nonorderkey -= 1
print(cnt)
