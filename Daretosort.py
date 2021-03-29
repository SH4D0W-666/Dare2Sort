import tkinter as t
from tkinter import *
from tkinter import ttk
import PIL
from PIL import Image,ImageTk
import time, datetime


def main():
    global  time_given,f1,go
    go=0
    time_given = 180
    # Creating window and canvas
    root = Tk()
    blank_space = " "
    root.title(140 * blank_space + 'DARE TO SORT')
    canvas_width = 1000
    canvas_height = 6000
    root.geometry(f'{canvas_width}x{canvas_height}')
    root.config(bg='#69614c')
    f1 = Frame(root, borderwidth=6, width=canvas_width, height=canvas_height)
    f1.place(x=0, y=0)
    image2 = Image.open('assets//DTS_bg.jpg')
    image1 = ImageTk.PhotoImage(image2.resize((1000, 1150), Image.ANTIALIAS))
    can_widget = Canvas(f1, width=canvas_width, height=canvas_height, bg="#36332c")
    can_widget.place(x=0, y=0)
    #can_widget.create_image(0, 0, image=image1, anchor='nw')      #To add Image Just Remove this comment

    #function for taking Name input and starting game
    def start():
        if (namevalue.get() != ""):
            Name_label.destroy()
            nameEntry.destroy()
            LabelInputtoPop.place(x=400, y=10)
            LabelInputtoPush.place(x=400, y=40)
            popEntry.place(x=570, y=10)
            pushEntry.place(x=570, y=40)
            start_btn.destroy()
            enter_btn.place(x=510, y=75)
            countdown(time_given)
            label_timer.config(bg="black")
            step_label.config(bg="black")

    # Labels and Entry
    Name_label = Label(f1, text="Enter Your Name: ", fg='black', font='comicsans 10')
    Name_label.place(x=400, y=25)
    namevalue = StringVar()
    nameEntry = Entry(f1, textvariable=namevalue)
    nameEntry.place(x=570, y=25)
    start_btn = Button(text='  Start  ', command=start, borderwidth=3, pady=5)
    start_btn.place(x=510, y=75)
    LabelInputtoPop = Label(f1, text="Source Bottle: ", fg='black', font='comicsans 10')
    LabelInputtoPush = Label(f1, text="Destination Bottle: ", font='comicsans 10')
    popvalue = StringVar()
    pushvalue = StringVar()
    popEntry = Entry(f1, textvariable=popvalue)
    pushEntry = Entry(f1, textvariable=pushvalue)
    note = StringVar()
    # current info Label
    l3 = Label(f1, text='', textvariable=note, padx=10, pady=10, borderwidth=3, relief=SUNKEN, bg='grey', fg='black',
               font='TimesNewRoman 10').place(x=450, y=130)
    # labels to identify bottle number
    label_A = Label(f1, text="1", borderwidth=2, bg='white', fg='black', font='TimesNewRoman 8 bold').place(x=116,
                                                                                                            y=410)
    label_B = Label(f1, text="2", borderwidth=2, bg='white', fg='black', font='TimesNewRoman 8 bold').place(x=316,
                                                                                                            y=410)
    label_C = Label(f1, text="3", borderwidth=2, bg='white', fg='black', font='TimesNewRoman 8 bold').place(x=516,
                                                                                                            y=410)
    label_D = Label(f1, text="4", borderwidth=2, bg='white', fg='black', font='TimesNewRoman 8 bold').place(x=716,
                                                                                                            y=410)
    label_E = Label(f1, text="5", borderwidth=2, bg='white', fg='black', font='TimesNewRoman 8 bold').place(x=916,
                                                                                                            y=410)
    # Time and Steps Label
    count = StringVar()
    ftime = StringVar()
    label_timer = Label(f1, text="", textvariable=count, borderwidth=2, bg="#36332c", fg='red',
                        font='TimesNewRoman 14 bold')
    label_timer.place(x=800, y=35)
    final_time = Label(f1, text="", textvariable=ftime, borderwidth=2, bg='black', fg='red',
                       font='TimesNewRoman 14 bold')
    step = StringVar()
    step_label = Label(f1, text="", textvariable=step, borderwidth=2, bg="#36332c", fg='red',
                       font='TimesNewRoman 14 bold')
    step_label.place(x=800, y=5)

    # function for steps and time
    def countdown(t):
        global time_taken,go
        if (count.get() == 'Time Left: 00:01'):
            label_timer.destroy()
            final_time.place(x=800, y=35)
            ftime.set("Time Left: 00:00")
            enter_btn['state'] = "disabled"
            note.set("Game Over!! You Lose")
            a = time.strptime(time_taken, "%M:%S")
            time_taken = time_given - datetime.timedelta(minutes=a.tm_min, seconds=a.tm_sec).seconds
            go = 1
            print("Lose!")
            print("Player: "+ namevalue.get())
            print("Steps: ",steps_count)
            print("Time Taken: ",time_taken)
        # change text in label
        mins, secs = divmod(t, 60)
        time_taken = '{:02d}:{:02d}'.format(mins, secs)
        if t > 0:
            count.set("Time Left: " + time_taken)
            step.set("Steps: " + str(steps_count))
            # call countdown again after 1000ms (1s)
            root.after(1000, countdown, t - 1)

    # function checking for Game Over
    tube_full = []
    tube_full = [0, 0, 0, 0, 0]

    def check(lst):
        global go, time_taken, time_given
        if (len(lst) == 3):
            ele = can_widget.itemcget(lst[0], "fill")
            chk = True
            mycolorlst = [can_widget.itemcget(lst[0], "fill"), can_widget.itemcget(lst[1], "fill"),
                          can_widget.itemcget(lst[2], "fill")]
            for item in mycolorlst:
                if ele != item:
                    chk = False
                    break;
            if (chk == True):
                if (lst == Atop):
                    tube_full[0] = 1
                elif (lst == Btop):
                    tube_full[1] = 1
                elif (lst == Ctop):
                    tube_full[2] = 1
                elif (lst == Dtop):
                    tube_full[3] = 1
                elif (lst == Etop):
                    tube_full[4] = 1
        if tube_full.count(1) == 4:
            go = 1
            enter_btn['state'] = "disabled"
            tem = count.get()
            label_timer.destroy()
            final_time.place(x=800, y=35)
            ftime.set(tem)
            note.set("Game Over, You Win!!")
            a = time.strptime(time_taken, "%M:%S")
            time_taken = time_given - datetime.timedelta(minutes=a.tm_min, seconds=a.tm_sec).seconds
            go = 1
            print("win")
            print("Player: " + namevalue.get())
            print("Steps: ", steps_count)
            print("Time Taken: ", time_taken)

    # function for moving liquid from one stack to another\
    global  steps_count
    steps_count=0
    def enter():
        global steps_count,go
        go=0
        steps_count = steps_count + 1
        popstack = ''
        if (popvalue.get() == '1'):
            popstack = Atop
        elif (popvalue.get() == '2'):
            popstack = Btop
        elif (popvalue.get() == '3'):
            popstack = Ctop
        elif (popvalue.get() == '4'):
            popstack = Dtop
        elif (popvalue.get() == '5'):
            popstack = Etop

        note.set('Game on')
        if (len(popstack) == 0):
            note.set(f'Tube {popvalue.get()} is Already Empty')
            print('Already Empty')
        else:
            if (len(popstack) == 3):
                if (popvalue.get() != '2' and pushvalue.get() == '2'):
                    if (len(Btop) == 3):
                        note.set('Tube 2 is already Full')
                        print("Tube Full")
                    if (len(Btop) == 2):
                        temp = popstack[2]
                        Btop.append(can_widget.create_rectangle(300, 250, 350, 300,
                                                                fill=can_widget.itemcget(popstack.pop(), "fill"),
                                                                outline='white'))
                        can_widget.delete(temp)
                    if (len(Btop) == 1):
                        temp = popstack[2]
                        Btop.append(can_widget.create_rectangle(300, 300, 350, 350,
                                                                fill=can_widget.itemcget(popstack.pop(), "fill"),
                                                                outline='white'))
                        can_widget.delete(temp)
                    if (len(Btop) == 0):
                        temp = popstack[2]
                        Btop.append(can_widget.create_rectangle(300, 350, 350, 400,
                                                                fill=can_widget.itemcget(popstack.pop(), "fill"),
                                                                outline='white'))
                        can_widget.delete(temp)
                elif (popvalue.get() != '1' and pushvalue.get() == '1'):
                    if (len(Atop) == 3):
                        note.set('Tube 1 is already Full')
                    if (len(Atop) == 2):
                        temp = popstack[2]
                        Atop.append(can_widget.create_rectangle(100, 250, 150, 300,
                                                                fill=can_widget.itemcget(popstack.pop(), "fill"),
                                                                outline='white'))
                        can_widget.delete(temp)
                    if (len(Atop) == 1):
                        temp = popstack[2]
                        Atop.append(can_widget.create_rectangle(100, 300, 150, 350,
                                                                fill=can_widget.itemcget(popstack.pop(), "fill"),
                                                                outline='white'))
                        can_widget.delete(temp)
                    if (len(Atop) == 0):
                        temp = popstack[2]
                        Atop.append(can_widget.create_rectangle(100, 350, 150, 400,
                                                                fill=can_widget.itemcget(popstack.pop(), "fill"),
                                                                outline='white'))
                        can_widget.delete(temp)
                elif (popvalue.get() != '3' and pushvalue.get() == '3'):
                    if (len(Ctop) == 3):
                        note.set('Tube 3 is already Full')
                    if (len(Ctop) == 2):
                        temp = popstack[2]
                        Ctop.append(can_widget.create_rectangle(500, 250, 550, 300,
                                                                fill=can_widget.itemcget(popstack.pop(), "fill"),
                                                                outline='white'))
                        can_widget.delete(temp)
                    if (len(Ctop) == 1):
                        temp = popstack[2]
                        Ctop.append(can_widget.create_rectangle(500, 300, 550, 350,
                                                                fill=can_widget.itemcget(popstack.pop(), "fill"),
                                                                outline='white'))
                        can_widget.delete(temp)
                    if (len(Ctop) == 0):
                        temp = popstack[2]
                        Ctop.append(can_widget.create_rectangle(500, 350, 550, 400,
                                                                fill=can_widget.itemcget(popstack.pop(), "fill"),
                                                                outline='white'))
                        can_widget.delete(temp)
                elif (popvalue.get() != '4' and pushvalue.get() == '4'):
                    if (len(Dtop) == 3):
                        note.set('Tube 4 is already Full')
                    if (len(Dtop) == 2):
                        temp = popstack[2]
                        Dtop.append(can_widget.create_rectangle(700, 250, 750, 300,
                                                                fill=can_widget.itemcget(popstack.pop(), "fill"),
                                                                outline='white'))
                        can_widget.delete(temp)
                    if (len(Dtop) == 1):
                        temp = popstack[2]
                        Dtop.append(can_widget.create_rectangle(700, 300, 750, 350,
                                                                fill=can_widget.itemcget(popstack.pop(), "fill"),
                                                                outline='white'))
                        can_widget.delete(temp)
                    if (len(Dtop) == 0):
                        temp = popstack[2]
                        Dtop.append(can_widget.create_rectangle(700, 350, 750, 400,
                                                                fill=can_widget.itemcget(popstack.pop(), "fill"),
                                                                outline='white'))
                        can_widget.delete(temp)
                elif (popvalue.get() != '5' and pushvalue.get() == '5'):
                    if (len(Etop) == 3):
                        note.set('Tube 5 is already Full')
                    if (len(Etop) == 2):
                        temp = popstack[2]
                        Etop.append(can_widget.create_rectangle(900, 250, 950, 300,
                                                                fill=can_widget.itemcget(popstack.pop(), "fill"),
                                                                outline='white'))
                        can_widget.delete(temp)
                    if (len(Etop) == 1):
                        temp = popstack[2]
                        Etop.append(can_widget.create_rectangle(900, 300, 950, 350,
                                                                fill=can_widget.itemcget(popstack.pop(), "fill"),
                                                                outline='white'))
                        can_widget.delete(temp)
                    if (len(Etop) == 0):
                        temp = popstack[2]
                        Etop.append(can_widget.create_rectangle(900, 350, 950, 400,
                                                                fill=can_widget.itemcget(popstack.pop(), "fill"),
                                                                outline='white'))
                        can_widget.delete(temp)
            elif (len(popstack) == 2):
                if (popvalue.get() != "2" and pushvalue.get() == '2'):
                    if (len(Btop) == 3):
                        note.set('Tube 2 is already Full')
                    if (len(Btop) == 2):
                        temp = popstack[1]
                        Btop.append(can_widget.create_rectangle(300, 250, 350, 300,
                                                                fill=can_widget.itemcget(popstack.pop(), "fill"),
                                                                outline='white'))
                        can_widget.delete(temp)
                    if (len(Btop) == 1):
                        temp = popstack[1]
                        Btop.append(can_widget.create_rectangle(300, 300, 350, 350,
                                                                fill=can_widget.itemcget(popstack.pop(), "fill"),
                                                                outline='white'))
                        can_widget.delete(temp)
                    if (len(Btop) == 0):
                        temp = popstack[1]
                        Btop.append(can_widget.create_rectangle(300, 350, 350, 400,
                                                                fill=can_widget.itemcget(popstack.pop(), "fill"),
                                                                outline='white'))
                        can_widget.delete(temp)
                elif (popvalue.get() != '1' and pushvalue.get() == '1'):
                    if (len(Atop) == 3):
                        note.set('Tube 1 is already Full')
                    if (len(Atop) == 2):
                        temp = popstack[1]
                        Atop.append(can_widget.create_rectangle(100, 250, 150, 300,
                                                                fill=can_widget.itemcget(popstack.pop(), "fill"),
                                                                outline='white'))
                        can_widget.delete(temp)
                    if (len(Atop) == 1):
                        temp = popstack[1]
                        Atop.append(can_widget.create_rectangle(100, 300, 150, 350,
                                                                fill=can_widget.itemcget(popstack.pop(), "fill"),
                                                                outline='white'))
                        can_widget.delete(temp)
                    if (len(Atop) == 0):
                        temp = popstack[1]
                        Atop.append(can_widget.create_rectangle(100, 350, 150, 400,
                                                                fill=can_widget.itemcget(popstack.pop(), "fill"),
                                                                outline='white'))
                        can_widget.delete(temp)
                elif (popvalue.get() != '3' and pushvalue.get() == '3'):
                    if (len(Ctop) == 3):
                        note.set('Tube 3 is already Full')
                    if (len(Ctop) == 2):
                        temp = popstack[1]
                        Ctop.append(can_widget.create_rectangle(500, 250, 550, 300,
                                                                fill=can_widget.itemcget(popstack.pop(), "fill"),
                                                                outline='white'))
                        can_widget.delete(temp)
                    if (len(Ctop) == 1):
                        temp = popstack[1]
                        Ctop.append(can_widget.create_rectangle(500, 300, 550, 350,
                                                                fill=can_widget.itemcget(popstack.pop(), "fill"),
                                                                outline='white'))
                        can_widget.delete(temp)
                    if (len(Ctop) == 0):
                        temp = popstack[1]
                        Ctop.append(can_widget.create_rectangle(500, 350, 550, 400,
                                                                fill=can_widget.itemcget(popstack.pop(), "fill"),
                                                                outline='white'))
                        can_widget.delete(temp)
                elif (popvalue.get() != '4' and pushvalue.get() == '4'):
                    if (len(Dtop) == 3):
                        note.set('Tube 4 is already Full')
                    if (len(Dtop) == 2):
                        temp = popstack[1]
                        Dtop.append(can_widget.create_rectangle(700, 250, 750, 300,
                                                                fill=can_widget.itemcget(popstack.pop(), "fill"),
                                                                outline='white'))
                        can_widget.delete(temp)
                    if (len(Dtop) == 1):
                        temp = popstack[1]
                        Dtop.append(can_widget.create_rectangle(700, 300, 750, 350,
                                                                fill=can_widget.itemcget(popstack.pop(), "fill"),
                                                                outline='white'))
                        can_widget.delete(temp)
                    if (len(Dtop) == 0):
                        temp = popstack[1]
                        Dtop.append(can_widget.create_rectangle(700, 350, 750, 400,
                                                                fill=can_widget.itemcget(popstack.pop(), "fill"),
                                                                outline='white'))
                        can_widget.delete(temp)
                elif (popvalue.get() != '5' and pushvalue.get() == '5'):
                    if (len(Etop) == 3):
                        note.set('Tube 5 is already Full')
                    if (len(Etop) == 2):
                        temp = popstack[1]
                        Etop.append(can_widget.create_rectangle(900, 250, 950, 300,
                                                                fill=can_widget.itemcget(popstack.pop(), "fill"),
                                                                outline='white'))
                        can_widget.delete(temp)
                    if (len(Etop) == 1):
                        temp = popstack[1]
                        Etop.append(can_widget.create_rectangle(900, 300, 950, 350,
                                                                fill=can_widget.itemcget(popstack.pop(), "fill"),
                                                                outline='white'))
                        can_widget.delete(temp)
                    if (len(Etop) == 0):
                        temp = popstack[1]
                        Etop.append(can_widget.create_rectangle(900, 350, 950, 400,
                                                                fill=can_widget.itemcget(popstack.pop(), "fill"),
                                                                outline='white'))
                        can_widget.delete(temp)
            elif (len(popstack) == 1):
                if (popvalue.get() != '2' and pushvalue.get() == '2'):
                    if (len(Btop) == 3):
                        note.set('Tube 2 is already Full')
                    if (len(Btop) == 2):
                        temp = popstack[0]
                        Btop.append(can_widget.create_rectangle(300, 250, 350, 300,
                                                                fill=can_widget.itemcget(popstack.pop(), "fill"),
                                                                outline='white'))
                        can_widget.delete(temp)
                    if (len(Btop) == 1):
                        temp = popstack[0]
                        print(can_widget.itemcget(Atop[0], "fill"))
                        Btop.append(can_widget.create_rectangle(300, 300, 350, 350,
                                                                fill=can_widget.itemcget(popstack.pop(), "fill"),
                                                                outline='white'))
                        can_widget.delete(temp)
                    if (len(Btop) == 0):
                        temp = popstack[0]
                        Btop.append(can_widget.create_rectangle(300, 350, 350, 400,
                                                                fill=can_widget.itemcget(popstack.pop(), "fill"),
                                                                outline='white'))
                        can_widget.delete(temp)
                elif (popvalue.get() != '1' and pushvalue.get() == '1'):
                    if (len(Atop) == 3):
                        note.set('Tube 1 is already Full')
                    if (len(Atop) == 2):
                        temp = popstack[0]
                        Atop.append(can_widget.create_rectangle(100, 250, 150, 300,
                                                                fill=can_widget.itemcget(popstack.pop(), "fill"),
                                                                outline='white'))
                        can_widget.delete(temp)
                    if (len(Atop) == 1):
                        temp = popstack[0]
                        Atop.append(can_widget.create_rectangle(100, 300, 150, 350,
                                                                fill=can_widget.itemcget(popstack.pop(), "fill"),
                                                                outline='white'))
                        can_widget.delete(temp)
                    if (len(Atop) == 0):
                        temp = popstack[0]
                        Atop.append(can_widget.create_rectangle(100, 350, 150, 400,
                                                                fill=can_widget.itemcget(popstack.pop(), "fill"),
                                                                outline='white'))
                        can_widget.delete(temp)
                elif (popvalue.get() != '3' and pushvalue.get() == '3'):
                    if (len(Ctop) == 3):
                        note.set('Tube 3 is already Full')
                    if (len(Ctop) == 2):
                        temp = popstack[0]
                        Ctop.append(can_widget.create_rectangle(500, 250, 550, 300,
                                                                fill=can_widget.itemcget(popstack.pop(), "fill"),
                                                                outline='white'))
                        can_widget.delete(temp)
                    if (len(Ctop) == 1):
                        temp = popstack[0]
                        Ctop.append(can_widget.create_rectangle(500, 300, 550, 350,
                                                                fill=can_widget.itemcget(popstack.pop(), "fill"),
                                                                outline='white'))
                        can_widget.delete(temp)
                    if (len(Ctop) == 0):
                        temp = popstack[0]
                        Ctop.append(can_widget.create_rectangle(500, 350, 550, 400,
                                                                fill=can_widget.itemcget(popstack.pop(), "fill"),
                                                                outline='white'))
                        can_widget.delete(temp)
                elif (popvalue.get() != '4' and pushvalue.get() == '4'):
                    if (len(Dtop) == 3):
                        note.set('Tube 4 is already Full')
                    if (len(Dtop) == 2):
                        temp = popstack[0]
                        Dtop.append(can_widget.create_rectangle(700, 250, 750, 300,
                                                                fill=can_widget.itemcget(popstack.pop(), "fill"),
                                                                outline='white'))
                        can_widget.delete(temp)
                    if (len(Dtop) == 1):
                        temp = popstack[0]
                        Dtop.append(can_widget.create_rectangle(700, 300, 750, 350,
                                                                fill=can_widget.itemcget(popstack.pop(), "fill"),
                                                                outline='white'))
                        can_widget.delete(temp)
                    if (len(Dtop) == 0):
                        temp = popstack[0]
                        Dtop.append(can_widget.create_rectangle(700, 350, 750, 400,
                                                                fill=can_widget.itemcget(popstack.pop(), "fill"),
                                                                outline='white'))
                        can_widget.delete(temp)
                elif (popvalue.get() != '5' and pushvalue.get() == '5'):
                    if (len(Etop) == 3):
                        note.set('Tube 5 is already Full')
                    if (len(Etop) == 2):
                        temp = popstack[0]
                        Etop.append(can_widget.create_rectangle(900, 250, 950, 300,
                                                                fill=can_widget.itemcget(popstack.pop(), "fill"),
                                                                outline='white'))
                        can_widget.delete(temp)
                    if (len(Etop) == 1):
                        temp = popstack[0]
                        Etop.append(can_widget.create_rectangle(900, 300, 950, 350,
                                                                fill=can_widget.itemcget(popstack.pop(), "fill"),
                                                                outline='white'))
                        can_widget.delete(temp)
                    if (len(Etop) == 0):
                        temp = popstack[0]
                        Etop.append(can_widget.create_rectangle(900, 350, 950, 400,
                                                                fill=can_widget.itemcget(popstack.pop(), "fill"),
                                                                outline='white'))
                        can_widget.delete(temp)
        if go != 1:
            check(Atop)
        if go != 1:
            check(Btop)
        if go != 1:
            check(Ctop)
        if go != 1:
            check(Dtop)
        if go != 1:
            check(Etop)

    # Reset Function
    def reset():

        root.destroy()
        main()
        print("Reset Working")

    # Buttons
    enter_btn = Button(text='  Enter  ', command=enter, state=ACTIVE, borderwidth=3, pady=5)
    reset_btn = Button(text='  Reset  ', command=reset, borderwidth=3, pady=5).place(x=880, y=700)

    # Creating all canvas widgets and stacks
    Atop = []
    Btop = []
    Ctop = []
    Dtop = []
    Etop = []

    rect_1 = can_widget.create_rectangle(100, 200, 150, 400, outline='white')
    Atop.append(can_widget.create_rectangle(100, 350, 150, 400, fill='blue', outline='white'))
    Atop.append(can_widget.create_rectangle(100, 300, 150, 350, fill='red', outline='white'))
    Atop.append(can_widget.create_rectangle(100, 250, 150, 300, fill='#eec201', outline='white'))

    rect_2 = can_widget.create_rectangle(300, 200, 350, 400, outline='white')
    Btop.append(can_widget.create_rectangle(300, 350, 350, 400, fill='green', outline='white'))
    Btop.append(can_widget.create_rectangle(300, 300, 350, 350, fill='green', outline='white'))
    Btop.append(can_widget.create_rectangle(300, 250, 350, 300, fill='#eec201', outline='white'))

    rect_3 = can_widget.create_rectangle(500, 200, 550, 400, outline='white')
    Ctop.append(can_widget.create_rectangle(500, 350, 550, 400, fill='red', outline='white'))
    Ctop.append(can_widget.create_rectangle(500, 300, 550, 350, fill='green', outline='white'))
    Ctop.append(can_widget.create_rectangle(500, 250, 550, 300, fill='#eec201', outline='white'))

    rect_4 = can_widget.create_rectangle(700, 200, 750, 400, outline='white')
    Dtop.append(can_widget.create_rectangle(700, 350, 750, 400, fill='blue', outline='white'))
    Dtop.append(can_widget.create_rectangle(700, 300, 750, 350, fill='blue', outline='white'))
    Dtop.append(can_widget.create_rectangle(700, 250, 750, 300, fill='red', outline='white'))

    rect_5 = can_widget.create_rectangle(900, 200, 950, 400, outline='white')

    rect6 = can_widget.create_rectangle(1000, 200, 1050, 400, outline='white')

    # HighScore Module
    score_widget = Canvas(root, width=canvas_width, height=canvas_height, bg="black", relief="raised", bd="8")
    score_widget.place(x=1000, y=0)

    Score_Label = Label(score_widget, text="LeaderBoard", font="Jokerman 20 bold", fg="yellow", bg="black").place(x=50,
                                                                                                                  y=20)
    Score_Grid = ttk.Treeview(score_widget, selectmode="browse")
    Score_Grid.place(x=10, y=80)

    # Scoreboard Style
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

    Score_Grid.insert("", 'end', text="L1", tags=('oddrow'),
                      values=("1", "Sh4d0w", "999999"))
    Score_Grid.insert("", 'end', text="L2", tags=('evenrow'),
                      values=("2", "D3m0n", "17214"))
    Score_Grid.insert("", 'end', text="L3", tags=('oddrow'),
                      values=("3", "Gh0st", "49842"))
    Score_Grid.insert("", 'end', text="L4", tags=('evenrow'),
                      values=("4", "Neon", "29723"))
    Score_Grid.insert("", 'end', text="L5", tags=('oddrow'),
                      values=("5", "Aakash", "23955"))
    Score_Grid.insert("", 'end', text="L6", tags=('evenrow'),
                      values=("6", "Creature", "24524"))
    Score_Grid.insert("", 'end', text="L7", tags=('oddrow'),
                      values=("7", "Vladimir", "72745"))
    Score_Grid.insert("", 'end', text="L8", tags=('evenrow'),
                      values=("8", "X Æ A-12", "24652"))
    Score_Grid.insert("", 'end', text="L9", tags=('oddrow'),
                      values=("9", "Achilles", "4562"))
    Score_Grid.insert("", 'end', text="L10", tags=('evenrow'),
                      values=("10", "Mjolnir", "464"))

    root.mainloop()

main()