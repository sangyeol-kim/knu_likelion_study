#    *
#   * *
#  * * *
# * * * *
n = int(input())
prev = ' '*(n-1) + '*'
print(prev)
for i in range(1, n):
    line = prev[1:] + ' *'
    print(line)
    prev = line
