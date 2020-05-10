from tkinter import *
import random

root = Tk()
width = 800
height = 600
size = 40
size2 = 23
root.resizable (0,0)
Font = 'Agency FB'
root.title("El dilema del prisionero")
canvas = Canvas(root, width = width, height = height)
optionslist = ["Aleatorio", "Confesar", "No Confesar"]
colorbk = '#28EEAF'
player1 = StringVar()
player2 = StringVar()
puntos1 = 2
puntos2 = 2
var_list1 = []
var_list2 = []
puntos1_list = []
puntos1_list2 = []
puntos2_list = []
puntos2_list2 = []


def aleatorio (player):
    if (player == optionslist[0]):
        bool = probability(0.5)
        if (bool == False):
            player = optionslist[-1]
        else:
            player = optionslist[-2]
    return player

def game(player1, player2, number):
    global var_list1
    global var_list2
    canvas.delete("all")
    if (player1 == ''):
        player1 = optionslist[0]
    if (player2 == ''):
        player2 = optionslist[0]

    if (player1 == optionslist[0]):
        player1 = aleatorio (player1)
    if (player2 == optionslist[0]):
        player2 = aleatorio (player2)

    var_list2.append(player2)
    var_list1.append(player1)
    jugador(player1, player2, number)
    back = Button(root, text = "Volver", width = int(width/100), command = lambda: inicio(), font = (Font, 20) )
    next = Button(root, text = "Siguiente", width = int(width/100), command = lambda: resultados(number), font = (Font, 20))
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
        if (puntos1 == 0 or puntos2 == 0):
            break
        decision(number, i, player1, player2)


def puntuation(i, var, h_tot, number, player2, boton):
    global var_list1, puntos1, puntos2, puntos2_list, puntos1_list
    if (i != 0):
        var_list1.append(var)
    cpu(i, player2, number)
    if (var == optionslist[0] and var_list2[i] == optionslist[1]):
        puntos1 -= 1
        puntos2 += 5
        puntos1_list2.append(puntos1 + 1)
        puntos2_list2.append(puntos2 - 4)
    elif (var == optionslist[1] and var_list2[i] == optionslist[0]):
        puntos1 += 5
        puntos2 -= 1
        puntos1_list2.append(puntos1 - 4)
        puntos2_list2.append(puntos2 + 1)
    elif (var == optionslist[0] and var_list2[i] == optionslist[0]):
        puntos1 += 1
        puntos2 += 1
        puntos1_list2.append(puntos1 + 4)
        puntos2_list2.append(puntos2 + 4)
    elif (var == optionslist[1] and var_list2[i] == optionslist[1]):
        puntos1 += 0
        puntos2 += 0
        puntos1_list2.append(puntos1 - 1)
        puntos2_list2.append(puntos2 - 1)
    puntos2_list.append(puntos2)
    puntos1_list.append(puntos1)
    canvas.create_text(27*width/32, h_tot , anchor = CENTER, text = str(puntos1) + ' año(s)', font =(Font , size-2*number))

def decision(number, i, player1, player2):
    var = StringVar()
    h = height - height/5
    h_tot = (i+1)*h/(number+h/150) + height/4
    canvas.create_text(3*width/16, h_tot , anchor = CENTER, text = 'Decisión\t ' + str(i+1) + ': ', font =(Font , size-2*number))
    options = OptionMenu(root, var, *optionslist)
    options.config(font=(Font , size2 - number),bg='white', width=12)
    canvas.create_window(width/2, h_tot, window = options, width = width/4)
    if (i == 0):
        var.set(player1)
        options.config(state = DISABLED)

    boton = Button(root, text = "->", width = int(width/100), command = lambda: puntuation(i, var.get(), h_tot, number, player2, boton), font = (Font , int(size2 - number)))
    canvas.create_window(11*width/16, h_tot, window = boton)


