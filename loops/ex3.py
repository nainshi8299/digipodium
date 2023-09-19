from turtle import *
speed('fastest')
pensize(4)
dis = [100,100,100,100,100,100,70,60,70,]
ng1 = [90,45,90,45,90,90,90,90,90]

for d,a in zip(dis,ng1):
    fd(d)
    lt(a)
penup()    
goto(24,90)
pendown()
circle(20,360) 
penup()
fd(77)
lt(90)
fd(10)
pendown() 

l1=[120,100,17]
l2=[45,90,90]
for i,j in zip(l1,l2):
    lt(j)
    fd(i)
penup()

rt(90)
fd(4)
lt(48.1)
pendown()

fd(100)    

    
#hideturtle()
mainloop()