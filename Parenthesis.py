from ADTStack import Stack

def is_balanced(chars, input):
    stack = Stack()
    for i in input:
        if i == chars[0]:
            stack.push(i)
        elif i == chars[1]:
            if stack.is_empty():
                return False
            else:
                 stack.pop()

    return stack.is_empty()


input1 = '()'

input2 = '[[[[[[[]]]]]]]]]]]]]'

input3 = '{{{{{{{{{{{}}}}}}}}}}}}}}}}'

print('(): ' + str(is_balanced(['(', ')'], input1)))
print('[]: ' + str(is_balanced(['[', ']'], input2)))
print('{}: ' + str(is_balanced(['{', '}'], input3)))


    