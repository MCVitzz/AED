from ADTStack import Stack

class Converter:
    @staticmethod
    def  is_operator(c):
        ops = ['+', '-', '*', '/', '^']
        return c in ops

    @staticmethod
    def is_float(num):
        try:
            float(num)
            return True
        except ValueError:
            return False
    @staticmethod
    def convert_to_postfix(expression):
        precedence = {'+':2, '-':2, '*':3, '/':3, '^':4, '(':1}
        op_stack = Stack()
        lst = []
        tk = ''
        token_list = expression.split(' ')
        try:
            for token in token_list:
                tk = token
                if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or Converter.is_float(token):
                    lst.append(token)
                    lst.append(' ')
                elif token == '(':
                    op_stack.push(token)
                elif token == ')':
                    while not op_stack.is_empty() and op_stack.peek() != '(':
                        lst.append(op_stack.pop())
                        lst.append(' ')
                    op_stack.pop()
                else:
                    while not op_stack.is_empty():
                        if precedence[op_stack.peek()] >= precedence[token]:
                            lst.append(op_stack.pop())
                            lst.append(' ')
                        else:
                            break
                    op_stack.push(token)

            while not op_stack.is_empty():
                lst.append(op_stack.pop())
                lst.append(' ')
        except IndexError:
            return 'Bad Expression: ' + expression
        except KeyError:
            return 'Invalid Operator: \'' + tk + '\' in expression: ' + expression

        return ''.join(lst)




#print(Converter.convert_to_postfix("A * B + C ^ D"))
#print(Converter.convert_to_postfix("( 4.4 + 4.6 ) ^ ( 2 / ( 1 + 3 ) )"))
#print(Converter.convert_to_postfix("( 2 ^ 20 ) ^ ( 2 / ( 1 + 3 ) )"))
#print(Converter.convert_to_postfix("A * B ) + ( C ^ D )"))
#print(Converter.convert_to_postfix("( A * B ) + (C ^ D )"))
#print(Converter.convert_to_postfix("7 + 9 * 8 / 4 ^ 2"))
#print(Converter.convert_to_postfix("( 17 + 9 ) * 3 / ( 5 - 3 ) ^ 4"))