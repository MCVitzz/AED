import turtle
import random

min_angle = 15
max_angle = 45
angle = random.randint(min_angle, max_angle)
myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(myTurtle, size):
    if size > 0:
        myTurtle.forward(size)
        myTurtle.right(30)
        drawSpiral(myTurtle,size-5)

def tree(branchLen, t):
    if branchLen > 5:
        myTurtle.color((40, 114 - branchLen, 47), (40, 114 - branchLen, 47))
        subtract = random.randint(5, 20)
        myTurtle.pensize(branchLen * .1)
        myTurtle.forward(branchLen)
        myTurtle.right(angle)
        tree(branchLen - subtract, myTurtle)
        myTurtle.left(angle * 2)
        tree(branchLen - subtract, myTurtle)
        myTurtle.right(angle)
        myTurtle.backward(branchLen)
        

myWin.colormode(255)
print(myTurtle.color())
tree(75, myTurtle)
myWin.exitonclick()