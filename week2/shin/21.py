# 4
# * *
#  * *
# * *
#  * *
# * *
#  * *
# * *
#  * *

n = int(input())

if(n == 1):
    print("*")
else:
    for i in range(n):
        print('*' + ' *'*((n-1)//2))
        print(' *'+ ' *'*((n-2)//2))