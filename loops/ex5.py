from turtle import *

speed('fastest')
bgcolor('black')
pencolor('red')
pensize(5)
#goto(-250,250)

for i in range (1,900,5):
    fd(i)
    lt(360/5)
    write(i)
    
hideturtle()
    
mainloop()   