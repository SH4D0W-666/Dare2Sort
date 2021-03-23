import tkinter as t
from tkinter import *
from tkinter import ttk
import PIL
from PIL import Image,ImageTk
import time


root= Tk()
blank_space = " "
root.title(140*blank_space+ 'DARE TO SORT')
canvas_width = 1000
canvas_height = 6000
root.geometry(f'{canvas_width}x{canvas_height}')
root.config(bg='#69614c')
can_widget = Canvas(root, width= canvas_width, height=canvas_height,bg="#36332c")
can_widget.place(x=0,y=0)


f1 = Frame(root,borderwidth=6).place(x=0,y=0)
LabelInputtoPop = Label(f1,text="Source Bottle: ",fg='black',font='comicsans 10')
LabelInputtoPush = Label(f1,text="Destination Bottle: ",font='comicsans 10')
LabelInputtoPop.place(x=200,y=10)
LabelInputtoPush.place(x=200,y=40)
popvalue = StringVar()
pushvalue = StringVar()
popEntry = Entry(f1,textvariable=popvalue).place(x=570,y=10)
pushEntry = Entry(f1,textvariable=pushvalue).place(x=570,y=40)

def enter():
    if (popvalue.get() == '1' ):
        note.set('Game on')
        if(len(Atop)==0):
            note.set('Tube 1 is Already Empty')
            print('Already Empty')
        else:
            if (len(Atop) == 3):
                if (pushvalue.get() == '2'):
                    if (len(Btop) == 3):
                        note.set('Tube 2 is already Full')
                        print("Tube Full")
                    if (len(Btop) == 2):
                        print("Bstack 2 Index")
                        temp = Atop[2]
                        Btop.append(can_widget.create_rectangle(300, 250, 350, 300, fill=can_widget.itemcget(Atop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    if (len(Btop) == 1):
                        print("Bstack 1 Index")
                        temp = Atop[2]
                        Btop.append(can_widget.create_rectangle(300, 300, 350, 350, fill=can_widget.itemcget(Atop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    if (len(Btop) == 0):
                        print("Bstack 0 Index")
                        temp = Atop[2]
                        Btop.append(can_widget.create_rectangle(300, 350, 350, 400, fill=can_widget.itemcget(Atop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                elif (pushvalue.get() == '3'):
                    if (len(Ctop) == 3):
                        note.set('Tube 3 is already Full')
                        print("Tube Full")
                    if (len(Ctop) == 2):
                        temp = Atop[2]
                        Ctop.append(can_widget.create_rectangle(500, 250, 550, 300, fill=can_widget.itemcget(Atop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    if (len(Ctop) == 1):
                        temp = Atop[2]
                        Ctop.append(can_widget.create_rectangle(500, 300, 550, 350, fill=can_widget.itemcget(Atop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    if (len(Ctop) == 0):
                        temp = Atop[2]
                        Ctop.append(can_widget.create_rectangle(500, 350, 550, 400, fill=can_widget.itemcget(Atop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                elif (pushvalue.get() == '4'):
                    print("Dstack")
                    print(len(Dtop))
                    if (len(Dtop) == 3):
                        note.set('Tube 4 is already Full')
                    if (len(Dtop) == 2):
                        temp = Atop[2]
                        Dtop.append(can_widget.create_rectangle(700, 250, 750, 300, fill=can_widget.itemcget(Atop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    if (len(Dtop) == 1):
                        temp = Atop[2]
                        Dtop.append(can_widget.create_rectangle(700, 300, 750, 350, fill=can_widget.itemcget(Atop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    if (len(Dtop) == 0):
                        temp = Atop[2]
                        Dtop.append(can_widget.create_rectangle(700, 350, 750, 400, fill=can_widget.itemcget(Atop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                elif (pushvalue.get() == '5'):
                    print("Estack")
                    print(len(Dtop))
                    if (len(Etop) == 3):
                        note.set('Tube 5 is already Full')
                    if (len(Etop) == 2):
                        temp = Atop[2]
                        Etop.append(can_widget.create_rectangle(900, 250, 950, 300, fill=can_widget.itemcget(Atop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    if (len(Etop) == 1):
                        temp = Atop[2]
                        Etop.append(can_widget.create_rectangle(900, 300, 950, 350, fill=can_widget.itemcget(Atop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    if (len(Etop) == 0):
                        temp = Atop[2]
                        Etop.append(can_widget.create_rectangle(900, 350, 950, 400, fill=can_widget.itemcget(Atop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
            elif(len(Atop) == 2):
                    if (pushvalue.get() == '2'):
                        print(len(Btop))
                        if (len(Btop) == 3):
                            note.set('Tube 2 is already Full')
                        if (len(Btop) == 2):
                            temp = Atop[1]
                            Btop.append(can_widget.create_rectangle(300, 250, 350, 300, fill=can_widget.itemcget(Atop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)
                        if (len(Btop) == 1):
                            temp = Atop[1]
                            Btop.append(can_widget.create_rectangle(300, 300, 350, 350, fill=can_widget.itemcget(Atop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)
                        if (len(Btop) == 0):
                            temp = Atop[1]
                            Btop.append(can_widget.create_rectangle(300, 350, 350, 400, fill=can_widget.itemcget(Atop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)
                    elif (pushvalue.get() == '3'):
                        print("Cstack")
                        print(len(Ctop))
                        if (len(Ctop) == 3):
                            note.set('Tube 3 is already Full')
                        if (len(Ctop) == 2):
                            temp = Atop[1]
                            Ctop.append(can_widget.create_rectangle(500, 250, 550, 300,fill=can_widget.itemcget(Atop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)
                        if (len(Ctop) == 1):
                            temp = Atop[1]
                            Ctop.append(can_widget.create_rectangle(500, 300, 550, 350,fill=can_widget.itemcget(Atop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)
                        if (len(Ctop) == 0):
                            temp = Atop[1]
                            Ctop.append(can_widget.create_rectangle(500, 350, 550, 400,fill=can_widget.itemcget(Atop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)
                    elif (pushvalue.get() == '4'):
                        print("Dstack")
                        print(len(Dtop))
                        if (len(Dtop) == 3):
                            note.set('Tube 4 is already Full')
                        if (len(Dtop) == 2):
                            temp = Atop[1]
                            Dtop.append(can_widget.create_rectangle(700, 250, 750, 300,fill=can_widget.itemcget(Atop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)
                        if (len(Dtop) == 1):
                            temp = Atop[1]
                            Dtop.append(can_widget.create_rectangle(700, 300, 750, 350,fill=can_widget.itemcget(Atop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)
                        if (len(Dtop) == 0):
                            temp = Atop[1]
                            Dtop.append(can_widget.create_rectangle(700, 350, 750, 400,fill=can_widget.itemcget(Atop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)
                    elif (pushvalue.get() == '5'):
                        print("Estack")
                        print(len(Dtop))
                        if (len(Etop) == 3):
                            note.set('Tube 5 is already Full')
                        if (len(Etop) == 2):
                            temp = Atop[1]
                            Etop.append(can_widget.create_rectangle(900, 250, 950, 300,fill=can_widget.itemcget(Atop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)
                        if (len(Etop) == 1):
                            temp = Atop[1]
                            Etop.append(can_widget.create_rectangle(900, 300, 950, 350,fill=can_widget.itemcget(Atop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)
                        if (len(Etop) == 0):
                            temp = Atop[1]
                            Etop.append(can_widget.create_rectangle(900, 350, 950, 400,fill=can_widget.itemcget(Atop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)
            elif(len(Atop) == 1):
                    if (pushvalue.get() == '2'):
                        print(len(Btop))
                        if (len(Btop) == 3):
                            note.set('Tube 2 is already Full')
                        if (len(Btop) == 2):
                            temp = Atop[0]
                            Btop.append(can_widget.create_rectangle(300, 250, 350, 300, fill=can_widget.itemcget(Atop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)
                        if (len(Btop) == 1):
                            temp = Atop[0]
                            print(can_widget.itemcget(Atop[0], "fill"))
                            Btop.append(can_widget.create_rectangle(300, 300, 350, 350, fill=can_widget.itemcget(Atop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)
                        if (len(Btop) == 0):
                            temp = Atop[0]
                            Btop.append(can_widget.create_rectangle(300, 350, 350, 400, fill=can_widget.itemcget(Atop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)
                    elif (pushvalue.get() == '3'):
                        print("Cstack")
                        print(len(Ctop))
                        if (len(Ctop) == 3):
                            note.set('Tube 3 is already Full')
                        if (len(Ctop) == 2):
                            temp = Atop[0]
                            Ctop.append(can_widget.create_rectangle(500, 250, 550, 300,fill=can_widget.itemcget(Atop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)
                        if (len(Ctop) == 1):
                            temp = Atop[0]
                            Ctop.append(can_widget.create_rectangle(500, 300, 550, 350,fill=can_widget.itemcget(Atop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)
                        if (len(Ctop) == 0):
                            temp = Atop[0]
                            Ctop.append(can_widget.create_rectangle(500, 350, 550, 400,fill=can_widget.itemcget(Atop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)
                    elif (pushvalue.get() == '4'):
                        print("Dstack")
                        print(len(Dtop))
                        if (len(Dtop) == 3):
                            note.set('Tube 4 is already Full')
                        if (len(Dtop) == 2):
                            temp = Atop[0]
                            Dtop.append(can_widget.create_rectangle(700, 250, 750, 300,fill=can_widget.itemcget(Atop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)
                        if (len(Dtop) == 1):
                            temp = Atop[0]
                            Dtop.append(can_widget.create_rectangle(700, 300, 750, 350,fill=can_widget.itemcget(Atop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)
                        if (len(Dtop) == 0):
                            temp = Atop[0]
                            Dtop.append(can_widget.create_rectangle(700, 350, 750, 400,fill=can_widget.itemcget(Atop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)
                    elif (pushvalue.get() == '5'):
                        print("Estack")
                        print(len(Dtop))
                        if (len(Etop) == 3):
                            note.set('Tube 5 is already Full')
                        if (len(Etop) == 2):
                            temp = Atop[0]
                            Etop.append(can_widget.create_rectangle(900, 250, 950, 300,fill=can_widget.itemcget(Atop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)
                        if (len(Etop) == 1):
                            temp = Atop[0]
                            Etop.append(can_widget.create_rectangle(900, 300, 950, 350,fill=can_widget.itemcget(Atop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)
                        if (len(Etop) == 0):
                            temp = Atop[0]
                            Etop.append(can_widget.create_rectangle(900, 350, 950, 400,fill=can_widget.itemcget(Atop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)


    #Pop from B stack
    elif(popvalue.get() == '2'):
            note.set('Game on')
            if (len(Btop) == 0):
                note.set('Tube 2 is already Empty')
            else:
                if (len(Btop) == 3):
                    if (pushvalue.get() == '1'):
                        if (len(Atop) == 3):
                            note.set('Tube 1 is already Full')
                        if (len(Atop) == 2):
                            print("Bstack 2 Index")
                            temp = Btop[2]
                            Atop.append(
                                can_widget.create_rectangle(100, 250, 150, 300,
                                                       fill=can_widget.itemcget(Btop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)
                        if (len(Atop) == 1):
                            print("Bstack 1 Index")
                            temp = Btop[2]
                            Atop.append(
                                can_widget.create_rectangle(100, 300, 150, 350,
                                                       fill=can_widget.itemcget(Btop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)
                        if (len(Atop) == 0):
                            print("Bstack 0 Index")
                            temp = Btop[2]
                            Atop.append(
                                can_widget.create_rectangle(100, 350, 150, 400,
                                                       fill=can_widget.itemcget(Btop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)

                            print("Len of Atop:", len(Btop))
                    elif (pushvalue.get() == '3'):
                        print("Cstack")
                        print(len(Ctop))
                        if (len(Ctop) == 3):
                            note.set('Tube 3 is already Full')
                            print("Tube Full")
                        if (len(Ctop) == 2):
                            temp = Btop[2]
                            Ctop.append(
                                can_widget.create_rectangle(500, 250, 550, 300,
                                                       fill=can_widget.itemcget(Btop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)
                        if (len(Ctop) == 1):
                            temp = Btop[2]
                            Ctop.append(
                                can_widget.create_rectangle(500, 300, 550, 350,
                                                       fill=can_widget.itemcget(Btop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)
                        if (len(Ctop) == 0):
                            temp = Btop[2]
                            Ctop.append(
                                can_widget.create_rectangle(500, 350, 550, 400,
                                                       fill=can_widget.itemcget(Btop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)
                    elif (pushvalue.get() == '4'):
                        print("Dstack")
                        print(len(Dtop))
                        if (len(Dtop) == 3):
                            note.set('Tube 4 is already Full')
                        if (len(Dtop) == 2):
                            temp = Btop[2]
                            Dtop.append(
                                can_widget.create_rectangle(700, 250, 750, 300,
                                                       fill=can_widget.itemcget(Btop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)

                        if (len(Dtop) == 1):
                            temp = Btop[2]
                            Dtop.append(
                                can_widget.create_rectangle(700, 300, 750, 350,
                                                       fill=can_widget.itemcget(Btop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)
                        if (len(Dtop) == 0):
                            temp = Btop[2]
                            Dtop.append(
                                can_widget.create_rectangle(700, 350, 750, 400,
                                                       fill=can_widget.itemcget(Btop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)
                    elif (pushvalue.get() == '5'):
                        print("Estack")
                        print(len(Dtop))
                        if (len(Etop) == 3):
                            note.set('Tube 5 is already Full')
                        if (len(Etop) == 2):
                            temp = Btop[2]
                            Etop.append(
                                can_widget.create_rectangle(900, 250, 950, 300,
                                                       fill=can_widget.itemcget(Btop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)

                        if (len(Etop) == 1):
                            temp = Btop[2]
                            Etop.append(
                                can_widget.create_rectangle(900, 300, 950, 350,
                                                       fill=can_widget.itemcget(Btop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)
                        if (len(Etop) == 0):
                            temp = Btop[2]
                            Etop.append(
                                can_widget.create_rectangle(900, 350, 950, 400,
                                                       fill=can_widget.itemcget(Btop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)
                elif (len(Btop) == 2):
                    if (pushvalue.get() == '1'):
                        print(len(Atop))
                        if (len(Atop) == 3):
                            note.set('Tube 1 is already Full')
                        if (len(Atop) == 2):
                            temp = Btop[1]
                            Atop.append(
                                can_widget.create_rectangle(100, 250, 150, 300,
                                                       fill=can_widget.itemcget(Btop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)
                        if (len(Atop) == 1):
                            temp = Btop[1]
                            Atop.append(
                                can_widget.create_rectangle(100, 300, 150, 350,
                                                       fill=can_widget.itemcget(Btop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)
                        if (len(Atop) == 0):
                            temp = Btop[1]
                            Atop.append(
                                can_widget.create_rectangle(100, 350, 150, 400,
                                                       fill=can_widget.itemcget(Btop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)
                    elif (pushvalue.get() == '3'):
                        print("Cstack")
                        print(len(Ctop))
                        if (len(Ctop) == 3):
                            note.set('Tube 3 is already Full')
                            print("Tube Full")
                        if (len(Ctop) == 2):
                            temp = Btop[1]
                            Ctop.append(
                                can_widget.create_rectangle(500, 250, 550, 300,
                                                       fill=can_widget.itemcget(Btop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)

                        if (len(Ctop) == 1):
                            temp = Btop[1]
                            Ctop.append(
                                can_widget.create_rectangle(500, 300, 550, 350,
                                                       fill=can_widget.itemcget(Btop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)
                        if (len(Ctop) == 0):
                            temp = Btop[1]
                            Ctop.append(
                                can_widget.create_rectangle(500, 350, 550, 400,
                                                       fill=can_widget.itemcget(Btop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)
                    elif (pushvalue.get() == '4'):
                        print("Dstack")
                        print(len(Dtop))
                        if (len(Dtop) == 3):
                            note.set('Tube 4 is already Full')
                        if (len(Dtop) == 2):
                            temp = Btop[1]
                            Dtop.append(
                                can_widget.create_rectangle(700, 250, 750, 300,
                                                       fill=can_widget.itemcget(Btop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)

                        if (len(Dtop) == 1):
                            temp = Btop[1]
                            Dtop.append(
                                can_widget.create_rectangle(700, 300, 750, 350,
                                                       fill=can_widget.itemcget(Btop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)
                        if (len(Dtop) == 0):
                            temp = Btop[1]
                            Dtop.append(
                                can_widget.create_rectangle(700, 350, 750, 400,
                                                       fill=can_widget.itemcget(Btop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)
                    elif (pushvalue.get() == '5'):
                        print("Estack")
                        print(len(Dtop))
                        if (len(Etop) == 3):
                            note.set('Tube 5 is already Full')
                        if (len(Etop) == 2):
                            temp = Btop[1]
                            Etop.append(
                                can_widget.create_rectangle(900, 250, 950, 300,
                                                       fill=can_widget.itemcget(Btop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)

                        if (len(Etop) == 1):
                            temp = Btop[1]
                            Etop.append(
                                can_widget.create_rectangle(900, 300, 950, 350,
                                                       fill=can_widget.itemcget(Btop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)
                        if (len(Etop) == 0):
                            temp = Btop[1]
                            Etop.append(
                                can_widget.create_rectangle(900, 350, 950, 400,
                                                       fill=can_widget.itemcget(Btop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)
                elif (len(Btop) == 1):
                    if (pushvalue.get() == '1'):
                        print(len(Atop))
                        if (len(Atop) == 3):
                            note.set('Tube 1 is already Full')
                        if (len(Atop) == 2):
                            temp = Btop[0]
                            Atop.append(
                                can_widget.create_rectangle(100, 250, 150, 300,
                                                       fill=can_widget.itemcget(Btop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)
                        if (len(Atop) == 1):
                            temp = Btop[0]
                            print(can_widget.itemcget(Atop[0], "fill"),outline='white')
                            Atop.append(
                                can_widget.create_rectangle(100, 300, 150, 350,
                                                       fill=can_widget.itemcget(Btop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)
                        if (len(Atop) == 0):
                            temp = Btop[0]
                            Atop.append(
                                can_widget.create_rectangle(100, 350, 150, 400,
                                                       fill=can_widget.itemcget(Btop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)
                    elif (pushvalue.get() == '3'):
                        print("Cstack")
                        print(len(Ctop))
                        if (len(Ctop) == 3):
                            note.set('Tube 3 is already Full')
                        if (len(Ctop) == 2):
                            temp = Btop[0]
                            Ctop.append(
                                can_widget.create_rectangle(500, 250, 550, 300,
                                                       fill=can_widget.itemcget(Btop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)

                        if (len(Ctop) == 1):
                            temp = Btop[0]
                            Ctop.append(
                                can_widget.create_rectangle(500, 300, 550, 350,
                                                       fill=can_widget.itemcget(Btop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)
                        if (len(Ctop) == 0):
                            temp = Atop[0]
                            Ctop.append(
                                can_widget.create_rectangle(500, 350, 550, 400,
                                                       fill=can_widget.itemcget(Btop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)
                    elif (pushvalue.get() == '4'):
                        print("Dstack")
                        print(len(Dtop))
                        if (len(Dtop) == 3):
                            note.set('Tube 4 is already Full')
                        if (len(Dtop) == 2):
                            temp = Btop[0]
                            Dtop.append(
                                can_widget.create_rectangle(700, 250, 750, 300,
                                                       fill=can_widget.itemcget(Btop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)

                        if (len(Dtop) == 1):
                            temp = Btop[0]
                            Dtop.append(
                                can_widget.create_rectangle(700, 300, 750, 350,
                                                       fill=can_widget.itemcget(Btop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)
                        if (len(Dtop) == 0):
                            temp = Btop[0]
                            Dtop.append(
                                can_widget.create_rectangle(700, 350, 750, 400,
                                                       fill=can_widget.itemcget(Btop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)
                    elif (pushvalue.get() == '5'):
                        print("Estack")
                        print(len(Etop))
                        if (len(Etop) == 3):
                            note.set('Tube 5 is already Full')
                        if (len(Etop) == 2):
                            temp = Btop[0]
                            Etop.append(
                                can_widget.create_rectangle(900, 250, 950, 300,
                                                       fill=can_widget.itemcget(Btop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)

                        if (len(Etop) == 1):
                            temp = Btop[0]
                            Etop.append(
                                can_widget.create_rectangle(900, 300, 950, 350,
                                                       fill=can_widget.itemcget(Btop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)
                        if (len(Etop) == 0):
                            temp = Btop[0]
                            Etop.append(
                                can_widget.create_rectangle(900, 350, 950, 400,
                                                       fill=can_widget.itemcget(Btop.pop(), "fill"),outline='white'))
                            can_widget.delete(temp)
    # Pop from C stack
    elif (popvalue.get() == '3'):
        note.set('Game on')
        if (len(Ctop) == 0):
            note.set('Tube 3 is already Empty')
        else:
            if (len(Ctop) == 3):
                if (pushvalue.get() == '1'):
                    if (len(Atop) == 3):
                        note.set('Tube 1 is already Full')
                    elif (len(Atop) == 2):
                        temp = Ctop[2]
                        Atop.append(
                            can_widget.create_rectangle(100, 250, 150, 300,
                                                   fill=can_widget.itemcget(Ctop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    elif (len(Atop) == 1):
                        temp = Ctop[2]
                        Atop.append(
                            can_widget.create_rectangle(100, 300, 150, 350,
                                                   fill=can_widget.itemcget(Ctop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    elif (len(Atop) == 0):
                        temp = Ctop[2]
                        Atop.append(
                            can_widget.create_rectangle(100, 350, 150, 400,
                                                   fill=can_widget.itemcget(Ctop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)

                elif (pushvalue.get() == '2'):
                    print("Bstack")
                    print(len(Btop))
                    if (len(Btop) == 3):
                        note.set('Tube 2 is already Full')
                    if (len(Btop) == 2):
                        temp = Ctop[2]
                        Btop.append(
                            can_widget.create_rectangle(300, 250, 350, 300,
                                                   fill=can_widget.itemcget(Ctop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    if (len(Btop) == 1):
                        temp = Ctop[2]
                        Btop.append(
                            can_widget.create_rectangle(300, 300, 350, 350,
                                                   fill=can_widget.itemcget(Ctop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    if (len(Btop) == 0):
                        temp = Ctop[2]
                        Btop.append(
                            can_widget.create_rectangle(300, 350, 350, 400,
                                                   fill=can_widget.itemcget(Ctop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                elif (pushvalue.get() == '4'):
                    print("Dstack")
                    print(len(Dtop))
                    if (len(Dtop) == 3):
                        note.set('Tube 4 is already Full')
                    if (len(Dtop) == 2):
                        temp = Ctop[2]
                        Dtop.append(
                            can_widget.create_rectangle(700, 250, 750, 300,
                                                   fill=can_widget.itemcget(Ctop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)

                    if (len(Dtop) == 1):
                        temp = Ctop[2]
                        Dtop.append(
                            can_widget.create_rectangle(700, 300, 750, 350,
                                                   fill=can_widget.itemcget(Ctop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    if (len(Dtop) == 0):
                        temp = Ctop[2]
                        Dtop.append(
                            can_widget.create_rectangle(700, 350, 750, 400,
                                                   fill=can_widget.itemcget(Ctop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                elif (pushvalue.get() == '5'):
                    print("Estack")
                    if (len(Etop) == 3):
                        note.set('Tube 5 is already Full')
                    if (len(Etop) == 2):
                        temp = Ctop[2]
                        Etop.append(
                            can_widget.create_rectangle(900, 250, 950, 300,
                                                   fill=can_widget.itemcget(Ctop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)

                    if (len(Etop) == 1):
                        temp = Ctop[2]
                        Etop.append(
                            can_widget.create_rectangle(900, 300, 950, 350,
                                                   fill=can_widget.itemcget(Ctop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    if (len(Etop) == 0):
                        temp = Ctop[2]
                        Etop.append(
                            can_widget.create_rectangle(900, 350, 950, 400,
                                                   fill=can_widget.itemcget(Ctop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
            elif (len(Ctop) == 2):
                if (pushvalue.get() == '1'):
                    print(len(Atop))
                    if (len(Atop) == 3):
                        note.set('Tube 1 is already Full')
                    if (len(Atop) == 2):
                        temp = Ctop[1]
                        Atop.append(
                            can_widget.create_rectangle(100, 250, 150, 300,
                                                   fill=can_widget.itemcget(Ctop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    if (len(Atop) == 1):
                        temp = Ctop[1]
                        Atop.append(
                            can_widget.create_rectangle(100, 300, 150, 350,
                                                   fill=can_widget.itemcget(Ctop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    if (len(Atop) == 0):
                        temp = Ctop[1]
                        Atop.append(
                            can_widget.create_rectangle(100, 350, 150, 400,
                                                   fill=can_widget.itemcget(Ctop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                elif (pushvalue.get() == '2'):
                    print("Bstack")
                    print(len(Btop))
                    if (len(Btop) == 3):
                        note.set('Tube 2 is already Full')
                    if (len(Btop) == 2):
                        temp = Ctop[1]
                        Btop.append(
                            can_widget.create_rectangle(300, 250, 350, 300,
                                                   fill=can_widget.itemcget(Ctop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)

                    if (len(Btop) == 1):
                        temp = Ctop[1]
                        Btop.append(
                            can_widget.create_rectangle(300, 300, 350, 350,
                                                   fill=can_widget.itemcget(Ctop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    if (len(Btop) == 0):
                        temp = Ctop[1]
                        Btop.append(
                            can_widget.create_rectangle(300, 350, 350, 400,
                                                   fill=can_widget.itemcget(Ctop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                elif (pushvalue.get() == '4'):
                    print("Dstack")
                    print(len(Dtop))
                    if (len(Dtop) == 3):
                        note.set('Tube 4 is already Full')
                    if (len(Dtop) == 2):
                        temp = Ctop[1]
                        Dtop.append(
                            can_widget.create_rectangle(700, 250, 750, 300,
                                                   fill=can_widget.itemcget(Ctop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)

                    if (len(Dtop) == 1):
                        temp = Ctop[1]
                        Dtop.append(
                            can_widget.create_rectangle(700, 300, 750, 350,
                                                   fill=can_widget.itemcget(Ctop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    if (len(Dtop) == 0):
                        temp = Ctop[1]
                        Dtop.append(
                            can_widget.create_rectangle(700, 350, 750, 400,
                                                   fill=can_widget.itemcget(Ctop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                elif (pushvalue.get() == '5'):
                    print("Estack")
                    print(len(Etop))
                    if (len(Etop) == 3):
                        note.set('Tube 5 is already Full')
                    if (len(Etop) == 2):
                        temp = Ctop[1]
                        Etop.append(
                            can_widget.create_rectangle(900, 250, 950, 300,
                                                   fill=can_widget.itemcget(Ctop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)

                    if (len(Etop) == 1):
                        temp = Ctop[1]
                        Etop.append(
                            can_widget.create_rectangle(900, 300, 950, 350,
                                                   fill=can_widget.itemcget(Ctop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    if (len(Etop) == 0):
                        temp = Ctop[1]
                        Etop.append(
                            can_widget.create_rectangle(900, 350, 950, 400,
                                                   fill=can_widget.itemcget(Ctop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
            elif (len(Ctop) == 1):
                if (pushvalue.get() == '1'):
                    print(len(Atop))
                    if (len(Atop) == 3):
                        note.set('Tube 1 is already Full')
                    if (len(Atop) == 2):
                        temp = Ctop[0]
                        Atop.append(
                            can_widget.create_rectangle(100, 250, 150, 300,
                                                   fill=can_widget.itemcget(Ctop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    if (len(Atop) == 1):
                        temp = Ctop[0]
                        Atop.append(
                            can_widget.create_rectangle(100, 300, 150, 350,
                                                   fill=can_widget.itemcget(Ctop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    if (len(Atop) == 0):
                        temp = Ctop[0]
                        Atop.append(
                            can_widget.create_rectangle(100, 350, 150, 400,
                                                   fill=can_widget.itemcget(Ctop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                elif (pushvalue.get() == '2'):
                    print("Cstack")
                    print(len(Ctop))
                    if (len(Btop) == 3):
                        note.set('Tube 2 is already Full')
                    if (len(Btop) == 2):
                        temp = Ctop[0]
                        Btop.append(
                            can_widget.create_rectangle(300, 250, 350, 300,
                                                   fill=can_widget.itemcget(Ctop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)

                    if (len(Btop) == 1):
                        temp = Ctop[0]
                        Btop.append(
                            can_widget.create_rectangle(300, 300, 350, 350,
                                                   fill=can_widget.itemcget(Ctop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    if (len(Btop) == 0):
                        temp = Ctop[0]
                        Btop.append(
                            can_widget.create_rectangle(300, 350, 350, 400,
                                                   fill=can_widget.itemcget(Ctop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                elif (pushvalue.get() == '4'):
                    print("Dstack")
                    print(len(Dtop))
                    if (len(Dtop) == 3):
                        note.set('Tube 4 is already Full')
                    if (len(Dtop) == 2):
                        temp = Ctop[0]
                        Dtop.append(
                            can_widget.create_rectangle(700, 250, 750, 300,
                                                   fill=can_widget.itemcget(Ctop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)

                    if (len(Dtop) == 1):
                        temp = Ctop[0]
                        Dtop.append(
                            can_widget.create_rectangle(700, 300, 750, 350,
                                                   fill=can_widget.itemcget(Ctop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    if (len(Dtop) == 0):
                        temp = Ctop[0]
                        Dtop.append(
                            can_widget.create_rectangle(700, 350, 750, 400,
                                                   fill=can_widget.itemcget(Ctop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                elif (pushvalue.get() == '5'):
                    print("Estack")
                    print(len(Etop))
                    if (len(Etop) == 3):
                        note.set('Tube 5 is already Full')
                    if (len(Etop) == 2):
                        temp = Ctop[0]
                        Etop.append(
                            can_widget.create_rectangle(900, 250, 950, 300,
                                                   fill=can_widget.itemcget(Ctop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)

                    if (len(Etop) == 1):
                        temp = Ctop[0]
                        Etop.append(
                            can_widget.create_rectangle(900, 300, 950, 350,
                                                   fill=can_widget.itemcget(Ctop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    if (len(Etop) == 0):
                        temp = Ctop[0]
                        Etop.append(
                            can_widget.create_rectangle(900, 350, 950, 400,
                                                   fill=can_widget.itemcget(Ctop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
    # Pop from D stack
    elif (popvalue.get() == '4'):
        note.set('Game on')
        if (len(Dtop) == 0):
            note.set('Tube 4 is already Empty')
        else:
            if (len(Dtop) == 3):
                if (pushvalue.get() == '1'):
                    if (len(Atop) == 3):
                        note.set('Tube 1 is already Full')
                    elif (len(Atop) == 2):
                        temp = Dtop[2]
                        Atop.append(
                            can_widget.create_rectangle(100, 250, 150, 300,
                                                   fill=can_widget.itemcget(Dtop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    elif (len(Atop) == 1):
                        temp = Dtop[2]
                        Atop.append(
                            can_widget.create_rectangle(100, 300, 150, 350,
                                                   fill=can_widget.itemcget(Dtop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    elif (len(Atop) == 0):
                        temp = Dtop[2]
                        Atop.append(
                            can_widget.create_rectangle(100, 350, 150, 400,
                                                   fill=can_widget.itemcget(Dtop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)

                elif (pushvalue.get() == '2'):
                    print("Bstack")
                    print(len(Btop))
                    if (len(Btop) == 3):
                        note.set('Tube 2 is already Full')
                    if (len(Btop) == 2):
                        temp = Dtop[2]
                        Btop.append(
                            can_widget.create_rectangle(300, 250, 350, 300,
                                                   fill=can_widget.itemcget(Dtop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    if (len(Btop) == 1):
                        temp = Dtop[2]
                        Btop.append(
                            can_widget.create_rectangle(300, 300, 350, 350,
                                                   fill=can_widget.itemcget(Dtop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    if (len(Btop) == 0):
                        temp = Dtop[2]
                        Btop.append(
                            can_widget.create_rectangle(300, 350, 350, 400,
                                                   fill=can_widget.itemcget(Dtop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                elif (pushvalue.get() == '3'):
                    print("Cstack")
                    print(len(Ctop))
                    if (len(Ctop) == 3):
                        note.set('Tube 3 is already Full')
                    if (len(Ctop) == 2):
                        temp = Dtop[2]
                        Ctop.append(
                            can_widget.create_rectangle(500, 250, 550, 300,
                                                   fill=can_widget.itemcget(Dtop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)

                    if (len(Ctop) == 1):
                        temp = Dtop[2]
                        Ctop.append(
                            can_widget.create_rectangle(500, 300, 550, 350,
                                                   fill=can_widget.itemcget(Dtop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    if (len(Ctop) == 0):
                        temp = Dtop[2]
                        Ctop.append(
                            can_widget.create_rectangle(500, 350, 550, 400,
                                                   fill=can_widget.itemcget(Dtop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                elif (pushvalue.get() == '5'):
                    print("Estack")
                    print(len(Etop))
                    if (len(Etop) == 3):
                        note.set('Tube 5 is already Full')
                    if (len(Etop) == 2):
                        temp = Dtop[2]
                        Etop.append(
                            can_widget.create_rectangle(900, 250, 950, 300,
                                                   fill=can_widget.itemcget(Dtop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)

                    if (len(Etop) == 1):
                        temp = Dtop[2]
                        Etop.append(
                            can_widget.create_rectangle(900, 300, 950, 350,
                                                   fill=can_widget.itemcget(Dtop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    if (len(Etop) == 0):
                        temp = Dtop[2]
                        Etop.append(
                            can_widget.create_rectangle(900, 350, 950, 400,
                                                   fill=can_widget.itemcget(Dtop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
            elif (len(Dtop) == 2):
                if (pushvalue.get() == '1'):
                    print(len(Atop))
                    if (len(Atop) == 3):
                        note.set('Tube 1 is already Full')
                    if (len(Atop) == 2):
                        temp = Dtop[1]
                        Atop.append(
                            can_widget.create_rectangle(100, 250, 150, 300,
                                                   fill=can_widget.itemcget(Dtop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    if (len(Atop) == 1):
                        temp = Dtop[1]
                        Atop.append(
                            can_widget.create_rectangle(100, 300, 150, 350,
                                                   fill=can_widget.itemcget(Dtop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    if (len(Atop) == 0):
                        temp = Dtop[1]
                        Atop.append(
                            can_widget.create_rectangle(100, 350, 150, 400,
                                                   fill=can_widget.itemcget(Dtop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                elif (pushvalue.get() == '2'):
                    print("Bstack")
                    print(len(Btop))
                    if (len(Btop) == 3):
                        note.set('Tube 2 is already Full')
                    if (len(Btop) == 2):
                        temp = Dtop[1]
                        Btop.append(
                            can_widget.create_rectangle(300, 250, 350, 300,
                                                   fill=can_widget.itemcget(Dtop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)

                    if (len(Btop) == 1):
                        temp = Dtop[1]
                        Btop.append(
                            can_widget.create_rectangle(300, 300, 350, 350,
                                                   fill=can_widget.itemcget(Dtop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    if (len(Btop) == 0):
                        temp = Dtop[1]
                        Btop.append(
                            can_widget.create_rectangle(300, 350, 350, 400,
                                                   fill=can_widget.itemcget(Dtop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                elif (pushvalue.get() == '3'):
                    print("Cstack")
                    print(len(Ctop))
                    if (len(Ctop) == 3):
                        note.set('Tube 3 is already Full')
                    if (len(Ctop) == 2):
                        temp = Dtop[1]
                        Ctop.append(
                            can_widget.create_rectangle(500, 250, 550, 300,
                                                   fill=can_widget.itemcget(Dtop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)

                    if (len(Ctop) == 1):
                        temp = Dtop[1]
                        Ctop.append(
                            can_widget.create_rectangle(500, 300, 550, 350,
                                                   fill=can_widget.itemcget(Dtop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    if (len(Ctop) == 0):
                        temp = Dtop[1]
                        Ctop.append(
                            can_widget.create_rectangle(500, 350, 550, 400,
                                                   fill=can_widget.itemcget(Dtop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                elif (pushvalue.get() == '5'):
                    print("Estack")
                    print(len(Etop))
                    if (len(Etop) == 3):
                        note.set('Tube 5 is already Full')
                    if (len(Etop) == 2):
                        temp = Dtop[1]
                        Etop.append(
                            can_widget.create_rectangle(900, 250, 950, 300,
                                                   fill=can_widget.itemcget(Dtop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)

                    if (len(Etop) == 1):
                        temp = Dtop[1]
                        Etop.append(
                            can_widget.create_rectangle(900, 300, 950, 350,
                                                   fill=can_widget.itemcget(Dtop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    if (len(Etop) == 0):
                        temp = Dtop[1]
                        Etop.append(
                            can_widget.create_rectangle(900, 350, 950, 400,
                                                   fill=can_widget.itemcget(Dtop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
            elif (len(Dtop) == 1):
                if (pushvalue.get() == '1'):
                    print(len(Atop))
                    if (len(Atop) == 3):
                        note.set('Tube 1 is already Full')
                    if (len(Atop) == 2):
                        temp = Dtop[0]
                        Atop.append(
                            can_widget.create_rectangle(100, 250, 150, 300,
                                                   fill=can_widget.itemcget(Dtop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    if (len(Atop) == 1):
                        temp = Dtop[0]
                        Atop.append(
                            can_widget.create_rectangle(100, 300, 150, 350,
                                                   fill=can_widget.itemcget(Dtop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    if (len(Atop) == 0):
                        temp = Dtop[0]
                        Atop.append(
                            can_widget.create_rectangle(100, 350, 150, 400,
                                                   fill=can_widget.itemcget(Dtop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                elif (pushvalue.get() == '2'):
                    print("Bstack")
                    print(len(Btop))
                    if (len(Btop) == 3):
                        note.set('Tube 2 is already Full')
                    if (len(Btop) == 2):
                        temp = Dtop[0]
                        Btop.append(
                            can_widget.create_rectangle(300, 250, 350, 300,
                                                   fill=can_widget.itemcget(Dtop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)

                    if (len(Btop) == 1):
                        temp = Dtop[0]
                        Btop.append(
                            can_widget.create_rectangle(300, 300, 350, 350,
                                                   fill=can_widget.itemcget(Dtop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    if (len(Btop) == 0):
                        temp = Dtop[0]
                        Btop.append(
                            can_widget.create_rectangle(300, 350, 350, 400,
                                                   fill=can_widget.itemcget(Dtop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                elif (pushvalue.get() == '3'):
                    print("Cstack")
                    print(len(Ctop))
                    if (len(Ctop) == 3):
                        note.set('Tube 3 is already Full')
                    if (len(Ctop) == 2):
                        temp = Dtop[0]
                        Ctop.append(
                            can_widget.create_rectangle(500, 250, 550, 300,
                                                   fill=can_widget.itemcget(Dtop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)

                    if (len(Ctop) == 1):
                        temp = Dtop[0]
                        Ctop.append(
                            can_widget.create_rectangle(500, 300, 550, 350,
                                                   fill=can_widget.itemcget(Dtop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    if (len(Ctop) == 0):
                        temp = Dtop[0]
                        Ctop.append(
                            can_widget.create_rectangle(500, 350, 550, 400,
                                                   fill=can_widget.itemcget(Dtop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                elif (pushvalue.get() == '5'):
                    print("Estack")
                    print(len(Etop))
                    if (len(Etop) == 3):
                        note.set('Tube 5 is already Full')
                    if (len(Etop) == 2):
                        temp = Dtop[0]
                        Etop.append(
                            can_widget.create_rectangle(900, 250, 950, 300,
                                                   fill=can_widget.itemcget(Dtop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)

                    if (len(Etop) == 1):
                        temp = Dtop[0]
                        Etop.append(
                            can_widget.create_rectangle(900, 300, 950, 350,
                                                   fill=can_widget.itemcget(Dtop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    if (len(Etop) == 0):
                        temp = Dtop[0]
                        Etop.append(
                            can_widget.create_rectangle(900, 350, 950, 400,
                                                   fill=can_widget.itemcget(Dtop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
    # Pop from E stack
    elif (popvalue.get() == '5'):
        note.set('Game on')
        if (len(Etop) == 0):
            note.set('Tube 5 is already Empty')
        else:
            if (len(Etop) == 3):
                if (pushvalue.get() == '1'):
                    if (len(Atop) == 3):
                        note.set('Tube 1 is already Full')
                    elif (len(Atop) == 2):
                        temp = Etop[2]
                        Atop.append(
                            can_widget.create_rectangle(100, 250, 150, 300,
                                                   fill=can_widget.itemcget(Etop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    elif (len(Atop) == 1):
                        temp = Etop[2]
                        Atop.append(
                            can_widget.create_rectangle(100, 300, 150, 350,
                                                   fill=can_widget.itemcget(Etop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    elif (len(Atop) == 0):
                        temp = Etop[2]
                        Atop.append(
                            can_widget.create_rectangle(100, 350, 150, 400,
                                                   fill=can_widget.itemcget(Etop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)

                elif (pushvalue.get() == '2'):
                    print("Bstack")
                    print(len(Btop))
                    if (len(Btop) == 3):
                        note.set('Tube 2 is already Full')
                    if (len(Btop) == 2):
                        temp = Etop[2]
                        Btop.append(
                            can_widget.create_rectangle(300, 250, 350, 300,
                                                   fill=can_widget.itemcget(Etop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    if (len(Btop) == 1):
                        temp = Etop[2]
                        Btop.append(
                            can_widget.create_rectangle(300, 300, 350, 350,
                                                   fill=can_widget.itemcget(Etop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    if (len(Btop) == 0):
                        temp = Etop[2]
                        Btop.append(
                            can_widget.create_rectangle(300, 350, 350, 400,
                                                   fill=can_widget.itemcget(Etop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                elif (pushvalue.get() == '3'):
                    print("Cstack")
                    print(len(Ctop))
                    if (len(Ctop) == 3):
                        note.set('Tube 3 is already Full')
                    if (len(Ctop) == 2):
                        temp = Etop[2]
                        Ctop.append(
                            can_widget.create_rectangle(500, 250, 550, 300,
                                                   fill=can_widget.itemcget(Etop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)

                    if (len(Ctop) == 1):
                        temp = Etop[2]
                        Ctop.append(
                            can_widget.create_rectangle(500, 300, 550, 350,
                                                   fill=can_widget.itemcget(Etop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    if (len(Ctop) == 0):
                        temp = Etop[2]
                        Ctop.append(
                            can_widget.create_rectangle(500, 350, 550, 400,
                                                   fill=can_widget.itemcget(Etop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                elif (pushvalue.get() == '4'):
                    print("Dstack")
                    print(len(Dtop))
                    if (len(Dtop) == 3):
                        note.set('Tube 4 is already Full')
                    if (len(Dtop) == 2):
                        temp = Etop[2]
                        Dtop.append(
                            can_widget.create_rectangle(700, 250, 750, 300,
                                                   fill=can_widget.itemcget(Etop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)

                    if (len(Dtop) == 1):
                        temp = Etop[2]
                        Dtop.append(
                            can_widget.create_rectangle(700, 300, 750, 350,
                                                   fill=can_widget.itemcget(Etop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    if (len(Dtop) == 0):
                        temp = Etop[2]
                        Dtop.append(
                            can_widget.create_rectangle(700, 350, 750, 400,
                                                   fill=can_widget.itemcget(Etop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
            elif (len(Etop) == 2):
                if (pushvalue.get() == '1'):
                    print(len(Atop))
                    if (len(Atop) == 3):
                        note.set('Tube 1 is already Full')
                    if (len(Atop) == 2):
                        temp = Etop[1]
                        Atop.append(
                            can_widget.create_rectangle(100, 250, 150, 300,
                                                   fill=can_widget.itemcget(Etop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    if (len(Atop) == 1):
                        temp = Etop[1]
                        Atop.append(
                            can_widget.create_rectangle(100, 300, 150, 350,
                                                   fill=can_widget.itemcget(Etop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    if (len(Atop) == 0):
                        temp = Etop[1]
                        Atop.append(
                            can_widget.create_rectangle(100, 350, 150, 400,
                                                   fill=can_widget.itemcget(Etop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                elif (pushvalue.get() == '2'):
                    print("Bstack")
                    print(len(Btop))
                    if (len(Btop) == 3):
                        note.set('Tube 2 is already Full')
                    if (len(Btop) == 2):
                        temp = Etop[1]
                        Btop.append(
                            can_widget.create_rectangle(300, 250, 350, 300,
                                                   fill=can_widget.itemcget(Etop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)

                    if (len(Btop) == 1):
                        temp = Etop[1]
                        Btop.append(
                            can_widget.create_rectangle(300, 300, 350, 350,
                                                   fill=can_widget.itemcget(Etop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    if (len(Btop) == 0):
                        temp = Etop[1]
                        Btop.append(
                            can_widget.create_rectangle(300, 350, 350, 400,
                                                   fill=can_widget.itemcget(Etop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                elif (pushvalue.get() == '3'):
                    print("Cstack")
                    print(len(Ctop))
                    if (len(Ctop) == 3):
                        note.set('Tube 3 is already Full')
                    if (len(Ctop) == 2):
                        temp = Etop[1]
                        Ctop.append(
                            can_widget.create_rectangle(500, 250, 550, 300,
                                                   fill=can_widget.itemcget(Etop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)

                    if (len(Ctop) == 1):
                        temp = Etop[1]
                        Ctop.append(
                            can_widget.create_rectangle(500, 300, 550, 350,
                                                   fill=can_widget.itemcget(Etop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    if (len(Ctop) == 0):
                        temp = Etop[1]
                        Ctop.append(
                            can_widget.create_rectangle(500, 350, 550, 400,
                                                   fill=can_widget.itemcget(Etop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                elif (pushvalue.get() == '4'):
                    print("Dstack")
                    print(len(Dtop))
                    if (len(Dtop) == 3):
                        note.set('Tube 4 is already Full')
                    if (len(Dtop) == 2):
                        temp = Etop[1]
                        Dtop.append(
                            can_widget.create_rectangle(700, 250, 750, 300,
                                                   fill=can_widget.itemcget(Etop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)

                    if (len(Dtop) == 1):
                        temp = Etop[1]
                        Dtop.append(
                            can_widget.create_rectangle(700, 300, 750, 350,
                                                   fill=can_widget.itemcget(Etop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    if (len(Dtop) == 0):
                        temp = Etop[1]
                        Dtop.append(
                            can_widget.create_rectangle(700, 350, 750, 400,
                                                   fill=can_widget.itemcget(Etop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
            elif (len(Etop) == 1):
                if (pushvalue.get() == '1'):
                    print(len(Atop))
                    if (len(Atop) == 3):
                        note.set('Tube 1 is already Full')
                    if (len(Atop) == 2):
                        temp = Etop[0]
                        Atop.append(
                            can_widget.create_rectangle(100, 250, 150, 300,
                                                   fill=can_widget.itemcget(Etop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    if (len(Atop) == 1):
                        temp = Etop[0]
                        Atop.append(
                            can_widget.create_rectangle(100, 300, 150, 350,
                                                   fill=can_widget.itemcget(Etop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    if (len(Atop) == 0):
                        temp = Etop[0]
                        Atop.append(
                            can_widget.create_rectangle(100, 350, 150, 400,
                                                   fill=can_widget.itemcget(Etop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                elif (pushvalue.get() == '2'):
                    print("Bstack")
                    print(len(Btop))
                    if (len(Btop) == 3):
                        note.set('Tube 2 is already Full')
                    if (len(Btop) == 2):
                        temp = Etop[0]
                        Btop.append(
                            can_widget.create_rectangle(300, 250, 350, 300,
                                                   fill=can_widget.itemcget(Etop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)

                    if (len(Btop) == 1):
                        temp = Etop[0]
                        Btop.append(
                            can_widget.create_rectangle(300, 300, 350, 350,
                                                   fill=can_widget.itemcget(Etop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    if (len(Btop) == 0):
                        temp = Etop[0]
                        Btop.append(
                            can_widget.create_rectangle(300, 350, 350, 400,
                                                   fill=can_widget.itemcget(Etop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                elif (pushvalue.get() == '3'):
                    print("Cstack")
                    print(len(Ctop))
                    if (len(Ctop) == 3):
                        note.set('Tube 3 is already Full')
                    if (len(Ctop) == 2):
                        temp = Etop[0]
                        Ctop.append(
                            can_widget.create_rectangle(500, 250, 550, 300,
                                                   fill=can_widget.itemcget(Etop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)

                    if (len(Ctop) == 1):
                        temp = Etop[0]
                        Ctop.append(
                            can_widget.create_rectangle(500, 300, 550, 350,
                                                   fill=can_widget.itemcget(Etop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    if (len(Ctop) == 0):
                        temp = Etop[0]
                        Ctop.append(
                            can_widget.create_rectangle(500, 350, 550, 400,
                                                   fill=can_widget.itemcget(Etop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                elif (pushvalue.get() == '4'):
                    print("Dstack")
                    print(len(Dtop))
                    if (len(Dtop) == 3):
                        note.set('Tube 4 is already Full')
                    if (len(Dtop) == 2):
                        temp = Etop[0]
                        Dtop.append(
                            can_widget.create_rectangle(700, 250, 750, 300,
                                                   fill=can_widget.itemcget(Etop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)

                    if (len(Dtop) == 1):
                        temp = Etop[0]
                        Dtop.append(
                            can_widget.create_rectangle(700, 300, 750, 350,
                                                   fill=can_widget.itemcget(Etop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    if (len(Dtop) == 0):
                        temp = Etop[0]
                        Dtop.append(
                            can_widget.create_rectangle(700, 350, 750, 400,
                                                   fill=can_widget.itemcget(Etop.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)

def reset():
    print("Reset Working")


Button(text='  Enter  ',command=enter,borderwidth=3,pady=5).place(x=510,y=75)
b2 = Button(text='  Reset  ',command= reset,borderwidth=3,pady=5).place(x=880,y=700)
note= StringVar()
l3 = Label(root,text='',textvariable=note,padx=10,pady=10,borderwidth=3,relief=SUNKEN,bg='grey',fg='black',font='TimesNewRoman 10').place(x=450,y=130)
label_A = Label(root,text="1",borderwidth=2,bg='white',fg='black',font='TimesNewRoman 8 bold').place(x=116,y=410)
label_B = Label(root,text="2",borderwidth=2,bg='white',fg='black',font='TimesNewRoman 8 bold').place(x=316,y=410)
label_C = Label(root,text="3",borderwidth=2,bg='white',fg='black',font='TimesNewRoman 8 bold').place(x=516,y=410)
label_D = Label(root,text="4",borderwidth=2,bg='white',fg='black',font='TimesNewRoman 8 bold').place(x=716,y=410)
label_E = Label(root,text="5",borderwidth=2,bg='white',fg='black',font='TimesNewRoman 8 bold').place(x=916,y=410)

Atop = []
Btop = []
Ctop = []
Dtop = []
Etop = []
colorR = ['red','red','red']

rect_1= can_widget.create_rectangle(100,200,150,400,outline='white')
Atop.append(can_widget.create_rectangle(100,350,150,400,fill='blue',outline='white'))
Atop.append(can_widget.create_rectangle(100,300,150,350,fill='red',outline='white'))
Atop.append(can_widget.create_rectangle(100,250,150,300,fill='#eec201',outline='white'))
#print(can_widget.itemcget(Atop[1],"fill"))




rect_2= can_widget.create_rectangle(300,200,350,400,outline='white')
Btop.append(can_widget.create_rectangle(300,350,350,400,fill='blue',outline='white'))
Btop.append(can_widget.create_rectangle(300,300,350,350,fill='green',outline='white'))
Btop.append(can_widget.create_rectangle(300,250,350,300,fill='#eec201',outline='white'))



rect_3= can_widget.create_rectangle(500,200,550,400,outline='white')
Ctop.append(can_widget.create_rectangle(500,350,550,400,fill='red',outline='white'))
Ctop.append(can_widget.create_rectangle(500,300,550,350,fill='#eec201',outline='white'))
Ctop.append(can_widget.create_rectangle(500,250,550,300,fill='green',outline='white'))


rect_4= can_widget.create_rectangle(700,200,750,400,outline='white')
Dtop.append(can_widget.create_rectangle(700,350,750,400,fill='blue',outline='white'))
Dtop.append(can_widget.create_rectangle(700,300,750,350,fill='green',outline='white'))
Dtop.append(can_widget.create_rectangle(700,250,750,300,fill='red',outline='white'))

rect_5= can_widget.create_rectangle(900,200,950,400,outline='white')

rect6 = can_widget.create_rectangle(1000, 200, 1050, 400, outline ='white')

#GameOver Module





#HighScore Module
score_widget = Canvas(root, width= canvas_width, height=canvas_height, bg="black", relief = "raised", bd = "8")
score_widget.place(x=1000,y=0)

Score_Label = Label(score_widget, text = "LeaderBoard", font = "Jokerman 20 bold", fg = "yellow", bg="black").place(x=50, y=20)
Score_Grid = ttk.Treeview(score_widget, selectmode="browse")
Score_Grid.place(x=10,y=80)

#Scoreboard Style
style = ttk.Style()
style.theme_use("classic")
# style.configure("Treeview", background="orange", foreground="blue", fieldbackground="#FFFFFF")
style.configure("Treeview.Heading", background="black", foreground="yellow", fieldbackground="#FFFFFF")
style.map('Treeview', background=[('selected', '#00FF04')])

Score_Grid.tag_configure('oddrow', background='orange')
Score_Grid.tag_configure('evenrow', background='white')

##Scrollbar
# verscrlbar = ttk.Scrollbar(window,
#                            orient="vertical",
#                            command=Score_Grid.yview)

# verscrlbar.pack(side='right', fill='x')
# Score_Grid.configure(xscrollcommand=verscrlbar.set)

Score_Grid["columns"] = ("1", "2", "3")
Score_Grid['show'] = 'headings'

Score_Grid.column("1", width=70, anchor='c')
Score_Grid.column("2", width=87, anchor='se')
Score_Grid.column("3", width=104, anchor='se')

Score_Grid.heading("1", text="Rank")
Score_Grid.heading("2", text="Player")
Score_Grid.heading("3", text="Score")

Score_Grid.insert("", 'end', text="L1", tags = ('oddrow'),
             values=("1", "Sh4d0w", "999999"))
Score_Grid.insert("", 'end', text="L2", tags = ('evenrow'),
             values=("2", "D3m0n", "17214"))
Score_Grid.insert("", 'end', text="L3", tags = ('oddrow'),
             values=("3", "Gh0st", "49842"))
Score_Grid.insert("", 'end', text="L4", tags = ('evenrow'),
             values=("4", "Neon", "29723"))
Score_Grid.insert("", 'end', text="L5", tags = ('oddrow'),
             values=("5", "Aakash", "23955"))
Score_Grid.insert("", 'end', text="L6", tags = ('evenrow'),
             values=("6", "Creature", "24524"))
Score_Grid.insert("", 'end', text="L7", tags = ('oddrow'),
             values=("7", "Vladimir", "72745"))
Score_Grid.insert("", 'end', text="L8", tags = ('evenrow'),
             values=("8", "X Æ A-12", "24652"))
Score_Grid.insert("", 'end', text="L9", tags = ('oddrow'),
             values=("9", "Achilles", "4562"))
Score_Grid.insert("", 'end', text="L10", tags = ('evenrow'),
             values=("10", "Mjolnir", "464"))


root.mainloop()