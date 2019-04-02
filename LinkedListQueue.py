from LinkedList import LinkedList

class Queue:
    def __init__(self):
        self.items = LinkedList()

    def is_empty(self):
        return self.items.is_empty()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def peek(self):
        return self.items.get(0)

    def size(self):
        return self.items.size()