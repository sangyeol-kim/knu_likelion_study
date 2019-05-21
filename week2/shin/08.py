# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *

n = int(input())
line = []
for i in range(n):
    line.append("*"*(i+1)+" "*(2*(n-1-i))+"*"*(i+1))
print('\n'.join(line + ([] if n-2 < 0 else line[n-2::-1])))
# print('\n'.join(line+line[(n-2 if n-2>0 else 0)::-1]))
