'''
https://www.acmicpc.net/problem/1929

백준 Step 10-3
'''
M, N = list(map(int, input().split()))


prime = [] # 소수를 저장할 배열

# 1은 소수가 아니므로 2부터 검색
for num in range(2,N+1) :
    IsPrime = True  # 소수인지 판별

    for p in prime :
        if num % p == 0 : # 소수의 곱으로 표현가능
            IsPrime = False
            break # (한번이라도 표현가능하다면 종료)

    if IsPrime : # 모든 소수의 곱으로 표현이 불가하다면 소수
        if num >= M : # M이상인 소수만 출력
            print(num)
        prime.append(num) # 소수추가