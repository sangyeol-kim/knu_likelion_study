'''
5
    *
   * *
  * * *
 * * * *
* * * * *

'''

n = int(input())

print(' ' * (n-1) + '*')

for i in range(1, n) :
    print(' ' * (n-1-i), end = '')
    print('* ' * i, end = '')
    print('*')

'''
n=int(input())
for i in range(1,n+1):
    print(' '*(n-i) + '* ' * i)
'''