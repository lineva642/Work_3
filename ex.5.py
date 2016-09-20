import turtle as tr
tr.shape("turtle")
s = 50
a = 90
p = 30
n = int(input())
for i in range(n):
  for i in range(4):
    tr.forward(s)
    tr.left(a)
  tr.penup()
  tr.backward(p/2)
  tr.right(a)
  tr.forward(p/2)
  tr.left(90)
  s+=p
tr.pendown()
