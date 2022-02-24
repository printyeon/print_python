import turtle
t=turtle.Pen()
t.pencolor("red")
t.shape("turtle")

while True :
    
    num=turtle.textinput("",'');

    if(num=="w") :
        t.forward(50)
    if(num=="a") :
        t.left(20)
    if(num=="s") :
        t.backward(50)
    if(num=="d") :
        t.right(20)
    if(num=="q") :
        t.penup()
    if(num=="e") :
        t.pendown()
    if(num=="z") :
        break;

