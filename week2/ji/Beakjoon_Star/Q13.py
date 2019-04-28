'''
input = 3
*
**
***
**
*
'''

n = int(input())

for i in range(1, n*2) :
    print('*' * (n - abs(n-i)))