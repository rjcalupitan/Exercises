class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items ==[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def printstack(self):
        for items in reversed(self.items):
            print (items)

s = Stack()
print(s.isEmpty())
print(' ')
s.push('Green')
s.push('Blue')
s.push('Yellow')
s.push('Red')
print(s.isEmpty())
print(' ')
s.printstack()
print(' ')
print(s.pop())
print(' ')
print(' ')
s.printstack()
