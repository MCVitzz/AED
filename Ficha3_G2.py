from ADTStack import Stack
from Ficha3_G1 import Converter

def do_math(num1, num2, operator):
    if not Converter.is_float(num1) or not Converter.is_float(num2):
        res = str(num1) + ' ' + operator + ' ' + str(num2)
    else:
        num1 = float(num1)
        num2 = float(num2)
        if operator == '+':
            res = num1 + num2
        elif operator == '-':
            res = num1 - num2
        elif operator == '*':
            res = num1 * num2
        elif operator == '/':
            res = num1 / num2
        elif operator == '^':
            res = num1 ** num2
    
    return res

def postfix_eval(postfix):

    try:
        if(postfix.startswith('Bad Expression') or postfix.startswith('Invalid Operator')):
            return postfix
        token_list = postfix.split(' ')
        stack = Stack()
        for token in token_list:
            if (token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or Converter.is_float(token)) and token != '':
                stack.push(token)
            elif Converter.is_operator(token):
                num1 = stack.pop()
                num2 = stack.pop()
                #switched because it's in FIFO first pop is the second number beacause it was pushed last
                stack.push(do_math(num2, num1, token))

        return stack.pop()
    except IndexError:
        return 'Bad Expression: ' + postfix

    
postfixExpressions = ['4.4 4.6 + 2 1 3 + / ^', '2 20 ^ 2 1 3 + / ^', '2 20 + 2 1 3 ++ *', '2 -1 3 + -']
infixExpressions = ["7 + 9 * 8 - 4 ^ 2", "7 + 9 * 8 / 4 ^ 2", "( 17 + 9 ) * 3 / ( 5 - 3 ) ^ 4", "7.5 + 9 - 1.8 / 4 ^ 2.5"]

print(postfix_eval('2 20 + 2 1 3 + + *'))

#print('Postfix:\n')
#for pe in postfixExpressions:
#    print(pe, ' = ', postfix_eval(pe))
#print('\n\n')
#print('Infix:\n')
#for pe in infixExpressions:
#    print(pe, ' = ', postfix_eval(Converter.convert_to_postfix(pe)))

