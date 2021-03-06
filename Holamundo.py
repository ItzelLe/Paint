from turtle import *
from freegames import vector 

def line(start, end): #Funcion que hace una linea
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start,end): #Funcion que hace un cuadrado
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def circles(start, end):#Funcion que hace un circulo
    "Draw circle from start to end." 
    up()
    goto(start.x, start.y)
    down()
    circle (end.x - start.x)
    end_fill


def rectangle(start, end):#Funcion que hace un rectangulo
    "Draw rectangle from start to end."
    forward(100)
    left(90)
    forward(50)
    left(90)
    forward(100)
    left(90)
    forward(50)
    left(90)


def triangle(start, end):#Funcion que hace un triangulo
    "Draw triangle from start to end."
    forward(100)
    left(120)
    forward(100)
    left(120)
    forward(100)
    left(150)

def tap(x, y):#Funcion del punto de inicio y la forma que se hara
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x,y)
    else: 
        shape = state['shape']
        end = vector(x,y)
        shape(start,end)
        state['start'] = None

def store (key, value):
    "Store value in state at key"
    state[key] = value 
    

#LLamado de las funciones
state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K') 
onkey(lambda: color('white'), 'W') 
onkey(lambda: color('green'), 'G') 
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')  
onkey(lambda: color('pink'), 'P')  
onkey(lambda: store('shape', line), 'l') 
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circles), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()    
