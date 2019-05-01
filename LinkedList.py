from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.nodes = 0

    def is_empty(self):
        return self.head == None

    def size(self):
        return self.nodes

    def get(self, pos):
        i = 0
        n = self.head
        while i != pos:
            n = n.next
            i += 1
        return n

    def index_of(self, item):
        i = 0
        n = self.head
        while n != None:
            if n.data == item:
                return i
            n = n.next
            i += 1
        return -1

    def insert(self, pos, item):
        if pos == 0:
            new = Node(item)
            new.next = self.head
            self.head = new
            return
        i = 0
        n = self.head
        prev = None
        while i != pos:
            prev = n
            n = n.next
            i += 1
        new = Node(item)
        prev.next = new
        new.next = n


    def append(self, item):
        n = self.head
        p = None
        if n == None:
            self.head = Node(item)
            return
            
        while n != None:
            p = n
            n = n.next
        p.next = Node(item)
        self.nodes += 1

    def add(self, item):
        n = self.head
        p = None
        if n == None:
            self.head = Node(item)
            return
        while n != None:
            p = n
            n = n.next
        p.next = Node(item)
        self.nodes += 1

    def remove(self, item):
        if self.head == None:
            return
        if self.head.data is item:
            self.head = self.head.next
            return
        
        n = self.head
        while n.next is not None:
            if n.next.data is item:
                n.next = n.next.next

            n = n.next

    def pop(self, pos = None):
        if pos is None:
            pos = self.nodes -1
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


    def search(self, item):
        n = self.head
        while n.data != item:
            n = n.next

        return n.data

    def __str__(self):
        s = '[ '
        n = self.head
        while n != None:
            s += str(n.data) + ', '
            n = n.next
        s += ']'
        s = s.replace(', ]', ' ]')
        return s

    def copy(self):
        lst = LinkedList()
        n = self.head
        while n is not None:
            lst.append(n.copy())
            n = n.next

        return lst

    def concatenate(self, other):
        last = self.get(self.size() - 1)
        last.next = other.head

my_list = LinkedList()
my_list.add(93)
my_list.add(93)
my_list.add(93)
print(my_list.pop(0))
print(my_list.pop(0))
print(my_list.pop(0))
print(my_list)

        

            