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
    wid1 = width/4
    heig = height/(len(lista1) + 2)
    wid2 = 3*wid1
    canvas.create_rectangle(wid1 - 50, heig -17,wid1 + 50, heig +17, fill = "white")
    canvas.create_text(wid1, heig, anchor = CENTER,text = 'Prisionero 1', fill = "black",font =(Font , 12))
    canvas.create_rectangle(wid2 - 50, heig -17,wid2 + 50, heig +17, fill = "white")
    canvas.create_text(wid2, heig, anchor = CENTER, text = 'Prisionero 2', font =(Font , 12))
    x = width/(3.8*len(lista1) + 1)
    recursion(lista1, lista2, wid1, wid2, heig, x)


def recursion(lista1, lista2, wid1,wid2, heig, x):
    n = len(lista1)
    if n==0:
        print("hola")
    else:
        heig1 = heig + 50

        if lista1[0] == "Confesar":
            canvas.create_line(wid1, heig+15, wid1 - x, heig1)
            canvas.create_line(wid1, heig + 15, wid1 + x, heig1)
            canvas.create_oval(wid1 -x -30,heig1 - 15, wid1 -x + 30, heig1+15, fill = "blue")
            canvas.create_oval(wid1 + x -40,heig1 - 15, wid1 +x +40, heig1+15)
            canvas.create_text(wid1 - x, heig1, anchor = CENTER, text = 'Confesar', font =(Font , 10))
            canvas.create_text(wid1 + x, heig1, anchor = CENTER, text = 'No confesar', font =(Font , 10))
            wid1 = wid1 - x
        else:
            canvas.create_line(wid1, heig + 15, wid1 - x, heig1)
            canvas.create_line(wid1, heig + 15, wid1 + x, heig1)
            canvas.create_oval(wid1 -x -30,heig1 - 15, wid1 -x + 30, heig1+15)
            canvas.create_oval(wid1 + x -40,heig1 - 15, wid1 +x +40, heig1+15)
            canvas.create_text(wid1 - x, heig1, anchor = CENTER, text = 'Confesar', font =(Font , 10))
            canvas.create_text(wid1 + x, heig1, anchor = CENTER, text = 'No confesar', font =(Font , 10))
            wid1 = wid1 + x
        if lista2[0] == "Confesar":
            canvas.create_line(wid2, heig + 15, wid2 - x, heig1)
            canvas.create_line(wid2, heig+ 15, wid2+ x, heig1)
            canvas.create_oval(wid2 -x -30,heig1 - 15, wid2 -x + 30, heig1+15)
            canvas.create_oval(wid2 + x -40,heig1 - 15, wid2 +x +40, heig1+15)
            canvas.create_text(wid2 - x, heig1, anchor= CENTER, text = 'Confesar', font =(Font , 10))
            canvas.create_text(wid2 + x, heig1, anchor = CENTER,text = 'No confesar', font =(Font , 10) )
            wid2 = wid2 - x
        else:
            canvas.create_line(wid2, heig +15, wid2 - x, heig1)
            canvas.create_line(wid2, heig + 15, wid2+ x, heig1)
            canvas.create_oval(wid2 -x -30,heig1 - 15, wid2 -x + 30, heig1+15)
            canvas.create_oval(wid2 + x -40,heig1 - 15, wid2 +x +40, heig1+15)
            canvas.create_text(wid2 - x, heig1, anchor= CENTER, text = 'Confesar', font =(Font , 10))
            canvas.create_text(wid2 + x, heig1, anchor = CENTER,text = 'No confesar', font =(Font , 10) )
            wid2 = wid2 + x
            x = 0.95*x
        del(lista1[0])
        del(lista2[0])
        recursion(lista1, lista2, wid1, wid2, heig1, x)

tree(lista1, lista2)

root.mainloop()
