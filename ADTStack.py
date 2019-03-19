class Stack:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        item = self.items[0]
        self.items.remove(item)
        return item

    def peek(self):
        return self.items[0]
    
    def size(self):
        return len(self.items)

    def reverse(self):
        t = Stack()
        while not self.is_empty():
            t.push(self.pop())

        self.items = t.items

    def remove(self, item):
        stack = Stack()
        while not self.is_empty():
            i = self.pop()
            if item != i:
                stack.push(i)
        self.items = stack.items
        self.reverse()

    def __str__(self):
        string = '['
        for c in self.items:
            string += (str(c) + ', ')

        string += ']'
        string = string.replace(', ]', ']')
        return string