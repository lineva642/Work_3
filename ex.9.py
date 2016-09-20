import turtle
turtle.shape('turtle')

def draw_circle(r):
  a = 3
  dx= r * 3.14/180*a
  for i in range(1000):
    turtle.forward(dx)
    r = r + 0.5
    dx= r * 3.14/180*a
    turtle.left(a)
draw_circle(50)
