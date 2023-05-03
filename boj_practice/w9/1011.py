# 2023.05.03(수) 
t = int(input()) 
for i in range(t): 
    x,y = map(int, input().split()) 
    a = y-x # a는 y와 x의 차이값 
    n = int(a**(1/2)) # n은 루트 a 
    # a가 n의 제곱보다 크거나 같고 (n+1)의 제곱보다 작은 상태, a가 n(n+1)보다 작거나 같은지 큰지를 판별해줘야 한다. 
    if a == n**2: #a가 n의 제곱이라면 
        print(n*2-1) #2*n-1 출력 
    else: #a가 n의 제곱보다 크고, 
        if a<=(n*(n+1)): #a가 n(n+1)보다 작거나 같다면 
            print(n*2) #2*n 출력 
        else: #a가 n(n+1)보다 크다면 
            print(n*2+1) #2*n+1 출력