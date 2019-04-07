''' By HyeonGyu
BAEKJOON STAR / 백준 별찍기
https://www.acmicpc.net/workbook/view/20

Q6
*********
 *******
  *****
   ***
    *
'''

num = int(input())

for i in range(num, 0, -1) :
    for k in range(i, num) :
        print(" ", end = "")

    for j in range(0, i*2-1) :
        print("*", end ="")
    print()
