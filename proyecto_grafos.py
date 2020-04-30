from tkinter import *
import random

root = Tk()
width = 800
height = 500
size = 40
size2 = 23
root.resizable (0,0)
Font = 'Agency FB'
root.title("El dilema del prisionero")
canvas = Canvas(root, width = width, height = height)
optionslist = ["Aleatorio", "Confesar", "No Confesar"]
colorbk = '#28EEAF'
puntos1 = 2
puntos2 = 2
var_list1 = []
var_list2 = []
puntos1_list = []
puntos1_list2 = []
puntos2_list = []
puntos2_list2 = []


def game(player1, player2, number):
    global var_list1
    global var_list2

    canvas.delete("all")
    if (player1 == ''):
        player1 = optionslist[0]
    if (player2 == ''):
        player2 = optionslist[0]

    if (player1 == optionslist[0]):
        bool = probability(0.5)
        if (bool == False):
            player1 = optionslist[-1]
        else:
            player1 = optionslist[-2]

    if (player2 == optionslist[0]):
        bool = probability(0.5)
        if (bool == False):
            player2 = optionslist[-1]
        else:
            player2 = optionslist[-2]

    var_list2.append(player2)
    var_list1.append(player1)
    jugador(player1, player2, number)
    back = Button(root, text = "Volver", width = int(width/100), command = lambda: inicio(), font = (Font, 20) )
    next = Button(root, text = "Siguiente", width = int(width/100), command = lambda: end(number), font = (Font, 20))
    canvas.create_window(6*width/8, 17*height/128, window = next)
    canvas.create_window(2*width/8, 17*height/128, window = back)

def probability(prob):
    num_aleatory = random.uniform(0, 1)
    if (num_aleatory < prob):
        return False
    else:
        return True

def cpu(i, player2, number):
    global var_list2
    global var_list1
    if (i < number-1):
        if (var_list2[i] == var_list1[i]):
            prob = 0.5
        elif (var_list2[i] == optionslist[-1] and var_list1[i] == optionslist[-2]):
            prob = 0.2
        else:
            prob = 0.4
        bool =probability(prob)
        if (bool == False):
            var_list2.append(optionslist[1])
        else:
            var_list2.append(optionslist[0])


def jugador(player1, player2, number):
    global optionslist
    if (len(optionslist) == 3):
        optionslist.pop(0)
    canvas.create_text(width/2, height/8, anchor = CENTER, text = 'Prisionero 1', font =(Font , size))
    canvas.create_line(width/8, height/5, 7*width/8, height/5)
    canvas.create_line(width/8, height/16, 7*width/8, height/16)
    canvas.create_text(3*width/4, height/5, anchor = NW, text = 'Condena', font =(Font , size - number))
    for i in range(number):
        decision(number, i, player1, player2)


def puntuation(i, var, h_tot, number, player2, boton):
    global var_list1
    global puntos1
    global puntos2
    global puntos2_list
    global puntos1_list
    if (i != 0):
        var_list1.append(var)
    cpu(i, player2, number)
    print("Var: ", var)
    if (var == optionslist[0] and var_list2[i] == optionslist[1]):
        puntos1 -= 1
        puntos2 += 5
    elif (var == optionslist[1] and var_list2[i] == optionslist[0]):
        puntos1 += 5
        puntos2 -= 1
    elif (var == optionslist[0] and var_list2[i] == optionslist[0]):
        puntos1 += 1
        puntos2 += 1

    puntos2_list.append(puntos2)
    puntos1_list.append(puntos1)

    canvas.create_text(27*width/32, h_tot , anchor = CENTER, text = str(puntos1) + ' año(s)', font =(Font , size-2*number))

def decision(number, i, player1, player2):
    var = StringVar()
    h = height - height/5
    h_tot = (i+1)*h/(number+h/150) + height/4
    canvas.create_text(3*width/16, h_tot , anchor = CENTER, text = 'Decisión\t ' + str(i+1) + ': ', font =(Font , size-4*number))
    options = OptionMenu(root, var, *optionslist)
    options.config(font=(Font , size-4*number),bg='white', width=12)
    canvas.create_window(width/2, h_tot, window = options, width = width/4)
    if (i == 0):
        var.set(player1)
        options.config(state = DISABLED)

    boton = Button(root, text = "->", width = int(width/100), command = lambda: puntuation(i, var.get(), h_tot, number, player2, boton), font = (Font , int(size2 - number)))
    canvas.create_window(11*width/16, h_tot, window = boton)


def Nodo (Nombre,x,y,size):
    # canvas.create_oval(x-(size/2),y,x+(size/2),y+size)
    # canvas.create_window(x,y+(size/2),anchor = CENTER,window = Label(root,text = Nombre))
    # root.update()

def Arista (Nombre,x1,y1,x2,y2):
    # canvas.create_line(x1,y1,x2,y2)
    # canvas.create_window(x2+((x1-x2)/2),y2+((y1-y2)/2),anchor = CENTER,window = Label(root,text = Nombre,bg = "white",fg="red"))
    # canvas.create_oval(x1-5,y1-5,x1+5,y1+5,fill = 'black')
    # root.update()

def Tree (puntos1_list, number):
    tg


def end(number):
    canvas.delete("all")

def inicio():
    global var_list1
    global var_list2
    global puntos1
    global puntos2
    var_list1 = []
    var_list2 = []
    optionslist = ["Aleatorio", "Confesar", "No Confesar"]
    puntos1 = 2
    puntos2 = 2
    puntos1_list = [2]
    puntos2_list = [2]


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
