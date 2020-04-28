from tkinter import *

root = Tk()
width = 800
height = 500
root.resizable (0,0)
Font = 'Agency FB'
root.title("El dilema del prisionero")
canvas = Canvas(root, width = width, height = height)
optionslist = ["Aleatorio", "Confesar", "No Confesar"]


def juego(jugador1, jugador2, entry):
    canvas.delete("all")
    if (jugador1 == ''):
        jugador1 = optionslist[0]
    if (jugador2 == ''):
        jugador2 = optionslist[0]
    print("Jugador 1: ", jugador1)
    print("Jugador 2: ", jugador2)
    print("entry: ", entry)


def inicio():
    jugador1 = StringVar()
    jugador2 = StringVar()
    numero = IntVar(value = 1)

    colorbk = '#28EEAF'  # se configura el color
    canvas.configure(background = colorbk)  # se configura el color de la pantalla
    canvas.pack()
    canvas.create_text(width/4, height/8, anchor = NW, text = 'El dilema del prisionero', font =(Font , 40))
    canvas.create_line(width/8, height/4, 7*width/8, height/4)
    canvas.create_line(width/8, height/8, 7*width/8, height/8)

    canvas.create_text(width/8, 5*height/16, anchor = NW, text = 'Elija la primera decisión de cada prisionero.', font =(Font , 25))
    canvas.create_text(width/8, 4*height/8, anchor = NW, text = 'Prisionero 1:', font =(Font , 25))
    canvas.create_text(width/8, 5*height/8, anchor = NW, text = 'Prisionero 2:', font =(Font , 25))
    canvas.create_text(width/8, 6*height/8, anchor = NW, text = 'Ingrese el número de veces a realizar:', font =(Font, 25))

    options = OptionMenu(root, jugador1, *optionslist)
    # options.config(font=(Font,(12)),bg='white',width=12)
    options2 = OptionMenu(root, jugador2, *optionslist)
    canvas.create_window(7*width/16, 4*height/8 + 20, window = options, width = width/4)
    canvas.create_window(7*width/16, 5*height/8 + 20, window = options2, width = width/4)
    entry = Entry(root, textvariable = numero, width = int(width/64), font = (Font, 20), justify = CENTER)
    canvas.create_window(12*width/16, 6*height/8 + 25, anchor = CENTER, window = entry)

    next = Button(root, text = "Next", width = int(width/100), command = lambda: juego(jugador1.get(), jugador2.get(), entry.get()))
    canvas.create_window(7*width/8, 7*height/8, window = next)



inicio()
root.mainloop()
