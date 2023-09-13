
from turtle import *


speed('fastest')
bgcolor('white')
pencolor('red')
for i in range(1,100,5):
    fd(i)
    lt(360/6)
    write(i)
    circle(i)
       

hideturtle()
mainloop()    
