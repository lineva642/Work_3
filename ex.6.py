import turtle
turtle.shape('turtle')
a = int(input())
b = int(input())
s = 50
def draw_circle(r, a):
  dx= r * 3.14/180*a
  for i in range(360//a):
    turtle.forward(dx)
    turtle.left(a)

def reg_pol(n, r):
  draw_circle(r, 360//n)

reg_pol(a, s)
turtle.penup()
turtle.goto(2*s, s/2)
turtle.pendown()

turtle.forward(s)
turtle.backward(s/2)
turtle.left(90)
turtle.forward(s/2)
turtle.backward(s)

turtle.penup()
turtle.forward(s)
turtle.left(90)
turtle.backward(s*2.5)
turtle.pendown()

reg_pol(b, s)

turtle.penup()
turtle.goto(5.5*s+5, s/2)
turtle.pendown()
turtle.forward(20)
turtle.right(90)
turtle.penup()
turtle.forward(10)
turtle.pendown()
turtle.right(90)
turtle.forward(20)

turtle.penup()
turtle.forward(2*s)

turtle.pendown()
reg_pol(a+b, s)
