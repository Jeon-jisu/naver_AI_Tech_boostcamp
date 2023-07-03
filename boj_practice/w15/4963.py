import sys
w,h = map(int,sys.stdin.readline().split())
while (w!=0) and (h!=0):
    #search map을 만듭니다.  
    #search map을 기준으로 대각선, 위, 왼쪽을 검사합니다. 
    #하나만 겹친다면 