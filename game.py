import turtle as t

t.reset()

t.speed(0)

posX = -300
posY =  300
t.penup()

t.setx(posX)
t.sety(posY)

t.pendown()

for board in range(4):
    t.fd(600)
    t.rt(90)
    
for rows in range(8):
    t.penup()
    t.setx(posX)
    posY = posY - 72
    t.sety(posY)
    t.fd(50)
    t.pendown()
    for circle in range(8):
        t.circle(30)
        t.penup()
        t.fd(70)
        t.pendown()
