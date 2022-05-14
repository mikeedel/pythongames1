from random import *
from turtle import *
from freegames import path

"Importamos los módulos" 

"Colocamos la pantalla"
screen = Screen()
 
"Escoger el color del fondo"
screen.bgcolor("blue")


"Se define la funcion para crear la seccion de cuadros dentro del juego"
def Square(x, y):
    up()
    goto(x, y)
    down()
    color('white', 'yellow')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()
 "Se determina el rango del tablero, como tambien el color"

"Definir el conteo para mantener el numero indice"
def Numbering(x, y):
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)
 
def Coordinates(count):
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200
 
 
 "Se define la funcion para hacer que el usuario pueda hacer click"
def click(x, y):
    spot = Numbering(x, y)
    mark = state['mark']
 
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
 "Determinamos el numero de veces que se da click y que si es una respuesta incorrecta, este vuelva a ocultar donde se dio click"
 
def draw():
    clear()
    goto(0, 0)
    stamp()
 
    for count in range(64):
        if hide[count]:
            x, y = Coordinates(count)
            Square(x, y)
 
    mark = state['mark']
 
    if mark is not None and hide[mark]:
        x, y = Coordinates(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))
 
    update()
    ontimer(draw, 10)
 
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
 
"Usamos lo siguienre para barajar los cuadros a seleccionar" 
shuffle(tiles)
tracer(False)
onscreenclick(click)
draw()
done()
