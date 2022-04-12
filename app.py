import turtle
import random
import time
from pygame import mixer


mixer.pre_init(frequency=48000, size=-16, channels=2, buffer=512)
mixer.init()
mixer.music.load("Happy_birthday_song_status_-_Mix_tw_(getmp3.pro).mp3")

bg = turtle.Screen()
bg.bgpic("aanan.gif")

bg.bgcolor("lightblue")
mixer.music.play()



turtle.penup()
turtle.goto(-170,-180)
turtle.color("green")
turtle.pendown()
turtle.forward(350)

turtle.backward(50)
turtle.write(arg=f"Happy Bday Aanann!",move=True, align="center", font=("jokerman", -20, "normal"))

turtle.penup()
turtle.goto(-160,-150)
turtle.color("blue")
turtle.pendown()
turtle.forward(300)

turtle.penup()
turtle.goto(-150,-120)
turtle.color("red")
turtle.pendown()
turtle.forward(250)
bg.bgcolor("lightgreen")

turtle.penup()
turtle.goto(-100,-100)
turtle.color("pink")
turtle.begin_fill()
turtle.pendown()
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.left(90)
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.end_fill()
bg.bgcolor("lightblue")

turtle.penup()
turtle.goto(-90,0)
turtle.width(5)
turtle.color("red")
turtle.left(180)
turtle.pendown()
turtle.forward(20)
turtle.penup()
turtle.goto(-60,0)
turtle.width(5)
turtle.color("blue")
turtle.pendown()
turtle.forward(20)
turtle.penup()
turtle.goto(-30,0)
turtle.width(5)
turtle.color("yellow")
turtle.pendown()
turtle.forward(20)
turtle.penup()
turtle.goto(0,0)
turtle.width(5)
turtle.color("green")
turtle.pendown()
turtle.forward(20)
turtle.penup()
turtle.goto(30,0)
turtle.width(5)
turtle.color("purple")
turtle.pendown()
turtle.forward(20)
bg.bgcolor("orange")

colors = ["red", "orange", "yellow", "green", "blue", "purple", "black"]
turtle.penup()
turtle.goto(-40,-50)
turtle.pendown()

for each_color in colors:
    angle = 360 / len(colors)
    turtle.color(each_color)
    turtle.circle(10)
    turtle.right(angle)
    turtle.forward(10)

bg.bgcolor("lightblue")


turtle.penup()
turtle.goto(-150, 50)
turtle.color("pink")
turtle.pendown()



time.sleep(25)
