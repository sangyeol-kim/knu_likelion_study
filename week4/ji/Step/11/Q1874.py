'''
https://www.acmicpc.net/problem/1874

백준 step 11-2
'''

'''
한 사이클
{
다음에 오는 수열 >= 지금 N값 = push, while(수열 == N) / pop
다음에 오는 수열 < 지금 N값 =  pop, if(pop==수열)? / fasle면 None
n++
}

'''
seq = []
stack =[]
method = [] # 어떻게 push pop할지 > 마지막에 print

n = int(input())
for _ in range(n): # 수열입력
    seq.append(int(input()))

i = 1
index = 0
check = True
# n이 넘으면 check를 계속pop
# 1~n원소(i)를 pop / push 결정
#
while i <= n :

    if i <= seq[index] : # push
        stack.append(i)
        method.append('+')
        i+= 1
        continue

    if stack.pop() == seq[index] : #pop
        method.append('-')
        index += 1
    else:
        check = False
        break

if check :
    while stack != [] and index <= n:
        if stack.pop() == seq[index] :
            method.append('-')
            index += 1
        else:
            check = False
            break

if check == False :
    print('NO')
else :
    for m in method :
        print(m)