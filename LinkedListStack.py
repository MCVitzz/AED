from LinkedList import LinkedList

class Stack:
    def __init__(self):
        self.items = LinkedList()

    def is_empty(self):
        return self.items.is_empty()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items.get(self.items.size() - 1)

    def size(self):
        return self.items.size()

    
