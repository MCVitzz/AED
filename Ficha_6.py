def invert(string):
    if not string:
        return

    c = string[0]
    invert(string[1:])
    print(c)


def is_palyndrome(string):
    if len(string) < 1:
        return True

    c1 = string[0]
    c2 = string[-1]
    if c1 is c2:
        return is_palyndrome(string[1:-1])
    return False

def reverse_list(lst):
    if len(lst) is 0:
        return []

    return [lst[-1]] + reverse_list(lst[:-1])

def factorial(num):
    if num is 0:
        return 1

    return num * factorial(num-1)

def fibonacci_recursive(num):
    if num < 0:
        return
    elif num is 0:
        return 0
    elif num is 1:
        return 1
    else:
        return fibonacci_recursive(num - 1) + fibonacci_recursive(num - 2)


def fibonacci_iterative(num):
    if num < 0:
        return
    elif num is 0:
        return 0
    elif num is 1 or num is 2:
        return 1
    else:
        a = 1
        b = 1
        c = 0
        for _ in range(num - 2):
            c = (a + b)
            a = b
            b = c
    return c
    
def pascal_triangle(num):
    if num < 0:
        return 
    line = []
    for i in range(num + 1):
        line.append(int(factorial(num) / (factorial(i) * factorial(num - i))))
    pascal_triangle(num - 1)
    print(line)