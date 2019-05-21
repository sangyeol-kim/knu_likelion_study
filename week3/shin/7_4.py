line = input()

arr = []
for i in range(26):
    arr.append(0)

for i in range(len(line)):
    if(ord(line[i]) >= 65 and ord(line[i]) <= 90):
        arr[ord(line[i]) - 65] += 1
    if(ord(line[i]) >= 97 and ord(line[i]) <= 122):
        arr[ord(line[i]) - 97] += 1

max = -1
maxIndex = 0
for i in range(len(arr)):
    if(arr[i] >= max):
        max = arr[i]
        maxIndex = i

result = 0
for i in range(len(arr)):
    if(max == arr[i]):
        result += 1

if(result == 1):
    print(chr(maxIndex+65))
else:
    print("?")