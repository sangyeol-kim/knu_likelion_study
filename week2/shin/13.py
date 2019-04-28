n = int(input())
line = []
for i in range(n):
    line.append("*"*(i+1))

line += line[n-2::-1]
if (n == 1):
    print("*")
else:
    print("\n".join(line))