import turtle
#Make a Turtle screen
screen = turtle.screen()
#Make a Turtle object
pen = turtle.Turtle()
#set the speed of turtle
pen.speed (2)
#Define colors
colors = ["pink", "yellow", "black" , "red" , "oreng" , "green" , "cream"]
#Draw a colorful square
for color in colors:
    pen.color(color)
    pen.forward (100)
    pen.left(90)
#close the Turtle graphics window on click
screen.exitonlick()
