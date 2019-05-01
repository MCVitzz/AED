import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def snowflake(lengthSide, levels): 
	if levels is 0: 
		myTurtle.forward(lengthSide)
		return

	lengthSide /= 3.0
	snowflake(lengthSide, levels-1) 
	myTurtle.left(60)
	snowflake(lengthSide, levels-1) 
	myTurtle.right(120)
	snowflake(lengthSide, levels-1) 
	myTurtle.left(60)
	snowflake(lengthSide, levels-1) 
    

myTurtle.speed(0)				 
length = 300
myTurtle.penup()					 
myTurtle.backward(length/2.0)
myTurtle.pendown()
for i in range(3):
    snowflake(length, 3)
    myTurtle.right(120)
myWin.exitonclick()