def resultados (number):
    canvas.delete("all")
    back = Button(root, text = "Inicio", width = int(width/100), command = lambda: inicio(), font = (Font, 20) )
    next = Button(root, text = "Siguiente", width = int(width/100), command = lambda: tree(), font = (Font, 20))
    canvas.create_window(6*width/8, 17*height/128, window = next)
    canvas.create_window(2*width/8, 17*height/128, window = back)
    canvas.create_text(width/2, height/8, anchor = CENTER, text = 'Resultados', font =(Font , size))
    canvas.create_line(0, height/5, width, height/5)
    canvas.create_line(0, height/16, width, height/16)
    canvas.create_line(width/2, height/5, width/2, height)
    canvas.create_text(width/32, height/5, anchor = NW, text = 'Prisionero 1', font =(Font , size - number))
    canvas.create_text(5*width/16, height/5, anchor = NW, text = 'Condena', font =(Font , size - number), fill = "#891C1C")
    canvas.create_text(17*width/32, height/5, anchor = NW, text = 'Prisionero 2', font =(Font , size - number))
    canvas.create_text(13*width/16, height/5, anchor = NW, text = 'Condena', font =(Font , size - number), fill = "#891C1C")
    for i in range (number):
        h = height - height/5
        h_tot = (i+1)*h/(number+h/150) + height/4
        canvas.create_text(5*width/32, h_tot , anchor = CENTER, text = var_list1[i], font =(Font , size-2*number))
        canvas.create_text(6*width/16, h_tot , anchor = CENTER, text = puntos1_list[i], font =(Font , size-2*number), fill = "#891C1C")
        canvas.create_text(21*width/32, h_tot , anchor = CENTER, text = var_list2[i], font =(Font , size-2*number))
        canvas.create_text(14*width/16, h_tot , anchor = CENTER, text = puntos2_list[i], font =(Font , size-2*number), fill = "#891C1C")


def tree(wid1 = width/4, wid2 = 3*width/4):
    canvas.delete("all")
    canvas.configure(background = colorbk)  # se configura el color de la pantalla
    canvas.pack()
    canvas.create_line(0, height/5, width, height/5)
    canvas.create_line(0, height/16, width, height/16)
    back = Button(root, text = "Inicio", width = int(width/100), command = lambda: inicio(), font = (Font, 20) )
    next = Button(root, text = "Cerrar", width = int(width/100), command = lambda: close_window(), font = (Font, 20))
    canvas.create_window(6*width/8, 17*height/128, window = next)
    canvas.create_window(2*width/8, 17*height/128, window = back)
    canvas.create_text(width/2, height/8, anchor = CENTER, text = 'Resultados', font =(Font , size))

    if (len(var_list1) < 20):
        x = width/(4*len(var_list1) + 2)
        heig = height/(len(var_list1) + 2) + height/5
        canvas.create_rectangle(wid1 - 50, heig -10,wid1 + 50, heig +10, fill = colorbk, width = 2)
        canvas.create_text(wid1, heig, anchor = CENTER,text = 'Prisionero 1', fill = "black",font =(Font , 13,"bold"))
        canvas.create_rectangle(wid2 - 50, heig -10,wid2 + 50, heig +10, fill = colorbk, width = 2)
        canvas.create_text(wid2, heig, anchor = CENTER, text = 'Prisionero 2', font =(Font , 13, "bold"))
    else:
        x = width/(2.2*len(var_list1))
        heig = height/(len(var_list1) + 5) + height/5
        canvas.create_rectangle(wid1 - 50, heig -10,wid1 + 50, heig +10, fill = colorbk, width = 2)
        canvas.create_text(wid1, heig, anchor = CENTER,text = 'Prisionero 1', fill = "black",font =(Font , 13,"bold"))
        canvas.create_rectangle(wid2 - 50, heig -10,wid2 + 50, heig +10, fill = colorbk, width = 2)
        canvas.create_text(wid2, heig, anchor = CENTER, text = 'Prisionero 2', font =(Font , 13, "bold"))

    recursion(wid1, wid2, heig, x)


