''' By HyeonGyu
BAEKJOON STAR / 백준 별찍기
https://www.acmicpc.net/workbook/view/20

Q2
    *
   **
  ***
 ****
*****
'''
num = int(input())

for i in range(1,num+1) :
    for k in range(i, num) :
        print(" ", end="")
    for j in range(i) :
        print("*", end = "")
    print()

'''0(n)'''
for i in range(1, num+1) :
    print(' ' * (num-i), end = '')
    print('*' * i)