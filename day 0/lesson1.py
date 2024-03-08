from turtle import *

#we want to paint a house

#step one draw a square
speed(60)
width(5)
color("green")
forward(200)
left (90)

forward(200)
left(90)

forward (200)
left(90)

forward(200)
left (90)
# end of square

#draw a door 

forward(70)
color("red")
begin_fill()
left(90)
forward(120)   #height of thr door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown()

color("yellow")
begin_fill()
right(150)
forward(170)
left(111)
forward(187)
end_fill()

left(129)
color("green")
forward(40)
left(90)
left(180)

color("white")
forward(20)
left(90)


color("black")
begin_fill()
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
end_fill()


penup()
goto(200,200)
pendown()

color("green")
left(90)


forward(30)
right(90)
right(180)

color("white")
forward(20)
left(90)

color("black")
begin_fill()
left(180)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
end_fill()

exitonclick()