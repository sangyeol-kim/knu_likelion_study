'''
input = 3

  *
 **
***
 **
  *
'''
num = int(input())

for i in range(1,2*num):
    print(' ' * abs(num-i)+'*' * (num - abs(num-i)))

