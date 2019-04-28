'''
*********
 *******
  *****
   ***
    *
   ***
  *****
 *******
*********
'''


num = int(input())

for i in list(range(num, 1, -1)) + list(range(1, num+1)) :
    print(' ' * (num - i) + '*' * (i*2-1))