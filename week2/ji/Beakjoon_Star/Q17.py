'''
   *
  * *
 *   *
*******
'''

n = int(input())
print(' ' * (n-1) + '*')

for i in range(1, n) :
    print(' ' * (n-1-i) + '*', end = '')
    if i == n-1 :
        print('*'* (2*i-1), end = '')
    else :
        print(' ' * (2*i-1), end = '')

    print('*')

'''
파이썬의 엄청난 기법!!!!!!! 

N=int(input())
for i in range(N):
    print(' '*(N-1-i)+'*'+'^+'[i<N-1]*(i+i-1)+'*'*(i>0))


print('AB'[True]) # 'B'
print('AB'[False]) # 'A'


print('*'*(True)) # 1번
print('*'*(False)) # 0번

'''