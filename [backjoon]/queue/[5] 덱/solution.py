import sys
input = sys.stdin.readline

class Deque():
    def __init__(self, n):
        self.arr = [None for _ in range(2*n + 1)]
        self.f, self.b = n, n - 1

    def proc(self, command):
        if command[0][:4] == 'push':
            num = int(command[1])
            if command[0] == 'push_back':
                self.b += 1
                self.arr[self.b] = num
            else: # front 
                self.f -= 1
                self.arr[self.f] = num
        elif command[0] == 'size':        
            print(self.b - self.f + 1)
        elif command[0] == 'empty':
            if self.is_empty(): print(1)
            else:               print(0)

        elif self.is_empty():
            print(-1); return

        elif command[0] == 'pop_front':
            print(self.arr[self.f])
            self.f +=1
        elif command[0] == 'pop_back':
            print(self.arr[self.b])
            self.b -=1
        
        elif command[0] == 'front':
            print(self.arr[self.f])
        elif command[0] == 'back':
            print(self.arr[self.b])
    
    def is_empty(self):
        return True if self.b - self.f < 0 else False



deq = Deque(10000)
for _ in range(int(input())):
    command = input().split()
    deq.proc(command)