''' By HyeonGyu
BAEKJOON STAR / 백준 별찍기
https://www.acmicpc.net/workbook/view/20

Q1
*
**
***
****
*****
'''
num = int(input())

for i in range(1, num+1) :
    for j in range(i) :
        print("*", end = "")
    print()