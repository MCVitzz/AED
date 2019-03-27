class Deque:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def pop_front(self):
        return self.items.pop(0)

    def pop_rear(self):
        return self.items.pop()

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)