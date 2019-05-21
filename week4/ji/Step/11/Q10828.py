'''
https://www.acmicpc.net/problem/10828

백준 step 11 - 1
'''


class Stack:

    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if not self.items :
            return -1
        else :
            return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return('01'[self.items == []])

    def top(self):
        if not self.items :
            return -1
        else :
            return self.items[-1]


case = int(input())
stack = Stack()

for _ in range(case):
    commend = input().split()

    if commend[0] == 'push':
        stack.push(int(commend[1]))

    elif commend[0] == 'pop':
        print(stack.pop())

    elif commend[0] == 'size':
        print(stack.size())

    elif commend[0] == 'empty':
        print(stack.isEmpty())

    elif commend[0] == 'top':
        print(stack.top())