#    *
#   * *
#  *   *
# *******

n = int(input())

if(n == 1):
    print("*")
else:
    line = [' *', '***']
    for i in range(2, n):
        for j in range(len(line)-1):
            line[j] = ' ' + line[j]
        line.insert(-1, ' *' + ' '*(2*(i-1)-1) + '*')
        line[-1] += '**'

    print('\n'.join(line))