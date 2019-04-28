# * * *
#  * * *
# * * *

n = int(input())

for i in range(n):
    line = ' ' + '* '*n
    print(line[(i+1)%2:-1])