def recursion(wid1,wid2, heig, x):
    global var_list1, var_list2, puntos1_list, puntos2_list, puntos1_list2, puntos2_list2
    n = len(var_list1)
    check = "#33E3E0"
    negrita = "bold"
    bool = True
    if n !=0:
        heig1 = heig + 45
        if (bool):
            # Prisionero 1
            canvas.create_line(wid1, heig + 10, wid1 - x, heig1, width = 2)
            canvas.create_line(wid1, heig + 10, wid1 + x, heig1, width = 2)
            canvas.create_oval(wid1 - x/2 -5, (heig+10 + heig1)/2 - 5, wid1 -x/2 +5, (heig+15 + heig1)/2 + 5, fill = colorbk, outline = colorbk)
            canvas.create_oval(wid1 + x/2 -5, (heig+10 + heig1)/2 - 5, wid1 + x/2 +5, (heig+15 + heig1)/2 + 5, fill = colorbk, outline = colorbk)
            canvas.create_text((2*wid1 - x)/2, (heig+10 + heig1)/2,  anchor = CENTER, text = "Sí", font = (Font , 10, negrita))
            canvas.create_text((2*wid1 + x)/2, (heig+10 + heig1)/2,  anchor = CENTER, text = "No", font = (Font , 10, negrita))
            if var_list1[0] == optionslist[-2]:
                # Si la decisión Confiesa
                canvas.create_rectangle(wid1 -x -10,heig1 - 10, wid1 -x + 10, heig1+10, fill = check, width = 2)
                canvas.create_oval(wid1 + x -10,heig1 - 10, wid1 +x +10, heig1+10, fill = colorbk, width = 2)
                canvas.create_text(wid1 - x, heig1, anchor = CENTER, text = str(puntos1_list[0]), font =(Font, 15))
                canvas.create_text(wid1 + x, heig1, anchor = CENTER, text = str(puntos1_list2[0]), font =(Font , 15))
                wid1 = wid1 - x
            else:
                # Si la decisión Confiesa
                canvas.create_oval(wid1 -x -10,heig1 - 10, wid1 -x + 10, heig1+10, fill = colorbk, width = 2)
                canvas.create_rectangle(wid1 + x -10,heig1 - 10, wid1 +x +10, heig1+10, fill = check, width= 2)
                canvas.create_text(wid1 - x, heig1, anchor = CENTER, text = str(puntos1_list2[0]), font =(Font , 15))
                canvas.create_text(wid1 + x, heig1, anchor = CENTER, text = str(puntos1_list[0]), font =(Font , 15))
                wid1 = wid1 + x
            bool = False
        if(bool == False):
            # Prisionero 2
            canvas.create_line(wid2, heig + 10, wid2 - x, heig1, width = 2 )
            canvas.create_line(wid2, heig+ 10, wid2+ x, heig1, width = 2)
            canvas.create_oval(wid2 - x/2 -5, (heig+10 + heig1)/2 -5, wid2 -x/2 +5, (heig+15 + heig1)/2 + 5, fill = colorbk, outline = colorbk)
            canvas.create_oval(wid2 + x/2 -5, (heig+10 + heig1)/2 -5, wid2 + x/2 +5, (heig+15 + heig1)/2 + 5, fill = colorbk, outline = colorbk)
            canvas.create_text((2*wid2 - x)/2, (heig+10 + heig1)/2,  anchor = CENTER, text = "Sí", font =(Font , 10, negrita))
            canvas.create_text((2*wid2 + x)/2, (heig+10 + heig1)/2,  anchor = CENTER, text = "No", font =(Font , 10, negrita))
            if var_list2[0] == optionslist[-2]:
                # Si la decisión es Confiesa
                canvas.create_rectangle(wid2 -x -10,heig1 - 10, wid2 -x + 10, heig1+10, fill = check, width = 2)
                canvas.create_oval(wid2 + x -10,heig1 - 10, wid2 +x +10, heig1+10, fill = colorbk, width = 2)
                canvas.create_text(wid2 - x, heig1, anchor= CENTER, text = str(puntos2_list[0]), font =(Font , 15))
                canvas.create_text(wid2 + x, heig1, anchor = CENTER,text = str(puntos2_list2[0]), font =(Font , 15) )
                wid2 = wid2 - x
            else:
                # Si la decisión es No Confiesa
                canvas.create_oval(wid2 -x -10,heig1 - 10, wid2 -x + 10, heig1+10, fill = colorbk, width = 2)
                canvas.create_rectangle(wid2 + x -10,heig1 - 10, wid2 +x +10, heig1+10, fill = check, width = 2)
                canvas.create_text(wid2 - x, heig1, anchor= CENTER, text = str(puntos2_list2[0]), font =(Font , 15))
                canvas.create_text(wid2 + x, heig1, anchor = CENTER,text = str(puntos2_list[0]), font =(Font , 15) )
                wid2 = wid2 + x
                x = 0.95*x


        del(var_list1[0])
        del(var_list2[0])
        del(puntos2_list[0])
        del(puntos1_list[0])
        del(puntos2_list2[0])
        del(puntos1_list2[0])
        recursion(wid1, wid2, heig1, x)

def close_window():
    root.destroy()

