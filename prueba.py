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


lista1 = ["Confesar", "No confesar", "No confesar", "Confesar", "No confesar", "Confesar", "Confesar", "Confesar", "No confesar", "Confesar"]
lista2 = ["Confesar", "Confesar", "No confesar", "No confesar", "Confesar", "Confesar", "Confesar", "No confesar", "Confesar", "Confesar"]
def tree(lista1, lista2):
    canvas.delete(ALL)
    canvas.configure(background = colorbk)  # se configura el color de la pantalla
    canvas.pack()
    wid1 = width/4
    wid2 = 3*wid1


    if len(lista1) < 6:
        x = width/(4*len(lista1) + 2)
        heig = height/(len(lista1) + 2)
        canvas.create_rectangle(wid1 - 50, heig -15,wid1 + 50, heig +15, fill = "white", width = 2)
        canvas.create_text(wid1, heig, anchor = CENTER,text = 'Prisionero 1', fill = "black",font =(Font , 13,"bold"))
        canvas.create_rectangle(wid2 - 50, heig -15,wid2 + 50, heig +15, fill = "white", width = 2)
        canvas.create_text(wid2, heig, anchor = CENTER, text = 'Prisionero 2', font =(Font , 13, "bold"))
    else:
        x = width/(2.2*len(lista1))
        heig = height/(len(lista1) + 5)
        canvas.create_rectangle(wid1 - 50, heig -15,wid1 + 50, heig +15, fill = "white", width = 2)
        canvas.create_text(wid1, heig, anchor = CENTER,text = 'Prisionero 1', fill = "black",font =(Font , 13,"bold"))
        canvas.create_rectangle(wid2 - 50, heig -15,wid2 + 50, heig +15, fill = "white", width = 2)
        canvas.create_text(wid2, heig, anchor = CENTER, text = 'Prisionero 2', font =(Font , 13, "bold"))

    recursion(lista1, lista2, wid1, wid2, heig, x)

def recursion(lista1, lista2, wid1,wid2, heig, x):
    n = len(lista1)
    if n==0:
        print("hola")
    else:
        heig1 = heig + 45
        if lista1[0] == "Confesar":
            canvas.create_line(wid1, heig+15, wid1 - x, heig1, width = 2)
            canvas.create_line(wid1, heig + 15, wid1 + x, heig1, width = 2)
            canvas.create_oval(wid1 -x -30,heig1 - 15, wid1 -x + 30, heig1+15, fill = "RoyalBlue1", width = 2)
            canvas.create_oval(wid1 + x -40,heig1 - 15, wid1 +x +40, heig1+15, fill = "white", width = 2)
            canvas.create_text(wid1 - x, heig1, anchor = CENTER, text = 'Confesar', font =(Font, 10, "bold"))
            canvas.create_text(wid1 + x, heig1, anchor = CENTER, text = 'No confesar', font =(Font , 10, "bold"))
            wid1 = wid1 - x
        else:
            canvas.create_line(wid1, heig + 15, wid1 - x, heig1, width = 2)
            canvas.create_line(wid1, heig + 15, wid1 + x, heig1, width = 2)
            canvas.create_oval(wid1 -x -30,heig1 - 15, wid1 -x + 30, heig1+15, fill = "white", width = 2)
            canvas.create_oval(wid1 + x -40,heig1 - 15, wid1 +x +40, heig1+15, fill = "firebrick1", width= 2)
            canvas.create_text(wid1 - x, heig1, anchor = CENTER, text = 'Confesar', font =(Font , 10, "bold"))
            canvas.create_text(wid1 + x, heig1, anchor = CENTER, text = 'No confesar', font =(Font , 10, "bold"))
            wid1 = wid1 + x
        if lista2[0] == "Confesar":
            canvas.create_line(wid2, heig + 15, wid2 - x, heig1, width = 2 )
            canvas.create_line(wid2, heig+ 15, wid2+ x, heig1, width = 2)
            canvas.create_oval(wid2 -x -30,heig1 - 15, wid2 -x + 30, heig1+15, fil = "RoyalBlue1", width = 2)
            canvas.create_oval(wid2 + x -40,heig1 - 15, wid2 +x +40, heig1+15, fill = "white", width = 2)
            canvas.create_text(wid2 - x, heig1, anchor= CENTER, text = 'Confesar', font =(Font , 10, "bold"))
            canvas.create_text(wid2 + x, heig1, anchor = CENTER,text = 'No confesar', font =(Font , 10, "bold") )
            wid2 = wid2 - x
        else:
            canvas.create_line(wid2, heig +15, wid2 - x, heig1, width = 2)
            canvas.create_line(wid2, heig + 15, wid2+ x, heig1, width = 2)
            canvas.create_oval(wid2 -x -30,heig1 - 15, wid2 -x + 30, heig1+15, fill = "white", width = 2)
            canvas.create_oval(wid2 + x -40,heig1 - 15, wid2 +x +40, heig1+15, fill = "firebrick1", width = 2)
            canvas.create_text(wid2 - x, heig1, anchor= CENTER, text = 'Confesar', font =(Font , 10, "bold"))
            canvas.create_text(wid2 + x, heig1, anchor = CENTER,text = 'No confesar', font =(Font , 10, "bold") )
            wid2 = wid2 + x
            x = 0.95*x
        del(lista1[0])
        del(lista2[0])
        recursion(lista1, lista2, wid1, wid2, heig1, x)

tree(lista1, lista2)

root.mainloop()
