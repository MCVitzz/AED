class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        item = self.items[0]
        self.items.remove(item)
        return item

    def peek(self):
        return self.items[0]
    
    def size(self):
        return len(self.items)

    def __str__(self):
        string = ""
        for item in self.items:
            string = string + str(item) + " "
        return string

    @staticmethod
    def to_queue(items):
        queue = Queue()
        for item in items:
            queue.push(item)
        return queue