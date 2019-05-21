# *********
# * ** ** *
# *********
# ***   ***
# * *   * *
# ***   ***
# *********
# * ** ** *
# *********
n = int(input())
k = 1
if(n == 1):
    print("*")
else :
    while (pow(3, k) != n):
        k += 1
    line = ["***", "* *", "***"]
    for i in range(1, k):
        line *= 3
        for j in list(range(0, len(line) // 3)) + list(range(len(line) // 3 * 2, len(line))):
            line[j] *= 3
        for k in range(len(line) // 3, len(line) // 3 * 2):
            line[k] += ' ' * (len(line[k]))
            line[k] += line[k][0: len(line[k]) // 2]
    print('\n'.join(line))






