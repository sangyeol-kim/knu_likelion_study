# *********
# *       *
# * ***** *
# * *   * *
# * * * * *
# * *   * *
# * ***** *
# *       *
# *********

n  = int(input())
if(n == 1):
    print("*")
else :
    line = ["*****", '*   *', '* * *', '*   *', '*****']
    for i in range(2, n):
        for j in range(len(line)):
            line[j] = '* ' + line[j] + ' *'
        line.append('*' + ' '*(len(line[0])-2) + '*')
        line.append('*'*len(line[0]))
        line.insert(0, line[-2])
        line.insert(0, line[-1])


    print('\n'.join(line))
