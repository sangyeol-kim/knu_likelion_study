n=int(input())
line=[]
for i in range(n-1):
    line+=['*'*n + ' '*(2*n-3)+'*'*n if i == 0
           else ' '*i+'*'+' '*(n-2)+'*'+' '*(2*(n-i)-3)+'*'+' '*(n-2)+'*']
for i in range(len(line)):
    print(line[i])
print(' '*(n-1) + '*' + ' '*(n-2) +'*' + ' '*(n-2) + '*')
for i in range(len(line)):
    print(line[len(line)-i-1])
