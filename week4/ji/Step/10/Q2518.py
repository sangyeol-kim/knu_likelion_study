'''
백준 Step 10-2
https://www.acmicpc.net/problem/2581
'''
M = int(input())
N = int(input())

#1. 1~N까지 소수찾기 / N~M 사이의 소수 저장 = NMprime

prime = [] # 1~N사이의 소수를 저장할 배열
NMprime = [] # M~N사이의 소수

# 1은 소수가 아니므로 2부터 검색
for num in range(2, N+1) :
    IsPrime = True  # 소수인지 판별

    for p in prime :
        if num % p == 0 : # 소수의 곱으로 표현가능
            IsPrime = False
            break # (한번이라도 표현가능하다면 종료)

    if IsPrime : # 모든 소수의 곱으로 표현이 불가하다면 소수
        prime.append(num) # 소수추가
        if num >= M : # 소수추가시 M보다 클경우
            NMprime.append(num) # N~M사이의 소수

#2. NMprime처리
if not NMprime: # N M 사이에 소수가 없는경우
    print(-1)
else:
    print(sum(NMprime)) # 소수들의 합
    print(NMprime[0]) # 가장 작은 소수

''' 개쩌는 코드
*s,=range(10001)
for i in s[2:]:
 if s[i]:s[2*i::i]=[0]*(10000//i-1)
P={*s[int(input()):int(input())+1]}-{0,1}
print(f"{sum(P)}\n{min(P)}"if P else-1)
'''