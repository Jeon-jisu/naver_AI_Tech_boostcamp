# 2023.05.08(월) 
import re
t = int(input())
search = re.compile(r'(100+1+|01)+')
# 정규표현식을 compile 
for i in range(t):
    st = input()
    # fullmatch는 문자열 전체가 해당 패턴인지를 검사
    # match는 target이 해당 패턴으로 시작하는지를 검사
    if search.fullmatch(st):
        print("YES")
    else:
        print("NO")