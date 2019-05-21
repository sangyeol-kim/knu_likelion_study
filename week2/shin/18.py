# *****************************
#  *            *            *
#   *          * *          *
#    *        *   *        *
#     *      *******      *
#      *    *  ***  *    *
#       *  *    *    *  *
#        ***************
#         *           *
#          *         *
#           *       *
#            *     *
#             *   *
#              * *
#               *

n = int(input())

if(n == 1):
    print("*")
else :
    line = ['*****', ' ***', '  *']
    for i in range(2, n):
        length = len(line)
        if(i % 2 == 0):
            for j in range(0, length):
                line[j] = ' '*(length-j) + '*' + ' '*j + line[j] + ' '*j*2 + '*'
            line.append('*'*(len(line[0])+length))
            length = len(line) - 1
            for j in range(length):
                line.insert(0, ' '*(length+1+j) + '*'*(1 if j != length-1 else 0) + ' '*(2*(length-j-1)-1) + '*')
        else:
            for j in range(0, length):
                line[j] = ' '*(j+1) + '*' + ' '*(length-j-1) + line[j] + ' '*(length-j-1)*2 + '*'
            line.insert(0, '*'*(len(line[0])+1))
            for j in range(length):
                line.append(' '*(length+j+1) + '*' + ' '*(2*(length-j-2)+1) + '*'*(1 if j != length-1 else 0))


    print('\n'.join(line))



