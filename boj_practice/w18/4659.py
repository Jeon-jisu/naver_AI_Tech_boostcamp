import sys
input = sys.stdin.readline
from collections import deque
tmp = input()
script = ["is acceptable.","is not acceptable."]
vowels = ['a','e','i','o','u']
exx = ['e','o']
while tmp.rstrip() != "end":
    error = 0
    check = list(tmp)
    if check.count('a') + check.count('e')+ check.count('i')+ check.count('o')+ check.count('u')==0:
        error = 1
    else:
        line = deque()
        for i in range(len(check)):
            if len(line)>=3:
                ssumline = line[0]+line[1]+line[2]
                if (ssumline >=3) or (ssumline <= -3):
                    error = 1
                    break
            if check[i] in vowels:
                line.append(1)
            else:
                line.append(-1)
            if len(line)>=4:
                line.popleft()
    if error == 0:
        for i in range(len(check)-1):
            if check[i]==check[i+1]:
                if check[i] not in exx:
                    error = 1
    print(f'<{tmp.rstrip()}>', script[error])
    tmp = input()