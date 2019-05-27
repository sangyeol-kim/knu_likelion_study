import sys

a = []
pm = []
stack = []
word = ''

N = int(input())

for _ in range(N):
  a.append(int(sys.stdin.readline()))
  
while (len(a) != 0):
  if pm == []:
    for _ in range(a[0]):
      pm.append('+')
    pm.append('-')
    temp = a[0]
    a.remove(temp)
    stack.append(temp)
  else:
    if a[0] > temp:
      b = 0
      for n in stack:
        if n > temp and n < a[0]:
          b += 1
      for _ in range(a[0]-temp-b):
        pm.append('+')
      pm.append('-')
      temp = a[0]
      a.remove(temp)
      stack.append(temp)
    else:
      for k in a:
        if temp > k and a[0] < k:
          del pm
          pm = 'NO'
          break
      
      if pm == 'NO':
        break
      b = 0
      for n in stack:
        if n < temp and n > a[0]:
          b += 1
      
      for _ in range(temp - a[0] - b):
        pm.append('-')
      temp = a[0]
      a.remove(temp)
      stack.append(temp)

if word == 'NO':
  print(word)
else:
  for n in pm:
    print(n)