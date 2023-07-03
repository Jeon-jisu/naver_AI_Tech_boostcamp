hamlist = list()
cokelist = list()
for i in range(3):
    hamlist.append(int(input()))
for i in range(2):
    cokelist.append(int(input()))
print(min(hamlist) + min(cokelist) - 50)
