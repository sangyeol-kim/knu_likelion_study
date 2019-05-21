'''
https://www.acmicpc.net/problem/9012

백준 step 11-3
'''

case = int(input())
result = [] # 결과

for _ in range(case) :
    check = True # 올바른 괄호식인지 확인
    p = input() # 입력괄호
    stack = [] #  괄호가 올바른지 검사를 위한 stack

    for ch in p : # 입력한 괄호식 앞부터 하나씩 가져오기
        if ch == '(' : # push
            stack.append(ch)
        else : # ch == ')' # pop 후 비교
            if not stack : # stack이 비어있으면(짝 맞춰서 버릴께 없으면)
                check = False
                break
            else:
                stack.pop() # 짝 맞춰서 버림
                continue

    if check and not stack: # 옳바른 괄호이며 stack도 비어있으면(마지막에 '((('입력시)
        result.append('YES')
    else : # 올바른 괄호가 아니거나 stack이 비어있지 않으면
        result.append('NO')

for r in result:
    print(r)




