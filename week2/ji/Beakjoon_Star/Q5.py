''' By HyeonGyu
BAEKJOON STAR / 백준 별찍기
https://www.acmicpc.net/workbook/view/20

Q5
    *
   ***
  *****
 *******
*********
'''

num = int(input())

for i in range(num) :

    for j in  range(i, num-1) :
        print(" ", end = "")

    for k in range(i*2+1) :
        print("*", end = "")

    print()

''' O(n)'''
for i in range(1, num+1) :
    print(" " * (num -i), end = '')
    print("*" * (2*i-1))