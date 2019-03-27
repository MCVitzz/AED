from Queue import Queue
from random import randint
from Deque import Deque

def get_count(question):
        try:
            c = input(question + '\n')
            c = int(c)
            if c <= 0:
                return get_count(question)
            return c
        except:
            return get_count('Please enter a valid number')

def play_hot_potato():
        num_players = get_count('How many players does this game have?')
        name_list = []
        for i in range(num_players):
            name = input('Enter player name: \n')
            name_list.append(name)

        name_list = Queue.to_queue(name_list)
        count = randint(1, 100)

        while name_list.size() > 1:
            for i in range(count):
                name_list.push(name_list.pop())
            name_list.pop()
            count = randint(1, 100)
            print(count)
        print('The winner is', name_list.pop(), '\n')


def is_palindrome(expression):
    expression = expression.replace(' ', '')
    deque = Deque()
    for c in expression:
        deque.add_rear(c)
    while deque.size() > 1:
        if deque.pop_rear() != deque.pop_front():
            print('Not palindrome!!')
            return
    print('Is palindrome!')