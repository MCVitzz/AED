import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(myTurtle, size):
    if size > 0:
        myTurtle.forward(size)
        myTurtle.right(30)
        drawSpiral(myTurtle,size-5)

def tree(branchLen, t):
    if branchLen > 5:
        myTurtle.forward(branchLen)
        myTurtle.right(20)
        tree(branchLen - 15, myTurtle)
        myTurtle.left(40)
        tree(branchLen - 15, myTurtle)
        myTurtle.right(20)
        myTurtle.backward(branchLen)

tree(75,myTurtle)
myWin.exitonclick()