def maximizar(number):
    list2 = []
    if (number == 1):
        list = [(puntos1 + 1, puntos1 + 1), (puntos1 - 1, puntos1 + 5), (puntos1 + 5, puntos1 - 1), (puntos1, puntos1)]
        return list
    else:
        list = maximizar(number - 1)
        for i in range (len(list)):
            list2.append((list[i][0] + 1, list[i][1] + 1))
        for i in range (len(list)):
            list2.append((list[i][0] - 1, list[i][1] + 5))
        for i in range (len(list)):
            list2.append((list[i][0] + 5, list[i][1] - 1))
        for i in range (len(list)):
            list2.append(list[i])
        return list2

def decision_tree (number):
    canvas.delete("all")
    back = Button(root, text = "Inicio", width = int(width/100), command = lambda: inicio(), font = (Font, 20) )
    canvas.create_window(width/8, 17*height/128, window = back)
    next = Button(root, text = "Cerrar", width = int(width/100), command = lambda: close_window(), font = (Font, 20))
    canvas.create_window(6*width/8, 17*height/128, window = next)

    canvas.create_text(width/2, height/8, anchor = CENTER, text = 'Árbol de decisión', font =(Font , size))
    canvas.create_line(0, height/5, width, height/5)
    canvas.create_line(0, height/16, width, height/16)

    list = maximizar(number)

    number = 2*number
    wid1 = width/2
    if (number < 20):
        x = width/(3*number)
        heig = height/(number + 2) + height/5
        canvas.create_text(wid1, heig, anchor = CENTER,text = 'P1', fill = "black",font =(Font , 13,"bold"))

    else:
        x = width/(2.2*number)
        heig = height/(number + 5) + height/5
        canvas.create_text(wid1, heig, anchor = CENTER,text = 'P1', fill = "black",font =(Font , 13,"bold"))
    number -= 1
    dib_arb(wid1, heig, 'P1', number, x)


def dib_arb(wid1,heig, pri, number, x):
    heig1= heig + 45
    if (number != 0):
        if (pri == 'P1'):
            canvas.create_line(wid1, heig + 15, wid1 - x, heig1, width = 2)
            canvas.create_line(wid1, heig + 15, wid1 + x, heig1, width = 2)
            canvas.create_text(wid1 - x, heig1, anchor = CENTER, text = 'P2', fill = 'black', font =(Font, 13, "bold"))
            canvas.create_text(wid1 + x , heig1, anchor = CENTER, text = 'P2', fill = 'black', font =(Font, 13, "bold"))
            pri = 'P2'
        else:
            canvas.create_line(wid1, heig + 15, wid1 - x, heig1, width = 2)
            canvas.create_line(wid1, heig + 15, wid1 + x, heig1, width = 2)
            canvas.create_text(wid1 - x, heig1, anchor = CENTER, text = 'P1', fill = 'black', font =(Font, 13, "bold"))
            canvas.create_text(wid1 + x, heig1,anchor = CENTER, text = 'P1', fill = 'black', font =(Font, 13, "bold"))
            pri = 'P1'
        wid2 = wid1 - x
        wid3 =wid1 + x
        x = 0.8*x
        number-=1
        dib_arb(wid2, heig1,pri, number, x)
        dib_arb(wid3,heig1, pri, number, x)



def nash(number):
    global var_list1, var_list2, puntos1_list, puntos2_list, puntos1_list2, puntos2_list2
    for i in range (number):
        var_list1.append(optionslist[-1])
        var_list2.append(optionslist[-1])
        puntos1_list.append(puntos1)
        puntos2_list.append(puntos2)
        puntos1_list2.append(puntos1 + 5)
        puntos2_list2.append(puntos2 + 5)
    resultados(number)

def inicio():
    global var_list1, var_list2, puntos1, puntos2, puntos1_list, puntos2_list, puntos1_list2, puntos2_list2
    var_list1 = []
    var_list2 = []
    optionslist = ["Aleatorio", "Confesar", "No Confesar"]
    puntos1 = 2
    puntos2 = 2
    puntos1_list = []
    puntos2_list = []
    puntos1_list2 = []
    puntos2_list2 = []

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
    max = Button(root, text = "Árbol de decisión", width = int(width/50), command = lambda: decision_tree(number.get()), font = (Font, 20))
    canvas.create_window(width/8, 7*height/8, window = max)
    eqnash = Button(root, text = "Equilibrio de Nash", width = int(width/50), command = lambda: nash(number.get()), font = (Font, 20))
    canvas.create_window(width/2, 7*height/8, window = eqnash)

inicio()
root.mainloop()
