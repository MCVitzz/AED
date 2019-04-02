class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


    def copy(self):
        return Node(self.data)

    def __str__(self):
        return 'data: ' + str(self.data)


class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None
        

    def __str__(self):
        return 'data: ' + str(self.data)
