from collections import deque

class Stack():
    def __init__(self):
        self.arr = deque()
        self.len = 0

    def proc(self, command=list()):
        w = command[0]
        if w == 'push':
            self.push(int(command[1]))
        elif w == 'pop':
            if      self.isEmpty(): print(-1)
            else:   self.pop()
        elif w == 'top':
            if      self.isEmpty(): print(-1)
            else:   print(self.arr[self.len-1])
        elif w == 'empty':
            print(self.isEmpty())
        elif w == 'size':
            print(self.len)

    def push(self, num):
        self.arr.append(num)
        self.len += 1 
    
    def pop(self):
        print(self.arr.pop())
        self.len -= 1

    def isEmpty(self):
        if self.len == 0:
            return  1
        else: return 0
n = int(input())
Stk = Stack()

for _ in range(n):
    command = input().split()
    Stk.proc(command)


        