import turtle as t
t.shape('turtle')
s=input()
a=50
t.speed(3)
for n in range (len(s)):
if s[n]=="l":
    t.goto(t.xcor()-a,t.ycor())
elif s[n]=="r":
    t.goto(t.xcor()+a,t.ycor())
elif s[n]=="d":
    t.goto(t.xcor(),t.ycor()-a)
elif s[n]=="u":
    t.goto(t.xcor(),t.ycor()+a)
elif s[n]=="+":
    t.pendown()
elif s[n]=="-":
    t.penup()
