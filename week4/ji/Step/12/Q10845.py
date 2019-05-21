'''
https://www.acmicpc.net/problem/10845

step 12-1
'''

class Queue :
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if not self.items: # 비어있으면
            return -1
        else:
            temp = self.items[0]
            del self.items[0] # 가장 첫번째 데이터 지우기
            return temp


    def size(self):
        return len(self.items)

    def isEmpty(self):
        return '01'[len(self.items) == 0]

    def front(self):
        if not self.items: # 비어있으면
            return -1
        else:
            return self.items[0]

    def back(self):
        if not self.items:  # 비어있으면
            return -1
        else:
            return self.items[-1]

case = int(input())
queue = Queue()

for _ in range(case) :
    commend = input().split()

    if commend[0] == 'push':
        queue.push(int(commend[1]))

    if commend[0] == 'pop':
        print(queue.pop())

    if commend[0] == 'size':
        print(queue.size())

    if commend[0] == 'empty':
        print(queue.isEmpty())

    if commend[0] == 'front':
        print(queue.front())

    if commend[0] == 'back':
        print(queue.back())
