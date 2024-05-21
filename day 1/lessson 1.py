from turtle import *

#we want to paint a house

#step 1: draw a square

speed(30)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color ("yellow")
begin_fill()
left(90)
forward(120)   #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown()

color("red")   #roof
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


penup()
goto (170, 170)
pendown()

color("blue") #window1
begin_fill()
left (30)
forward (20)
right(90)
forward(20)
right(90)
forward(20)
right(90)
forward(20)
end_fill()

penup()
goto(50, 170)
pendown()

begin_fill()
forward(20)
right(90)

forward(20)
right(90)

forward(20)
right(90)

forward(20)
right(90)
end_fill()





exitonclick()