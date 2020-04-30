from tkinter import *

root = Tk()
width = 800
height = 500
root.resizable(0,0)
size = 40
root.resizable (0,0)
Font = 'Agency FB'
root.title("El dilema del prisionero")
canvas = Canvas(root, width = width, height = height)
optionslist = ["Aleatorio", "Confesar", "No Confesar"]
colorbk = '#28EEAF'


lista1 = ["Confesar", "No confesar", "Confesar", "No confesar", "Confesar"]
lista2 = ["Confesar", "Confesar", "No confesar", "No confesar", "Confesar", "Confesar"]
def tree(lista1, lista2):
    canvas.delete(ALL)
    canvas.configure(background = colorbk)  # se configura el color de la pantalla
    canvas.pack()
    raiz1 = Label(canvas, text='Prisionero 1', fg='black', bg='white')
    raiz1.pack()
    wid1 = width/4
    heig = height/(len(lista1) + 2)
    wid2 = 3*wid1
    canvas.create_window(wid1, heig, window=raiz1)
    raiz2 = Label(canvas, text='Prisionero 2', fg='black', bg='white')
    raiz2.pack()
    canvas.create_window(wid2, heig, window=raiz2)
    x = width/(3.8*len(lista1) + 1)
    recursion(lista1, lista2, wid1, wid2, heig, x)


def recursion(lista1, lista2, wid1,wid2, heig, x):
    n = len(lista1)
    if n==0:
        print("hola")
    else:
        heig1 = heig + 50

        if lista1[0] == "Confesar":
            yes = Label(canvas, text='Confesar', fg='black', bg='green')
            yes.pack()
            canvas.create_window(wid1 - x, heig1, window=yes)
            canvas.create_line(wid1, heig, wid1 - x, heig1)
            #canvas.create_oval(wid1 - x,heig1, wid1-2*x, 2*heig1)
            no = Label(canvas, text='No confesar', fg='black', bg='white')
            no.pack()
            canvas.create_window(wid1 + x, heig1, window=no)
            canvas.create_line(wid1, heig, wid1 + x, heig1)
            wid1 = wid1 - x
        else:
            yes = Label(canvas, text='Confesar', fg='black', bg='white')
            yes.pack()
            canvas.create_window(wid1 - x, heig1, window=yes)
            canvas.create_line(wid1, heig, wid1 - x, heig1)
            no = Label(canvas, text='No confesar', fg='black', bg='red')
            no.pack()
            canvas.create_window(wid1 + x, heig1, window=no)
            canvas.create_line(wid1, heig, wid1 + x, heig1)
            wid1 = wid1 + x
        if lista2[0] == "Confesar":
            yes1 = Label(canvas, text='Confesar', fg='black', bg='green')
            yes1.pack()
            canvas.create_window(wid2 - x, heig1, window=yes1)
            canvas.create_line(wid2, heig, wid2 - x, heig1)
            no1 = Label(canvas, text='No confesar', fg='black', bg='white')
            no1.pack()
            canvas.create_window(wid2 + x, heig1, window=no1)
            canvas.create_line(wid2, heig, wid2+ x, heig1)
            wid2 = wid2 - x
        else:
            yes1 = Label(canvas, text='Confesar', fg='black', bg='white')
            yes1.pack()
            canvas.create_window(wid2 - x, heig1, window=yes1)
            canvas.create_line(wid2, heig, wid2 - x, heig1)
            no1 = Label(canvas, text='No confesar', fg='black', bg='red')
            no1.pack()
            canvas.create_window(wid2 + x, heig1, window=no1)
            canvas.create_line(wid2, heig, wid2+ x, heig1)
            wid2 = wid2 + x
            x = 0.95*x
        del(lista1[0])
        del(lista2[0])
        recursion(lista1, lista2, wid1, wid2, heig1, x)

tree(lista1, lista2)

root.mainloop()
