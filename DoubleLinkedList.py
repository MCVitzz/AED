from Node import DoubleNode

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, item):
        item = DoubleNode(item)
        if self.head is None:
            self.head = item
            self.tail = item

        else:
            n = self.head
            while n.next is not None:
                n = n.next

            n.next = item
            self.tail = item

    def remove(self, item):
        n = self.head
        while n.data is not item:
            n = n.next

        n.previous.next = n.next

    def search(self, item):
        n = self.head
        while n.data is not item:
            n = n.next

        return n

    def is_empty(self):
        return self.head is None

    def size(self):
        n = self.head
        i = 0
        while n is not None:
            n = n.next
            i += 1

        return i

    def append(self, item):
        item = DoubleNode(item)
        if self.is_empty():
            self.head = item
            self.tail = item
        else:
            self.tail.next = item
            self.tail = item


    def index(self, item):
        n = self.head
        i = 0
        while n.data is not item:
            n = n.next
            i += 1

        return i

    def insert(self, pos, item):
        item = DoubleNode(item)
        if pos == 0:
            new = item
            new.next = self.head
            self.head.previous = item
            self.head = new
            return
        i = 0
        n = self.head
        prev = None
        while i != pos:
            prev = n
            n = n.next
            i += 1
        item.previous = prev
        prev.next = item
        item.next = n

    def pop(self, pos = None):
        if pos is None:
            pos = self.size() -1
        i = 0
        n = self.head
        prev = None
        while i != pos:
            prev = n
            n = n.next
            i += 1
        popped = None
        if prev != None and n.next != None:
            popped = n
            prev.next = n.next
            n.next.previous = prev
            n = n.next
        elif prev == None:
            popped = n
            self.head = n.next
            n = n.next
        elif n.next == None:
            popped = n
            prev.next = None
            n = n.next
            prev = n
        return popped
