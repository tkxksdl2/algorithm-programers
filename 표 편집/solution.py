def solution(n ,k ,cmd):
    answer = ['O'for _ in range(n)]
    linked_list = LinkedList(n, k)

    for command in cmd:
        if command[0] in ['D', 'U']:
            if command[0] =='D': linked_list.next_point(int(command[2:]))
            else:                linked_list.pre_point(int(command[2:]))
            
        elif command[0] == 'C':
            linked_list.clear()
                
        else:
            linked_list.undo()

    for d in linked_list.deleted:
        answer[d['value']] = 'X'

    return ''.join(answer)

class LinkedList():
    def __init__(self, n, k):
        self.lst = [{'value':i, 'pre': i-1, 'next': i+1} for i in range(n)]
        self.lst[0]['pre'] = None
        self.lst[-1]['next'] = None
        self.pointed = self.lst[k]
        self.deleted = []

    def next_point(self, i):
        for _ in range(i):
            self.pointed = self.lst[self.pointed['next']]

    def pre_point(self, i):
        for _ in range(i):
            self.pointed = self.lst[self.pointed['pre']]
    
    def clear(self):
        self.deleted.append(self.pointed)
        if self.pointed['pre'] != None:
            self.lst[self.pointed['pre']]['next'] = self.pointed['next']
        if self.pointed['next'] != None:
            self.lst[self.pointed['next']]['pre'] = self.pointed['pre']
            self.next_point(1)
            return
        self.pre_point(1)

    def undo(self):
        undo_point = self.deleted.pop()
        if undo_point['pre'] != None:
            self.lst[undo_point['pre']]['next'] = undo_point['value']
        if undo_point['next'] != None:
            self.lst[undo_point['next']]['pre'] = undo_point['value']


        
n, k = 8,2
cmd =["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
print(solution(n,k, cmd))
