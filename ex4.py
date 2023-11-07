from turtle import *
speed('fastest')
bgcolor('light blue')
pensize(7)
fillcolor('red')
begin_fill()
dis = [100,100,100,100,100,100,80,60,80,290,100,190,100,190,100,100,190]
ng1 = [90,45,90,45,90,90,90,90,90,90,90,90,90,90,45,45,90]

for d,a in zip(dis,ng1):
    fd(d)
    lt(a)
end_fill()

hideturtle()
mainloop()
