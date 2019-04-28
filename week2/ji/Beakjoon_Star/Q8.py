'''
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
'''
num = int(input())

for i in list(range(1, num)) + list(range(num, 0, -1)) :
    print(('*' * i) + ' ' * (num-i)*2 + (('*') * i))