import sys
input = sys.stdin.readline
class Queue():
    def __init__(self):
        self.q = []
        self.b = -1; self.f = 0

    def proc(self, command):
        c = command[0]
        if c == 'push':
            self.q.append(int(command[1]))
            self.b += 1
        elif c == 'pop':
            if self.is_empty():   print(-1)
            else:
                print(self.q[self.f])
                self.f += 1
        elif c == 'back':
            if self.is_empty():   print(-1)
            else:               print(self.q[self.b])
        elif c == 'front':
            if self.is_empty():   print(-1)
            else:               print(self.q[self.f])
        elif c == 'empty':
            print(1) if self.is_empty() else print(0)
        elif c == 'size': print(self.b - self.f + 1)

    def is_empty(self):
        return True if self.b - self.f < 0 else False


queue = Queue()
for _ in range(int(input())):
    command = input().split()
    queue.proc(command)