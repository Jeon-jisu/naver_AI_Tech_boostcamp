import sys
input = sys.stdin.readline
n,k = map(int,input().split())
A = list(map(int, input().split()))
anslst = [i for i in range(1,n+1)]
error = 0
A.sort()
for i in anslst:
    if i in A:
        A.remove(i)
    else:
        error = 1
    if error == 1:
        for m in range(1, 50):
            for a in A:
                if i == a+m*k:
                    A.remove(a)
                    error = 0
                    break
            if error == 0:
                break
    if error == 1:
        break
if error == 1:
    print("0")
else:
    print("1")