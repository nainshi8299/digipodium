#hexagon
from turtle import *


speed('fastest')
bgcolor('white')
pencolor('red')
fillcolor('green')
begin_fill()
for i in range(6):
    fd(100)
    lt(360/6)
    
    #write(i)
    #circle(i)
    
end_fill()   

hideturtle()
mainloop()    
