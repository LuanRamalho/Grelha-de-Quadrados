import turtle

a = turtle.Screen()
turtle.speed(0)
def quadrado(posx, posy,lado):
    turtle.showturtle()
    # posicioan
    turtle.penup()
    turtle.goto(posx, posy)
    turtle.pendown()

    # desenha
    for i in range(4):
        turtle.forward(lado)
        turtle.left(90)
    turtle.hideturtle()

def grelha(n,posx, posy,lado,cor):

    # inicialização
    turtle.pencolor(cor)
    for i in range(n):

        # desenha linha i
        for j in range(n):
            quadrado(turtle.xcor(),turtle.ycor(), lado)
            turtle.setx(turtle.xcor()+lado)

        # muda de linha
        turtle.penup()
        turtle.goto(posx,turtle.ycor()-lado)
        turtle.pendown()
    turtle.hideturtle()


quadrado(-100,280,50)
grelha(5,-100,280,50,'blue')

a.exitonclick()