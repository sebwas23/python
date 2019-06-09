import turtle
t = turtle.Turtle(shape="turtle")
def kolko(kolor1,kolor2,x,y,r):
    t.color(kolor1,kolor2)
    t.penup()
    t.setpos(x,y)
    t.pendown()
    t.begin_fill()
    t.circle(r)
    t.end_fill()

kolko("red","red",0,100,50)
kolko("yellow","yellow",0,-50,50)
kolko("green","green",0,-200,50)
