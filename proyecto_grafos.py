from tkinter import *
import time

root = Tk()
width = 800
height = 500
size = 40
root.resizable (0,0)
Font = 'Agency FB'
root.title("El dilema del prisionero")
canvas = Canvas(root, width = width, height = height)
optionslist = ["Aleatorio", "Confesar", "No Confesar"]
colorbk = '#28EEAF'
puntos1 = 2
puntos2 = 2
var_list1 = []
# var = StringVar()

# def cpu()

def game(player1, player2, number):
    canvas.delete("all")
    if (player1 == ''):
        player1 = optionslist[0]
    if (player2 == ''):
        player2 = optionslist[0]

    jugador(player1, number)
    back = Button(root, text = "Volver", width = int(width/100), command = lambda: inicio(), font = (Font, 20) )
    next = Button(root, text = "Siguiente", width = int(width/100), command = lambda: end(), font = (Font, 20))
    canvas.create_window(6*width/8, 17*height/128, window = next)
    canvas.create_window(2*width/8, 17*height/128, window = back)


def jugador(player1, number):
    global optionslist
    optionslist.pop(0)
    canvas.create_text(width/2, height/8, anchor = CENTER, text = 'Prisionero 1', font =(Font , size))
    canvas.create_line(width/8, height/5, 7*width/8, height/5)
    canvas.create_line(width/8, height/16, 7*width/8, height/16)
    canvas.create_text(3*width/4, height/5, anchor = NW, text = 'Condena', font =(Font , size - number))
    for i in range(number):
        decision(number, i, player1)

def puntuation(var, h_tot, number):
    global var_list1
    global puntos1
    var_list1.append(var)
    if (var == optionslist[0]):
        puntos1 += 10
    elif (var == optionslist[1]):
        puntos1 += 20
    canvas.create_text(27*width/32, h_tot , anchor = CENTER, text = str(puntos1) + ' años', font =(Font , size-2*number))


def decision(number, i, player1):
    var = StringVar()
    h = height - height/5
    h_tot = (i+1)*h/(number+h/150) + height/4
    canvas.create_text(3*width/16, h_tot , anchor = CENTER, text = 'Decisión\t ' + str(i+1) + ': ', font =(Font , size-2*number))
    options = OptionMenu(root, var, *optionslist)
    options.config(font=(Font,(18)),bg='white',width=12)
    canvas.create_window(width/2, h_tot, window = options, width = width/4)
    if (i == 0):
        var.set(player1)
        options.config(state = DISABLED)

    boton = Button(root, text = "->", width = int(width/100), command = lambda: puntuation(var.get(), h_tot, number), font = (Font, 15))
    canvas.create_window(11*width/16, h_tot, window = boton)


def Nodo():
    rg

def Arista():
    gr

def tree():
    rg

def end():
    print(var_list)

def inicio():
    canvas.delete("all")
    player1 = StringVar()
    player2 = StringVar()
    number = IntVar(value = 1)

    canvas.configure(background = colorbk)  # se configura el color de la pantalla
    canvas.pack()
    canvas.create_text(width/4, height/8, anchor = NW, text = 'El dilema del prisionero', font =(Font , size))
    canvas.create_line(width/8, height/4, 7*width/8, height/4)
    canvas.create_line(width/8, height/8, 7*width/8, height/8)

    canvas.create_text(width/8, 5*height/16, anchor = NW, text = 'Elija la primera decisión de cada prisionero.', font =(Font , 25))
    canvas.create_text(width/8, 4*height/8, anchor = NW, text = 'Prisionero 1:', font =(Font , 25))
    canvas.create_text(width/8, 5*height/8, anchor = NW, text = 'Prisionero 2:', font =(Font , 25))
    canvas.create_text(width/8, 6*height/8, anchor = NW, text = 'Ingrese el número de veces a realizar:', font =(Font, 25))

    options = OptionMenu(root, player1, *optionslist)
    options.config(font=(Font,(18)),bg='white',width=12)
    options2 = OptionMenu(root, player2, *optionslist)
    options2.config(font=(Font,(18)),bg='white',width=12)
    canvas.create_window(7*width/16, 4*height/8 + 20, window = options, width = width/4)
    canvas.create_window(7*width/16, 5*height/8 + 20, window = options2, width = width/4)
    entry = Entry(root, textvariable = number, width = int(width/128), font = (Font, 20), justify = CENTER)
    canvas.create_window(11*width/16, 6*height/8 + 25, anchor = CENTER, window = entry)

    next = Button(root, text = "Siguiente", width = int(width/100), command = lambda: game(player1.get(), player2.get(), number.get()), font = (Font, 20))
    canvas.create_window(7*width/8, 7*height/8, window = next)



inicio()
root.mainloop()
