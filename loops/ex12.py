#nested loop example
from turtle import *

move =5
while True:
    for i in range(6):
        fd(100+move)
        
        rt(60)
        pencolor('blue')
        fillcolor('green')
        begin_fill()
        for i in range(6):
            fd(50)
            rt(60)
        end_fill()
        pencolor('red')
    rt(60)
   
rt(5)
move+= 4

hideturtle()
mainloop()