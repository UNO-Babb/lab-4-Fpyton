#TurtleGraphics.py
#Name:
#Date:
#Assignment:

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(joe, sides):
    for s in range(sides):
        joe.forward(50)
        joe.right(360/sides)
        
def fillCorner(alice, corner):
    #draw big square
    drawSquare(alice, 100)
    
    
    if corner == 1:
        alice.begin_fill()   
        drawSquare(alice, 50)
        alice.end_fill()
    elif corner == 2:
        alice.forward(50)
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
    elif corner == 3:
        alice.right(90)
        alice.forward(50)
        alice.left(90)
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
    elif corner == 4:
        alice.right(90)
        alice.forward(50)
        alice.left(90)
        alice.forward(50)
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
        


def drawSquare(myTurtle, size):
    myTurtle.penup()
    myTurtle.goto(-size/2, -size/2)  # bottom-left corner so it's centered
    myTurtle.pendown()
    for _ in range(4):
        myTurtle.forward(size)
        myTurtle.left(90)

def squaresInSquares(myTurtle, size, count=5, step=40):
    for i in range(count):
        drawSquare(myTurtle, size)
        size += step   # each square bigger

def concentricSquares(myTurtle, size, count=3, step=40):
    for i in range(count):
        drawSquare(myTurtle, size)
        size += step   # each square bigger


# Setup
wn = turtle.Screen()
alice = turtle.Turtle()
alice.speed(0)
# concentricSquares(alice, 50, 5, 40)
# squaresInSquares(alice, 50)

wn.mainloop()


        

turtle.done()

    
def main():
    myTurtle = turtle.Turtle()
    
    # drawSquare(myTurtle, 100)
    
    # drawPolygon(myTurtle, 5) #draws a pentagon
    # drawPolygon(myTurtle, 8) #draws an octogon
    # drawPolygon(myTurtle, 3)  #draws a triangle

    # fillCorner(myTurtle, 1) #draws a square with top right left filled in.
    # fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.
    # fillCorner(myTurtle, 4) #draws a square bottom right corner filled in.
    # squaresInSquares(alice, 50, 5, 40) #draws 5 concentric squares
    # concentricSquares(alice, 50, 3, 40) #draws 3 concentric squares


main()
