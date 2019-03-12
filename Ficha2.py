from ADTStack import Stack

def transfer(s, t):
    while not s.is_empty():
        t.push(s.pop())
    return t

def rev_string(str):
    stack = Stack()
    for c in str:
        stack.push(c)
    return stack
    
def is_balanced(chars, input):
    return input.count(chars[0]) == input.count(chars[1])

def test_html():
    script = ('<body>' 
    '<center>' 
    '<h1> The Little Boat </h1>' 
    '</center>' 
    '<p> The storm tossed the little ' 
    'boat like a cheap sneaker in an ' 
    'old washing machine. The three ' 
    'drunken fishermen were used to ' 
    'such treatment, of course, but ' 
    'not the tree salesman, who even as ' 
    'a stowaway now felt that he ' 
    'had overpaid for the voyage. </p>' 
    '<ol>' 
    '<li> Will the salesman die? </li>' 
    '<li> What color is the boat? </li>' 
    '<li> And what about Naomi? </li>' 
    '</ol>' 
    '</body>')
    print(str(is_balanced_html(script)))





def is_balanced_html(str):
    flag = is_balanced(['<body>', '</body>'], str)
    flag = flag and is_balanced(['<h1>', '</h1>'], str)
    flag = flag and is_balanced(['<center>', '</center>'], str)
    flag = flag and is_balanced(['<p>', '</p>'], str)
    flag = flag and is_balanced(['<ol>', '</ol>'], str)
    flag = flag and is_balanced(['<li>', '</li>'], str)

    return flag

def test_remove():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    print(stack)
    stack.remove(3)
    print(stack)

def test_transfer():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    print(stack)
    new_stack = transfer(stack, Stack())
    print(new_stack)

def test_rev_string():
    string = 'Vasco'
    print(string)
    print(''.join(rev_string(string).items))

test_html()