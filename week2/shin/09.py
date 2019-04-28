# *********
#  *******
#   *****
#    ***
#     *
#    ***
#   *****
#  *******
# *********
n = int(input())
line = []
for i in range(n):
    line.append(" "*(i) + "*"*(2*(n-i-1)+1))

if(n != 1):
    line += line[n-2::-1]
print("\n".join(line))
