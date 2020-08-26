import turtle as t
#make turtle program speed of turtle
t.reset()
t.speed(0)
t.ht()
#make variables for position of turtle
posX = -300
posY = 300
#make a 2d backend of the 4inarow
Board = [
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
]
#getter for values in board
def getBoardValue(x,y):
    return Board[x][y]
#setter for values in board
def setBoardValue(x,y,color):
    Board[x][y] = color
#set position of x and y and define it when called pen up and pen down so it does not draw its route
def setPosition(x,y):
    t.penup()
    t.setpos(x,y)
    t.pendown()
#draw the border of the board
def drawOutline():
    for s in range(4):
        t.fd(600)
        t.rt(90)
#draws circle         
def drawCircle(color):
    t.color('black', color)
    t.begin_fill()
    t.circle(30)
    t.end_fill()    
#draws circles and repeats the process 8 times in a row
def drawRow(color):
    t.penup()
    t.fd(50)
    t.pendown()
    for circle in range(8):
        drawCircle(color)
        t.penup()
        t.fd(70)
        t.pendown()
#draws circles repeats 8 times and goes down
def drawColumn(x,y,color):
    for s in range(8):
        y = y - 72
        t.penup()
        t.setpos(x,y)
        t.pendown()
        drawRow(color)
#checks if collumn is empty
def checkCollumForEmpty(collum):
    x = 7
    for i in range(8):
        if getBoardValue(x,collum) == 0:
            t.penup()
            t.setpos(convertX(x), convertY(collum))
            t.pendown()
            drawCircle('red')
            
            
        x = x - 1  
#eventHandeler checks if the coordinate thats clicked is empty by using a function already made before called checkCollumForEmpty()        
def clickEventHandeler(x,y):
    if x >= -300 and x <= -225:
        checkCollumForEmpty(0)
    elif x >= -224 and x <= -150:
        checkCollumForEmpty(1)
    elif x >= -149 and x <= -75:
        checkCollumForEmpty(2)
    elif x >= -74 and x <= 0:
        checkCollumForEmpty(3)
    elif x >= 1 and x <= 75:
        checkCollumForEmpty(4)
    elif x >= 76 and x <= 150:
        checkCollumForEmpty(5)
    elif x >= 151 and x <= 225:
        checkCollumForEmpty(6)
    elif x >= 226 and x <= 301:
        checkCollumForEmpty(7)
    
#We call the functions
setPosition(posX,posY)
drawOutline()
drawColumn(posX,posY,'white')
#eventListener
t.onscreenclick(clickEventHandeler)
