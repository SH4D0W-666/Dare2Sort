import tkinter as t
from tkinter import *
from tkinter import ttk
import PIL
from PIL import Image,ImageTk
import time, datetime, random
import mysql.connector as mysql
points=0
def main():
    global  time_given,f1,go,points
    go=0
    time_given = 180
    # Creating window and canvas
    root = Tk()
    blank_space = " "
    root.title(140 * blank_space + 'DARE TO SORT')
    canvas_width = 1800
    canvas_height = 1000
    root.geometry(f'{canvas_width}x{canvas_height}')
    # root.config(bg='#fff') #69614c
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
            LabelInputtoPop.place(x=320, y=30)
            LabelInputtoPush.place(x=320, y=60)
            popEntry.place(x=470, y=30)
            pushEntry.place(x=470, y=60)
            start_btn.destroy()
            enter_btn.place(x=650, y=45)
            step_label.place(x=800, y=20)
            label_timer.place(x=800,y=50)
            countdown(time_given)
            label_timer.config(bg="black")
            step_label.config(bg="black")
            step.set("Steps: 0")

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
    op_info = StringVar()
    # current info Label
    l3 = Label(f1, text='', textvariable=note, padx=10, pady=10, borderwidth=3, relief=SUNKEN, bg='grey', fg='black',
               font='TimesNewRoman 10')
    l4 = Label(f1, text='', textvariable=op_info, padx=10, pady=10, borderwidth=3, relief=SUNKEN, bg='grey', fg='black',
               font='TimesNewRoman 10')
    # operation info Label
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
    label_timer = Label(f1, text="", textvariable=count, borderwidth=2, fg='red',
                        font='TimesNewRoman 14 bold')
    final_time = Label(f1, text="", textvariable=ftime, borderwidth=2, bg='black', fg='red',
                       font='TimesNewRoman 14 bold')
    step = StringVar()
    step_label = Label(f1, text="", textvariable=step, borderwidth=2, fg='red',
                       font='TimesNewRoman 14 bold')



    ##Functions
    #Function for Database connection
    records = ""
    def createdb():
        conn = mysql.connect(host="localhost", user="root", password="")
        cur = conn.cursor()
        cur.execute("CREATE DATABASE GameScore")
        cur.execute("commit")
        conn.close()
    def createtable():
        conn = mysql.connect(host="localhost", user="root", password="",database="GameScore")
        cur = conn.cursor()
        cur.execute("CREATE TABLE score ( id int(100) NOT NULL auto_increment, Name varchar(100), Points varchar(100), PRIMARY KEY(id) );")
        cur.execute("commit")
        conn.close()
    def insert(namevalue, point):
        conn = mysql.connect(host="localhost", user="root", password="", database="GameScore")
        cur = conn.cursor()
        cur.execute("INSERT INTO score (Name,Points) VALUES (%s,%s)", (namevalue, point))
        print("working")
        cur.execute("commit")
        conn.close()

    def fetch():
        global records, x
        conn = mysql.connect(host="localhost", user="root", password="", database="GameScore")
        cur = conn.cursor()
        cur.execute("SELECT * from score order by Points DESC")
        records = cur.fetchall()
        print(records)
        i = 1
        for x in records:
            if (i % 2 != 0):
                Score_Grid.insert("", 'end', text="L1", tags=('oddrow'),values=(i, x[1], x[2]))
            if (i % 2 == 0):
                Score_Grid.insert("", 'end', text="L2", tags=('evenrow'),values=(i, x[1], x[2]))
            i += 1
        cur.execute("commit")
        conn.close()

    # function for steps and time
    global win
    win=0
    def countdown(t):
        global time_taken,go,win,points
        if (count.get() == 'Time Left: 00:00' and win!=1):
            label_timer.destroy()
            final_time.place(x=800, y=50)
            ftime.set("Time Left: 00:00")
            enter_btn['state'] = "disabled"
            note.set("Game Over!! You Lose")
            a = time.strptime(time_taken, "%M:%S")
            time_taken = datetime.timedelta(minutes=a.tm_min, seconds=a.tm_sec).seconds
            points = max(0,500-steps_count*10)
            go = 1
            print("Lose!")
            print("Player: "+ namevalue.get())
            print(points)
            insert(namevalue.get(),points)
        # change text in label
        mins, secs = divmod(t, 60)
        time_taken = '{:02d}:{:02d}'.format(mins, secs)
        if t >= 0:
            count.set("Time Left: " + time_taken)
            # call countdown again after 1000ms (1s)
            root.after(1000, countdown, t - 1)

    # function checking for Game Over
    tube_full = []
    tube_full = [0, 0, 0, 0, 0]
    def check(lst):
        global go, time_taken, time_given,win
        l3.place(x=450, y=130)
        l4.place(x=280,y=510)
        if (len(lst) == 3):
            ele = can_widget.itemcget(lst[0], "fill")
            chk = True
            mycolorlst = [can_widget.itemcget(lst[0], "fill"), can_widget.itemcget(lst[1], "fill"),
                          can_widget.itemcget(lst[2], "fill")]
            for item in mycolorlst:
                if ele != item:
                    chk = False
                    if (chk == False):
                        if (lst == Atop):
                            tube_full[0] = 0
                        elif (lst == Btop):
                            tube_full[1] = 0
                        elif (lst == Ctop):
                            tube_full[2] = 0
                        elif (lst == Dtop):
                            tube_full[3] = 0
                        elif (lst == Etop):
                            tube_full[4] = 0
                    break
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
            final_time.place(x=800, y=50)
            ftime.set(tem)
            note.set("Game Over, You Win!!")
            a = time.strptime(str(time_taken), "%M:%S")
            time_taken = datetime.timedelta(minutes=a.tm_min, seconds=a.tm_sec).seconds
            win=1
            points = time_taken * 100 - steps_count * 10
            insert(namevalue.get(), points)
            print(points)
            print("win")
            print("Player: " + namevalue.get())

    # function for moving liquid from one stack to another\
    global  steps_count
    steps_count=0
    def enter():
        global steps_count,go
        go=0
        i=x=y=0
        popstack = ''
        pushstack = ''
        if(popvalue.get()!="" or pushvalue.get()!=""):
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

        if (pushvalue.get() != "" or popvalue.get() != ""):
            if (pushvalue.get() == '1'):
                pushstack = Atop
                x=y=0
            elif (pushvalue.get() == '2'):
                pushstack = Btop
                x=y=200
            elif (pushvalue.get() == '3'):
                pushstack = Ctop
                x=y=400
            elif (pushvalue.get() == '4'):
                pushstack = Dtop
                x=y=600
            elif (pushvalue.get() == '5'):
                pushstack = Etop
                x=y=800

        if(pushvalue.get() != "" or popvalue.get() != ""):
            if(len(popstack)==3):
                i = 2
            elif(len(popstack)==2):
                i = 1
            elif (len(popstack) == 1):
                i = 0

            note.set('Game on')
            if (len(popstack) == 0):
                note.set(f'Tube {popvalue.get()} is Already Empty')
                print('Already Empty')
            else:
                if (len(popstack)!=0):
                    if(len(pushstack)==3 and pushstack!=popstack):
                        note.set(f'Tube {pushvalue.get()} is already full')
                    elif(len(pushstack)==2 and pushstack!=popstack):
                        steps_count=steps_count+1
                        temp = popstack[i]
                        pushstack.append(can_widget.create_rectangle(x+100, 250, y+150, 300,fill=can_widget.itemcget(popstack.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    elif (len(pushstack) == 1 and pushstack!=popstack):
                        steps_count = steps_count + 1
                        temp = popstack[i]
                        pushstack.append(can_widget.create_rectangle(x+100, 300, y+150, 350,fill=can_widget.itemcget(popstack.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)
                    elif (len(pushstack) == 0 and pushstack!=popstack):
                        steps_count = steps_count + 1
                        temp = popstack[i]
                        pushstack.append(can_widget.create_rectangle(x+100, 350, y+150, 400,fill=can_widget.itemcget(popstack.pop(), "fill"),outline='white'))
                        can_widget.delete(temp)

                if pushstack==popstack:
                    op_info.set(f'Please enter a valid input                                        ')
                    l4.place(x=320, y=510)
                else:
                    op_info.set(f'Element Popped from Top of Tube {popvalue.get()} and Pushed to Top of Tube {pushvalue.get()}')
                    l4.place(x=280, y=510)

                step.set("Steps: " + str(steps_count))
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

    # Buttons
    enter_btn = Button(text='  Enter  ', command=enter, state=ACTIVE, borderwidth=3, pady=5)
    reset_btn = Button(text='  Reset  ', command=reset, borderwidth=3, pady=5).place(x=880, y=580)

    # Creating all canvas widgets and stacks
    Atop = []
    Btop = []
    Ctop = []
    Dtop = []
    Etop = []

    main_bottle = [Atop,Btop,Ctop,Dtop,Etop]

    ways = [[0, 3, 3, 3, 3], [1, 2, 3, 3, 3], [2, 2, 2, 3, 3]]

    temp_items = random.sample(ways[random.randint(0, 2)], 5)

    colors = ['blue','red','#eec201','green','blue','red','green','blue','red','#eec201','green','#eec201']

    bx,by = 100,350

    for i in range(5):
        for j in range(temp_items[i]):
            color_select = random.choice(colors)
            main_bottle[i].append(can_widget.create_rectangle(bx, by, bx+50, by+50, fill=color_select, outline='white'))
            colors.remove(color_select)
            by-=50
        bx+=200
        by=350

    rect_1 = can_widget.create_rectangle(100, 230, 150, 400, outline='white')
    can_widget.create_line(100,230,150,230,fill="#36332c")

    rect_2 = can_widget.create_rectangle(300, 230, 350, 400, outline='white')
    can_widget.create_line(300, 230, 150, 230, fill="#36332c")

    rect_3 = can_widget.create_rectangle(500, 230, 550, 400, outline='white')
    can_widget.create_line(500, 230, 150, 230, fill="#36332c")

    rect_4 = can_widget.create_rectangle(700, 230, 750, 400, outline='white')
    can_widget.create_line(700, 230, 150, 230, fill="#36332c")

    rect_5 = can_widget.create_rectangle(900, 230, 950, 400, outline='white')
    can_widget.create_line(900, 230, 150, 230, fill="#36332c")

    rect6 = can_widget.create_rectangle(1000, 230, 1050, 400, outline='white')
    can_widget.create_line(1000, 230, 150, 230, fill="#36332c")


    # HighScore Module
    score_widget = Canvas(root, width=canvas_width, height=canvas_height, bg="black", relief="raised")
    score_widget.place(x=1000, y=0)

    Instruction_Label = Label(score_widget, text="Instructions", font="Jokerman 20 bold", fg="yellow", bg="black")
    Instruction_Label.place(x=180, y=20)

    Label(score_widget, text="1.   Enter bottle number from which you want to pop the liquid.", font="Helvetica 12 bold", fg="white", bg="black").place(x=45,y=80)


    Label(score_widget, text="2.   Enter bottle number to which you want to append the liquid.", font="Helvetica 12 bold", fg="white", bg="black").place(x=45,y=120)
    Label(score_widget, text="3.   Only the Liquid which is on top of tube can be appended.", font="Helvetica 12 bold",fg="white", bg="black").place(x=45, y=160)
    Label(score_widget, text="4.   Only the Liquid which is on top of tube can be appended.", font="Helvetica 12 bold",fg="white", bg="black").place(x=45, y=200)
    Label(score_widget, text="5.   To gain maximum points you need to complete the game as ", font="Helvetica 12 bold",fg="white", bg="black").place(x=45, y=240)
    Label(score_widget, text="\tearly as possible with less number of steps.", font="Helvetica 12 bold",fg="white", bg="black").place(x=45, y=265)

    Score_Label = Label(score_widget, text="LeaderBoard", font="Jokerman 20 bold", fg="yellow", bg="black").place(x=180,y=370)
    global Score_Grid
    Score_Grid = ttk.Treeview(score_widget, selectmode="browse")
    Score_Grid.place(x=30, y=420)

    # Scoreboard Style
    style = ttk.Style()
    style.theme_use("classic")
    # style.configure("Treeview", background="orange", foreground="blue", fieldbackground="#FFFFFF")
    style.configure("Treeview.Heading", background="black", foreground="yellow", fieldbackground="#FFFFFF")
    style.map('Treeview', background=[('selected', '#00FF04')])

    Score_Grid.tag_configure('oddrow', background='orange')
    Score_Grid.tag_configure('evenrow', background='white')

    Score_Grid["columns"] = ("1", "2", "3")
    Score_Grid['show'] = 'headings'

    Score_Grid.column("1", width=140, anchor='c')
    Score_Grid.column("2", width=160, anchor='c')
    Score_Grid.column("3", width=160, anchor='c')

    Score_Grid.heading("1", text="Rank")
    Score_Grid.heading("2", text="Player")
    Score_Grid.heading("3", text="Score")

    #Run this 2 Functions once at the start of game
    # createdb()
    # createtable()
    fetch()
    root.mainloop()

main()