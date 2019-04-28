''' By HyeonGyu
BAEKJOON STAR / 백준 별찍기
https://www.acmicpc.net/workbook/view/20

Q7
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''

num = int(input())

for i in range(num*2-1) :
    if i < num : # 0~4
        for j in range(i, num-1) :
            print(" ", end = "")
        for k in range(i*2+1) :
            print("*", end = "")

    else : # 5 ~ 8
        for j in range(num-1, i) :
            print(" ", end = "")
        for k in range(((num*2-1)-i)*2-1) :
            print("*", end = "")
    print()

'''O(n)'''

for i in (list(range(1,num)) + list(range(num,0,-1))):
    print(' '*(num-i)+'*'*(i*2-1))

