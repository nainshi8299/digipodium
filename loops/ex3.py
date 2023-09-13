from turtle import *
speed('slowest')
dis = [100,100,100,100,100,100,70,60,70]
ng1 = [90,45,90,45,90,90,90,90,90]

for d,a in zip(dis,ng1):
    fd(d)
    lt(a)

    
hideturtle()
mainloop()