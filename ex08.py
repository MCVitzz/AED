from Queue import Queue

def process(q, a, b):
    while not q.is_empty():
        y = q.pop()
        x = q.pop()
        if y == 'X':
            if a.size() > b.size():
                b.push(x)
            elif a.size() < b.size():
                a.push(x)
        elif y == 'A':
            a.push(x)
        elif y == 'B':
            b.push(x)

        
def merge(a, b):
    merge_queue = Queue()
    while not a.is_empty() or not b.is_empty():
        if a.is_empty():
            merge_queue.push(b.pop())
        elif b.is_empty():
            merge_queue.push(a.pop())
        elif a.peek() < b.peek():
            merge_queue.push(a.pop())
        elif a.peek() > b.peek():
            merge_queue.push(b.pop())
        else:
            merge_queue.push(a.pop())
            merge_queue.push(b.pop())

    return merge_queue


def read_int():
    while True:
        try:
            n = int(input("Número de nomes --> "))
            if n >= 1:
                return n
            else:
                print("Ops! O número tem de ser um inteiro positivo")
        except ValueError:
            print("Ops! O número tem de ser um inteiro positivo")

#def #main ():
#
    #q = Queue()
    #a = Queue()
    #b = Queue()
#
    #n = read_int()
#
    #for i in range(0, n):
#
    #    nome_operacao = input("Nome e Operação (separados por espaço) --> ")
    #    nome_operacao = nome_operacao.split()
#
    #    q.push(nome_operacao[1])
    #    q.push(nome_operacao[0])
#
    #print("Início:")
    #print("q: ", q)
    #print("a: ", a)
    #print("b: ", b)
#
    #process(q, a, b)
#
    #print("-------------------------------")
    #print("q: ", q)
    #print("a: ", a)
    #print("b: ", b)
#

def test_merge():
    a = Queue.to_queue([1, 4, 9])
    b = Queue.to_queue([1, 4, 9 ])
    c = merge(a, b)
    print(c)

test_merge()
