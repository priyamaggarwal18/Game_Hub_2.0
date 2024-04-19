from tkinter import *
from PIL import Image,ImageTk
import random
import time
import pygame
import sqlite3
from tkVideoPlayer import TkinterVideo

startTime=time.time()
sonar=True
pomodoro=True
root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry("955x601")
root.title("Code Blasters 💣")
root.iconbitmap('fav.ico')

videoplayer = TkinterVideo(master=root, scaled=True)
videoplayer.load("codeBlasters.gif")
videoplayer.pack(expand=True, fill="both")

videoplayer.play() # play the video
root.after(4900,lambda:root.destroy())

root.mainloop()
pygame.mixer.init()
pygame.mixer.music.set_volume(0.15)
pygame.mixer.music.load('mu.mp3')
pygame.mixer.music.play()
op=-1
countm=0

def frame_raise(frame,*more):
    frame.tkraise()
    for i in more:
        i.tkraise()
def TTT():
    global op
    op=1
    root.destroy()
    frame_raise(crossF1)
def BTMM():
    global op
    global c
    c=1
    op=0
    root.destroy()
    frame_raise(crossF1)
def RPS():
    global op
    op=2
    root.destroy()
    frame_raise(crossF1)
def PAP():
    global op
    op=3
    root.destroy()
def FFF():
    global op
    op=4
    root.destroy()
    frame_raise(crossF1)
def guess():
    global op
    op=5
    root.destroy()
    frame_raise(crossF1)
def FB():
    global op
    op=6
    root.destroy()
    frame_raise(crossF1)
def CS():
    global op
    op=8
    root.destroy()
    frame_raise(crossF1)
def musicOfffn():
    global countm
    if(countm==0):
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.15)
        pygame.mixer.music.load('mu.mp3')
        pygame.mixer.music.pause()
        countm=1
    elif(countm==1):
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.15)
        pygame.mixer.music.load('mu.mp3')
        pygame.mixer.music.play()
        countm=0
def SG():
    global op
    op=7
    root.destroy()
    frame_raise(crossF1)
def cross1():
    global op
    op=9
    root.destroy()
def cross2():
    global op
    op=9
    root.destroy()
def cross3():
    global op
    op=9
    root.destroy()
    pygame.quit()
def MMfunc():
    global op
    global c
    global count
    count=4
    c=1
    op=0
    root.destroy()
    frame_raise(crossF1)
def create_table():
    conn = sqlite3.connect('Gamehub.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Game_Hub
                    (id INTEGER PRIMARY KEY,
                    username TEXT,
                    password TEXT,
                    email TEXT,
                    snake_score INTEGER,
                    flappy_score INTEGER,
                    achievement INTEGER,
                    Piano_score INTEGER)''')
    conn.commit()
    conn.close()
create_table()
def update_snakescore(username, score):
    conn = sqlite3.connect('Gamehub.db')
    c = conn.cursor()
    c.execute("UPDATE Game_Hub SET snake_score = ? WHERE username = ?", (score, username,))
    conn.commit()
    conn.close()


def update_flappyscore(username, score):
    conn = sqlite3.connect('Gamehub.db')
    c = conn.cursor()
    c.execute("UPDATE Game_Hub SET flappy_score = ? WHERE username = ?", (score, username,))
    conn.commit()
    conn.close()
#function to add a new user
def adduser(username, email, password):
    conn = sqlite3.connect('Gamehub.db')
    c = conn.cursor()
    c.execute("INSERT INTO Game_Hub (username, password, email ,flappy_score,snake_score ) VALUES (?, ?, ?, ?, ?)", (username, password, email, 0, 0))

    conn.commit()
    conn.close()

#function to check credentials on login page
def check_login(username, password):
    conn = sqlite3.connect('Gamehub.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Game_Hub WHERE username = ? AND password=?", (username, password,))
    row = c.fetchone()
    conn.close()
    if row:
        return True
    else:
        return False


def check_username(username):
    conn = sqlite3.connect('Gamehub.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Game_Hub WHERE username = ?", (username,))
    row = c.fetchone()
    conn.close()
    if row:
        return True
    else:
        return False


def check_email(email):
    conn = sqlite3.connect('Gamehub.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Game_Hub WHERE email = ?", (email,))
    row = c.fetchone()
    conn.close()
    if row:
        return True
    else:
        return False





def update_pianoscore(username, score):
    conn = sqlite3.connect('Gamehub.db')
    c = conn.cursor()
    c.execute("UPDATE Game_Hub SET Piano_score = ? WHERE username = ?", (score, username,))
    conn.commit()
    conn.close()


def update_achievements(username, number):
    conn = sqlite3.connect('Gamehub.db')
    c = conn.cursor()
    c.execute("UPDATE Game_Hub SET achievement = ? WHERE username = ?", (number, username,))
    conn.commit()
    conn.close()


def search_data(username):
    conn = sqlite3.connect('Gamehub.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Game_Hub WHERE username=?", (username,))
    data = c.fetchone()
    conn.commit()
    conn.close()
    return data


#signup button on login page
def signup():
    frame_raise(signupf, usnamef2, emailf, newpassf, conpassf, showf2, subf2, btlf, msgf)
    usname.delete(0, END)
    passe.delete(0, END)
#back to login on signup page
def btl():
    msg2.config(text="")
    msg.config(text="")
    frame_raise(loginf, usnamef, passf, showf, signf, subf,msgf2)
    usname2.delete(0, END)
    email.delete(0, END)
    newpass.delete(0, END)
    conpass.delete(0, END)

#submit button on signup page
def submitsign():
    msg2.config(text="")
    msg.config(text="")
    list1 = []
    count = 0
    b = email.get().lower()
    for i in b:
        list1.append(i)
    for i in list1:
        if (
                i == '@' or i == '.' or i == 'c' or i == 'o' or i == 'm' or i == 'e' or i == 'd' or i == 'u' or i == 'i' or i == 'n'):
            count = count + 1
    if (usname2.get() > "" and newpass.get() > ""):
        if (count >= 5):
            if (newpass.get() == conpass.get()):
                if check_username(usname2.get()):
                    msg.config(text="Username has been taken")
                elif check_email(email.get()):
                    msg.config(text="Email already in use")
                else:
                    adduser(usname2.get(), email.get(), newpass.get())
                    frame_raise(loginf, usnamef, passf, showf, signf, subf, msgf2)
                    usname2.delete(0, END)
                    email.delete(0, END)
                    newpass.delete(0, END)
                    conpass.delete(0, END)
            else:
                msg.config(text="password Does not match")
        else:
            msg.config(text="enter a valid email Address")
    else:
        msg.config(text="all fields are mandatory")

# submit button on login page
def submitlogin():
    msg2.config(text="")
    if (usname.get() > "" and passe.get() > ""):
        if (check_login(usname.get(), passe.get())):
            global op
            op=0
            root.destroy()

        else:
            msg2.config(text="Invalid Credentials")
    else:
        msg2.config(text="All fields are mandatory")
def showdef(button, entry):
    global count
    if count == 1:
        entry.config(show="*")
        button.config(text="Show Password 🔑")
        count -= 1
    elif count == 0:
        passe.config(show="")
        button.config(text="Hide Password 🔑")
        count += 1
def showdef2(button, entry, entry2):
    global count2
    if count2 == 1:
        entry.config(show="*")
        entry2.config(show="*")
        button.config(text="Show Password 🔑")
        count2 -= 1
    elif count2 == 0:
        entry.config(show="")
        entry2.config(show="")
        button.config(text="Hide Password 🔑")
        count2 += 1
def openSettings():
    global op
    op=-2
    root.destroy()
def openDashboard():
    global op
    op=-3
    root.destroy()
def logoutfn():
    global op
    global pomodoro
    pomodoro=True
    op=-1
    root.destroy()
def pomodoroFn():
    global op
    op=-4
    root.destroy()
def pomodoropy():
    global op
    op=-4
    pygame.quit()
#main window
while(op!=9):
    if(op==-1):
        count = 0
        count2 = 0

        # login page
        root = Tk()
        root.title("login")
        root.state("zoomed")
        # signup page
        # username


        usnamef2 = Frame(root)
        usnamef2.place(x=955, y=290)
        a = StringVar()
        usname2 = Entry(usnamef2, textvariable=a, show="", width=18, font=('roboto', 20, 'bold'), borderwidth=3)
        usname2.pack()

        # email
        emailf = Frame(root)
        emailf.place(x=955, y=350)
        a = StringVar()
        email = Entry(emailf, textvariable=a, show="", width=18, font=('roboto', 20, 'bold'), borderwidth=3)
        email.pack()

        # newpass
        newpassf = Frame(root)
        newpassf.place(x=955, y=420)
        a = StringVar()
        newpass = Entry(newpassf, textvariable=a, show="*", width=18, font=('roboto', 20, 'bold'), borderwidth=3)
        newpass.pack()

        # confirmpass
        conpassf = Frame(root)
        conpassf.place(x=1000, y=490)
        a = StringVar()
        conpass = Entry(conpassf, textvariable=a, show="*", width=15, font=('roboto', 20, 'bold'), borderwidth=3)
        conpass.pack()
        # message
        msgf = Frame(root)
        msgf.place(x=888, y=570)
        msg = Label(msgf, text="", foreground="Red", background="White", font=('roboto', 15, 'bold'))
        msg.pack()

        # signup
        signupf = Frame(root)
        signupf.place(x=725, y=140)
        signup1 = ImageTk.PhotoImage(Image.open("signup1.png"))
        signu = Label(signupf, image=signup1)
        signu.pack()

        # submit
        subf2 = Frame(root)
        subf2.place(x=888, y=600)
        submit2 = ImageTk.PhotoImage(Image.open("submitbtn.png"))
        subb2 = Button(subf2, image=submit2, command=lambda: submitsign())
        subb2.pack()

        # back to login
        btlf = Frame(root)
        btlf.place(x=940, y=680)
        btl1 = Button(btlf, text="back to >> login", padx=10, pady=1, font=('roboto', 10, 'italic', 'bold'),
                      fg='#000000',
                      bg='white',
                      command=lambda: btl())
        btl1.pack()

        # show password
        showf2 = Frame(root)
        showf2.place(x=955, y=540)
        showb2 = Button(showf2, text="Show Password 🔑", padx=10, pady=1, font=('roboto', 10, 'italic', 'bold'),
                        fg='#000000',
                        bg='white',
                        command=lambda: showdef2(showb2, newpass, conpass))

        showb2.pack()

        # login page
        # username
        usnamef = Frame(root)
        usnamef.place(x=955, y=280)
        a1 = StringVar()
        usname = Entry(usnamef, textvariable=a1, show="", width=18, font=('roboto', 20, 'bold'), borderwidth=3)
        usname.pack()

        # password
        passf = Frame(root)
        passf.place(x=955, y=355)
        a = StringVar()
        passe = Entry(passf, textvariable=a, width=18, font=('roboto', 20, 'bold'), borderwidth=3, show="*")
        passe.pack()

        # signup button
        signf = Frame(root)
        signf.place(x=1020, y=555)
        sign = ImageTk.PhotoImage(Image.open("signupbtn.png"))
        signb = Button(signf, image=sign, command=lambda: signup())
        signb.pack()

        # submit button
        subf = Frame(root)
        subf.place(x=888, y=479)
        submit = ImageTk.PhotoImage(Image.open("submitbtn.png"))
        subb = Button(subf, image=submit, command=lambda: submitlogin())
        subb.pack()
        # msg
        msgf2 = Frame(root)
        msgf2.place(x=888, y=450)
        msg2 = Label(msgf2, text="", foreground="Red", background="White", font=('roboto', 15, 'bold'))
        msg2.pack()
        # login label background
        loginf = Frame(root)
        loginf.place(x=725, y=140)
        login = ImageTk.PhotoImage(Image.open("login1.png"))
        login1 = Label(loginf, image=login)
        login1.pack()

        showf = Frame(root)
        showf.place(x=955, y=410)
        showb = Button(showf, text="Show Password 🔑", padx=10, pady=1, font=('roboto', 10, 'italic', 'bold'),
                       fg='#000000',
                       bg='white',
                       command=lambda: showdef(showb, passe))
        showb.pack()

        i = 10000
        videoplayer = TkinterVideo(master=root, scaled=True)
        videoplayer.load("signuppage.gif")
        videoplayer.pack(expand=True, fill="both")
        videoplayer.play()
        while i <= 10000000:
            root.after(i, lambda: videoplayer.play())
            i += 10000
        crossF2=Frame(root)
        crossF2.place(x=1490,y=0)
        crossB2 = Button(crossF2, text="X", height=1, width=5, font=('roboto', 10, 'bold'), bg="red", fg="white",
                         command=cross2)
        crossB2.pack()
        frame_raise(loginf, usnamef, passf, showf, signf, subf, msgf2,crossF2)
        # signup page
        root.mainloop()
    elif(op==-3):
        root = Tk()
        root.title("welcome page")
        root.state("zoomed")

        if(pomodoro==False):
            CT1=time.time()
            root.after(600000-int((CT1-startTime)*1000),lambda :pomodoroFn())


        # rookie
        rookief = Frame(root)
        rookief.place(x=0, y=0)
        rookiep = Image.open("Beginner.png")
        rookiep = rookiep.resize((screen_width, screen_height))
        rookiep = ImageTk.PhotoImage(rookiep)
        rookiebatch = Label(rookief, image=rookiep)
        rookiebatch.pack()

        # pro
        prof = Frame(root)
        prof.place(x=0, y=0)
        prop = Image.open("Pro.png")
        prop = prop.resize((screen_width, screen_height))
        prop = ImageTk.PhotoImage(prop)
        probatch = Label(rookief, image=prop)
        probatch.pack()

        # allstar
        allstarf = Frame(root)
        allstarf.place(x=0, y=0)
        allstarp = Image.open("All star.png")
        allstarp = allstarp.resize((screen_width, screen_height))
        allstarp = ImageTk.PhotoImage(allstarp)
        allstar = Label(allstarf, image=allstarp)
        allstar.pack()

        # name
        namef = Frame(root)
        namef.place(x=960, y=164)
        name = Label(namef, text=f"{a1.get().capitalize()}", font=('roboto', 33, 'bold'), bg="white")
        name.pack()

        # email
        emlf = Frame(root)
        emlf.place(x=960, y=255)
        eml = Label(emlf, text=f"{search_data(a1.get())[3]}", font=('roboto', 33, 'bold'), bg="white")
        eml.pack()

        # flappy high score
        flappyhighf = Frame(root)
        flappyhighf.place(x=1200, y=530)
        flappyhigh = Label(flappyhighf, text=f"{search_data(a1.get())[5]}", font=('Big Heroes Free Trial', 34, 'bold'), bg="white")
        flappyhigh.pack()

        # snake high score
        snakehighf = Frame(root)
        snakehighf.place(x=1200, y=630)
        snakehigh = Label(snakehighf, text=f"{search_data(a1.get())[4]}", font=('Big Heroes Free Trial', 34, 'bold'), bg="white")
        snakehigh.pack()

        # back to main menu
        btmf = Frame(root)
        btmf.place(x=20, y=15)
        btmp = ImageTk.PhotoImage(Image.open("backtomaoinmenu.png"))
        btmb = Button(btmf, image=btmp, background="white", command=lambda: BTMM())
        btmb.pack()

        # prob
        probf = Frame(root)
        probf.place(x=0, y=0)
        probp = ImageTk.PhotoImage(Image.open("pro.png"))
        probb = Label(probf, image=probp)
        probb.pack()
        if (search_data(a1.get())[4] > 40 and search_data(a1.get())[5] > 20):
            frame_raise(allstarf, btmf, namef, emlf, flappyhighf, snakehighf)
        elif(search_data(a1.get())[4] > 20 and search_data(a1.get())[5] > 10):
            frame_raise(prof, btmf, namef, emlf, flappyhighf, snakehighf)
        else:
            frame_raise(rookief, btmf, namef, emlf, flappyhighf, snakehighf)
        root.mainloop()
    elif(op==0):
        root =Tk()
        root.title("main menu")
        root.iconbitmap('fav.ico')
        root.state('zoomed')

        #heading
        from tkinter import *
        from PIL import Image,ImageTk

        if (pomodoro == False):
            CT1 = time.time()
            root.after(600000 - int((CT1 - startTime) * 1000), lambda: pomodoroFn())

        settingsF=Frame(root)
        settingsF.place(x=1450,y=125)
        settingsI=ImageTk.PhotoImage(Image.open("settingsIcon.png"))
        settingsB=Button(settingsF,image=settingsI,command=openSettings)
        settingsB.pack()
        dashboardF=Frame(root)
        dashboardF.place(x=1370,y=125)
        dashboardI=ImageTk.PhotoImage(Image.open("profileIcon.png"))
        dashboardB=Button(dashboardF,image=dashboardI,command=openDashboard)
        dashboardB.pack()
        yourNameF=Frame(root)
        yourNameF.place(x=300,y=125)
        yourNameL=Label(yourNameF,text=f"{search_data(a1.get())[1].capitalize()}",font=('Big Heroes Free Trial',34,'bold'),bg="white")
        yourNameL.pack()
        head_1=Frame(root)
        head_1.place(x=0,y=0)
        musicF=Frame(root)
        musicF.place(x=1400,y=125)
        head_1_img = Image.open("mm.png")
        head_1_img = head_1_img.resize((screen_width, screen_height))
        head_1_img = ImageTk.PhotoImage(head_1_img)
        heading_1=Label(head_1,image=head_1_img)
        heading_1.pack()

        #buttons
        bt_img1=Frame(root)
        bt_img1.place(x=65,y=225)
        from tkinter import *
        from PIL import Image, ImageTk
        crossF = Frame(root)
        crossF.place(x=1320, y=30)
        crossI=ImageTk.PhotoImage(Image.open("quitBtn.png"))
        crossB = Button(crossF, image=crossI , command=cross1)
        crossB.pack()
        btimg1=ImageTk.PhotoImage(Image.open("1.png"))
        bt_img_1= Button(bt_img1,image=btimg1,command=TTT)
        bt_img_1.pack()

        bt_img2=Frame(root)
        bt_img2.place(x=425,y=225)
        btimg2=ImageTk.PhotoImage(Image.open("2.png"))
        bt_img_2= Button(bt_img2,image=btimg2,command=RPS)
        bt_img_2.pack()

        bt_img3=Frame(root)
        bt_img3.place(x=785,y=225)
        btimg3=ImageTk.PhotoImage(Image.open("3.png"))
        bt_img_3= Button(bt_img3,image=btimg3,command=PAP)
        bt_img_3.pack()

        bt_img4=Frame(root)
        bt_img4.place(x=1145,y=225)
        btimg4=ImageTk.PhotoImage(Image.open("4.png"))
        bt_img_4= Button(bt_img4,image=btimg4,command=FFF)
        bt_img_4.pack()

        bt_img5=Frame(root)
        bt_img5.place(x=65,y=545)
        btimg5=ImageTk.PhotoImage(Image.open("6.png"))
        bt_img_5= Button(bt_img5,image=btimg5,command=guess)
        bt_img_5.pack()

        bt_img6=Frame(root)
        bt_img6.place(x=425,y=545)
        btimg6=ImageTk.PhotoImage(Image.open("7.png"))
        bt_img_6= Button(bt_img6,image=btimg6,command=FB)
        bt_img_6.pack()

        bt_img7=Frame(root)
        bt_img7.place(x=785,y=545)
        btimg7=ImageTk.PhotoImage(Image.open("8.png"))
        bt_img_7= Button(bt_img7,image=btimg7,command=SG)
        bt_img_7.pack()

        bt_img8=Frame(root)
        bt_img8.place(x=1145,y=545)
        btimg8=ImageTk.PhotoImage(Image.open("5.png"))
        bt_img_8= Button(bt_img8,image=btimg8,command=CS)
        bt_img_8.pack()
        frame_raise(yourNameF,settingsF,dashboardF)
        root.mainloop()
    elif(op==-2):
        root = Tk()
        root.title("welcome page")
        root.state("zoomed")

        if (pomodoro == False):
            CT1 = time.time()
            root.after(600000 - int((CT1 - startTime) * 1000), lambda: pomodoroFn())

        # functions
        def frame_raise(frame, *more):
            frame.tkraise()
            for i in more:
                i.tkraise()


        # turn of pomodoro and turn on pomodoro
        def tofp():
            pass


        def tonp():
            global pomodoro
            global op
            pomodoro=False
            frame_raise(tofpf)


        # turn off sound and turn on sound
        def tofs():
            global sonar
            pygame.mixer.init()
            pygame.mixer.music.load('mu.mp3')
            pygame.mixer.music.play()
            sonar=True
            frame_raise(tosf)


        def tons():
            global sonar
            pygame.mixer.music.pause()
            sonar=False
            frame_raise(tofsf)


        # welcome page

        # profile button
        prof = Frame(root)
        prof.place(x=1330, y=135)
        proi = ImageTk.PhotoImage(Image.open("profileicon.png"))
        prob = Button(prof, image=proi, background="white")
        prob.pack()

        # settings button
        settingsf = Frame(root)
        settingsf.place(x=1400, y=135)
        settingg = ImageTk.PhotoImage(Image.open("settingsicon.png"))
        settingb = Button(settingsf, image=settingg, background="white")
        settingb.pack()

        # quit button
        quitf = Frame(root)
        quitf.place(x=1300, y=35)
        quit = ImageTk.PhotoImage(Image.open("quitbtn.png"))
        quitb = Button(quitf, image=quit, background="white", command=lambda: root.destroy())
        quitb.pack()

        # settings page

        # settings
        settingf = Frame(root)
        settingf.place(x=0, y=0)
        settingp = Image.open("settingspage.png")
        settingp = settingp.resize((screen_width, screen_height))
        settingp = ImageTk.PhotoImage(settingp)
        settinggg = Label(settingf, image=settingp)
        settinggg.pack()

        # turnonsound
        tosf = Frame(root)
        tosf.place(x=350, y=150)
        tosp = ImageTk.PhotoImage(Image.open("tos1.png"))
        tosb = Button(tosf, image=tosp, background="white", command=lambda: tons())
        tosb.pack()

        # turnoffsound
        tofsf = Frame(root)
        tofsf.place(x=350, y=150)
        tofsp = ImageTk.PhotoImage(Image.open("tos2.png"))
        tofsb = Button(tofsf, image=tofsp, background="white", command=lambda: tofs())
        tofsb.pack()

        # turnonpomodoro
        topf = Frame(root)
        topf.place(x=300, y=380)
        topp = ImageTk.PhotoImage(Image.open("top1.png"))
        topb = Button(topf, image=topp, background="white", command=lambda: tonp())
        topb.pack()

        # turnoffpomodoro
        tofpf = Frame(root)
        tofpf.place(x=300, y=380)
        tofpp = ImageTk.PhotoImage(Image.open("top2.png"))
        tofpb = Button(tofpf, image=tofpp, background="white", command=lambda: tofp())
        tofpb.pack()

        # Login
        logoutf = Frame(root)
        logoutf.place(x=350, y=610)
        logout1 = ImageTk.PhotoImage(Image.open("logout.png"))
        logout = Button(logoutf, image=logout1, background="white",command=logoutfn)
        logout.pack()

        # back to main menu
        btmf = Frame(root)
        btmf.place(x=20, y=15)
        btmp = ImageTk.PhotoImage(Image.open("backtomaoinmenu.png"))
        btmb = Button(btmf, image=btmp, background="white",command=BTMM)
        btmb.pack()
        if pomodoro and sonar:
            frame_raise(settingf, btmf, topf, tosf, logoutf)
        elif(sonar):
            frame_raise(settingf, btmf, tofpf, tosf, logoutf)
        elif(pomodoro):
            frame_raise(settingf, btmf, tofsf, topf, logoutf)
        else:
            frame_raise(settingf, btmf, tofsf, tofpf, logoutf)
        root.mainloop()
    elif(op==-4):
        root=Tk()
        root.state("zoomed")
        pomoF=Frame(root)
        pomoF.place(x=0,y=0)
        pomoI = Image.open("gameCloser.png")
        pomoI = pomoI.resize((screen_width, screen_height))
        pomoI = ImageTk.PhotoImage(pomoI)
        pomoL=Label(pomoF,image=pomoI)
        pomoL.pack()
        byeF=Frame(root)
        byeF.place(x=670,y=600)
        byeI=ImageTk.PhotoImage(Image.open("quitBtn.png"))
        byeB=Button(byeF,image=byeI,command=cross3)
        byeB.pack()
        root.mainloop()
    elif(op==1):

        # main window

        root = Tk()
        root.title("Tic Tac Toe")
        root.iconbitmap('fav.ico')
        root.state('zoomed')

        if (pomodoro == False):
            CT1 = time.time()
            root.after(600000 - int((CT1 - startTime) * 1000), lambda: pomodoroFn())
        # heading
        crossF1 = Frame(root)
        crossF1.place(x=1490, y=0)
        crossB1 = Button(crossF1, text="X", height=1, width=5, font=('roboto', 10, 'bold'), bg="red", fg="white",
                        command=MMfunc)
        crossB1.pack()
        head1 = Frame(root)
        head1.place(x=390, y=15)
        head1_img = ImageTk.PhotoImage(Image.open("head2.png"))
        heading1 = Label(head1, image=head1_img)
        heading1.pack()

        # check_layout
        head = Frame(root)
        head.place(x=495, y=230)
        head_img = ImageTk.PhotoImage(Image.open("check.png"))
        heading = Label(head, image=head_img)
        heading.pack()

        # messages
        mesg = Frame(root)
        mesg.place(x=550, y=760)
        msg = Label(mesg, text="Player 1 your turn", font=('', 45, 'bold'), fg="black")
        msg.pack()

        # buttons
        bt1 = Frame(root)
        bt1.place(x=523, y=245)
        bt5 = Frame(root)
        bt5.place(x=685, y=415)
        bt2 = Frame(root)
        bt2.place(x=685, y=245)
        bt3 = Frame(root)
        bt3.place(x=850, y=245)
        bt4 = Frame(root)
        bt4.place(x=523, y=415)

        bt6 = Frame(root)
        bt6.place(x=850, y=415)
        bt7 = Frame(root)
        bt7.place(x=523, y=580)
        bt8 = Frame(root)
        bt8.place(x=685, y=580)
        bt9 = Frame(root)
        bt9.place(x=850, y=580)

        # lines
        line_row1 = Frame(root)
        line_row1.place(x=495, y=280)
        line_row1_img = ImageTk.PhotoImage(Image.open("line 1.png"))
        line_row1 = Label(line_row1, image=line_row1_img)

        line_row2 = Frame(root)
        line_row2.place(x=495, y=450)
        line_row2_img = ImageTk.PhotoImage(Image.open("line 1.png"))
        line_row2 = Label(line_row2, image=line_row2_img)

        line_row3 = Frame(root)
        line_row3.place(x=495, y=620)
        line_row3_img = ImageTk.PhotoImage(Image.open("line 1.png"))
        line_row3 = Label(line_row3, image=line_row3_img)

        line_col1 = Frame(root)
        line_col1.place(x=555, y=235)
        line_col1_img = ImageTk.PhotoImage(Image.open("line2.png"))
        line_col1 = Label(line_col1, image=line_col1_img)

        line_col2 = Frame(root)
        line_col2.place(x=725, y=235)
        line_col2_img = ImageTk.PhotoImage(Image.open("line2.png"))
        line_col2 = Label(line_col2, image=line_col2_img)

        line_col3 = Frame(root)
        line_col3.place(x=890, y=235)
        line_col3_img = ImageTk.PhotoImage(Image.open("line2.png"))
        line_col3 = Label(line_col3, image=line_col3_img)

        diag = Frame(root)
        diag.place(x=495, y=230)
        diag_img = ImageTk.PhotoImage(Image.open("check1.png"))
        diagonal = Label(diag, image=diag_img)

        diag1 = Frame(root)
        diag1.place(x=495, y=230)
        diag_1img = ImageTk.PhotoImage(Image.open("check2.png"))
        diagonal1 = Label(diag1, image=diag_1img)

        diag2 = Frame(root)
        diag2.place(x=495, y=230)
        diag_2img = ImageTk.PhotoImage(Image.open("check3.png"))
        diagonal2 = Label(diag2, image=diag_2img)

        diag3 = Frame(root)
        diag3.place(x=495, y=230)
        diag_3img = ImageTk.PhotoImage(Image.open("check4.png"))
        diagonal3 = Label(diag3, image=diag_3img)

        count = 1
        li = []


        def working(Y):
            global count
            global li
            if count <= 9:
                if count % 2 != 0:
                    updatemsg("Player 2 your turn")
                    if Y not in li:
                        li.append(Y)
                        updatex(Y)
                        count = count + 1
                    else:
                        count = count - 2
                        updatemsg("Invalid Move")
                        root.after(500, lambda: updatemsg("Player 1 your turn"))
                else:
                    updatemsg("Player 1 your turn")
                    if Y not in li:
                        li.append(Y)
                        updateo(Y)
                        count = count + 1
                    else:
                        count = count - 2
                        updatemsg("Invalid Move")
                        root.after(500, lambda: updatemsg("Player 2 your turn"))
                checkwin()
            if count == 10:
                updatemsg("Its a tie")
                root.after(500, lambda: BTMM())


        def checkwin():
            if button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X':
                line_row1.pack()
                updatemsg("Player 1 Win 🎊")
                root.after(700, lambda: BTMM())
                return
            elif button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O':
                line_row1.pack()
                updatemsg("Player 2 Win 🎊")
                root.after(700, lambda: BTMM())
                return
            elif button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X':
                line_row2.pack()
                updatemsg("Player 1 Win 🎊")
                root.after(700, lambda: BTMM())
                return
            elif button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O':
                line_row2.pack()
                updatemsg("Player 2 Win 🎊")
                root.after(700, lambda: BTMM())
                return
            elif button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X':
                line_row3.pack()
                updatemsg("Player 1 Win 🎊")
                root.after(700, lambda: BTMM())
                return
            elif button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O':
                line_row3.pack()
                updatemsg("Player 2 Win 🎊")
                root.after(700, lambda: BTMM())
                return
            elif button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X':
                line_col1.pack()
                updatemsg("Player 1 Win 🎊")
                root.after(700, lambda: BTMM())
                return
            elif button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O':
                line_col1.pack()
                updatemsg("Player 2 Win 🎊")
                root.after(700, lambda: BTMM())
                return
            elif button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X':
                line_col2.pack()
                updatemsg("Player 1 Win 🎊")
                root.after(700, lambda: BTMM())
                return
            elif button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O':
                line_col2.pack()
                updatemsg("Player 2 Win 🎊")
                root.after(700, lambda: BTMM())
                return
            elif button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X':
                line_col3.pack()
                updatemsg("Player 1 Win 🎊")
                root.after(700, lambda: BTMM())
                return
            elif button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O':
                line_col3.pack()
                updatemsg("Player 2 Win 🎊")
                root.after(700, lambda: BTMM())
                return
            elif button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X':
                diagonal.pack()
                frame_raise(diag, bt2, bt3, bt4, bt6, bt7, bt8)
                updatemsg("Player 1 Win 🎊")
                root.after(700, lambda: BTMM())
                return
            elif button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O':
                diagonal1.pack()
                frame_raise(diag1, bt2, bt3, bt4, bt6, bt7, bt8)
                updatemsg("Player 2 Win 🎊")
                root.after(700, lambda: BTMM())
                return
            elif button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X':
                diagonal2.pack()
                frame_raise(diag2, bt2, bt1, bt4, bt6, bt9, bt8)
                updatemsg("Player 1 Win 🎊")
                root.after(700, lambda: BTMM())
                return
            elif button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O':
                diagonal3.pack()
                frame_raise(diag3, bt2, bt1, bt4, bt6, bt9, bt8)
                updatemsg("Player 2 Win 🎊")
                root.after(700, lambda: BTMM())
                return


        def frame_raise(frame, *more):
            frame.tkraise()
            for i in more:
                i.tkraise()


        def updatemsg(x):
            msg['text'] = x


        def updatex(y):
            y['text'] = 'X'
            y.configure(fg='#004AAD')


        def updateo(y):
            y['text'] = 'O'
            y.configure(fg='#FF5757')


        button1 = Button(bt1, text="  ", padx=10, pady=1, font=('roboto', 50, 'bold'), fg='#000000',
                         command=lambda: working(button1))
        button1.pack()
        button2 = Button(bt2, text="  ", padx=10, pady=1, font=('roboto', 50, 'bold'), fg='#000000',
                         command=lambda: working(button2))
        button2.pack()
        button3 = Button(bt3, text="  ", padx=10, pady=1, font=('roboto', 50, 'bold'), fg='#000000',
                         command=lambda: working(button3))
        button3.pack()
        button4 = Button(bt4, text="  ", padx=10, pady=1, font=('roboto', 50, 'bold'), fg='#000000',
                         command=lambda: working(button4))
        button4.pack()
        button5 = Button(bt5, text="  ", padx=10, pady=1, font=('roboto', 50, 'bold'), fg='#000000',
                         command=lambda: working(button5))
        button5.pack()
        button6 = Button(bt6, text="  ", padx=10, pady=1, font=('roboto', 50, 'bold'), fg='#000000',
                         command=lambda: working(button6))
        button6.pack()
        button7 = Button(bt7, text="  ", padx=10, pady=1, font=('roboto', 50, 'bold'), fg='#000000',
                         command=lambda: working(button7))
        button7.pack()
        button8 = Button(bt8, text="  ", padx=10, pady=1, font=('roboto', 50, 'bold'), fg='#000000',
                         command=lambda: working(button8))
        button8.pack()
        button9 = Button(bt9, text="  ", padx=10, pady=1, font=('roboto', 50, 'bold'), fg='#000000',
                         command=lambda: working(button9))
        button9.pack()

        root.mainloop()
    elif(op==2):
        root = Tk()
        root.title("rock paper scissors")
        root.iconbitmap('fav.ico')
        root.state('zoomed')

        if (pomodoro == False):
            CT1 = time.time()
            root.after(600000 - int((CT1 - startTime) * 1000), lambda: pomodoroFn())

        # heading
        crossF1 = Frame(root)
        crossF1.place(x=1490, y=0)
        crossB1 = Button(crossF1, text="X", height=1, width=5, font=('roboto', 10, 'bold'), bg="red", fg="white",
                        command=MMfunc)
        crossB1.pack()
        head = Frame(root)
        head.place(x=460, y=20)
        head_img = ImageTk.PhotoImage(Image.open("head.png"))
        heading = Label(head, image=head_img)
        heading.pack()

        # image
        sci_img = ImageTk.PhotoImage(Image.open("scissors.png"))
        rock_img = ImageTk.PhotoImage(Image.open("rock.png"))
        paper_img = ImageTk.PhotoImage(Image.open("paper.png"))
        sci_img1 = ImageTk.PhotoImage(Image.open("scissors1.png"))
        rock_img1 = ImageTk.PhotoImage(Image.open("rock2.png"))
        paper_img1 = ImageTk.PhotoImage(Image.open("paper1.png"))
        user = Frame(root)
        comp = Frame(root)
        comp.place(x=250, y=250)
        user.place(x=1000, y=250)

        # insert image
        user_label = Label(user, image=sci_img1)
        comp_label = Label(comp, image=sci_img)
        user_label.pack()  # comp_label.grid(row=1,column=0)
        comp_label.pack()

        # scoareboared
        user_score = Frame(root)
        user_score.place(x=880, y=350)
        userscore = Label(user_score, text=0, font="roboto 60", fg="black")
        userscore.pack()

        comp_score = Frame(root)
        comp_score.place(x=600, y=350)
        compscore = Label(comp_score, text=0, font="roboto 60", fg="black")
        compscore.pack()

        # Indicators
        user_ind = Frame(root)
        user_ind.place(x=1115, y=550)
        userind = Label(user_ind, text="USER", font=100, fg="black")
        userind.pack()

        comp_ind = Frame(root)
        comp_ind.place(x=325, y=550)
        compind = Label(comp_ind, text="COMPUTER", font=100, fg="black")
        compind.pack()
        # messages
        mesg = Frame(root)
        mesg.place(x=670, y=750)
        msg = Label(mesg, text="", font="roboto 30", fg="black")
        msg.pack()
        # buttons
        rockf = Frame(root)
        rockf.place(x=390, y=650)
        paperf = Frame(root)
        paperf.place(x=640, y=650)
        scissorsf = Frame(root)
        scissorsf.place(x=890, y=650)
        rock = Button(rockf, width=20, height=2, font=10, text="Rock", bg="#FF5757", fg="white",
                      command=lambda: update_choice("rock"))
        rock.pack()
        paper = Button(paperf, width=20, height=2, font=10, text="Paper", bg="#004AAD", fg="white",
                       command=lambda: update_choice("paper"))
        paper.pack()
        scissors = Button(scissorsf, width=20, height=2, font=10, text="Scissors", bg="#02A447", fg="white",
                          command=lambda: update_choice("scissors"))
        scissors.pack()

        # update choices
        choice = ["rock", "paper", "scissors"]


        def update_choice(x):
            # for user
            if x == "rock":
                user_label.configure(image=rock_img1)
            elif x == "paper":
                user_label.configure(image=paper_img1)
            else:
                user_label.configure(image=sci_img1)

            # for comp
            compchoice = choice[random.randint(0, 2)]
            if compchoice == "rock":
                comp_label.configure(image=rock_img)
            elif compchoice == "paper":
                comp_label.configure(image=paper_img)
            else:
                comp_label.configure(image=sci_img)

            checkwin(x, compchoice)
            Quit(userscore['text'], compscore['text'])


        def Quit(x, y):
            if x == '3' or y == '3':
                root.after(1000, lambda: BTMM())


        def updatemsg(x):
            msg['text'] = x


        def updateuserscore():
            score = int(userscore["text"])
            score += 1
            userscore["text"] = str(score)


        def updatecompscore():
            score = int(compscore["text"])
            score += 1
            compscore["text"] = str(score)


        def checkwin(user, comp):
            if user == comp:
                updatemsg("Its a Tie")
            elif user == "rock":
                if comp == "paper":
                    updatemsg("you lose")
                    updatecompscore()
                else:
                    updatemsg("you win")
                    updateuserscore()
            elif user == "paper":
                if comp == "scissors":
                    updatemsg("you lose")
                    updatecompscore()
                else:
                    updatemsg("you win")
                    updateuserscore()
            else:
                if comp == "rock":
                    updatemsg("you lose")
                    updatecompscore()
                else:
                    updatemsg("you win")
                    updateuserscore()


        root.mainloop()
    elif(op==3):



        def e():
            global count
            count = 0
            root.destroy()


        def b():
            global count
            count = 1
            root.destroy()


        def h():
            global count
            count = 2
            root.destroy()


        def en():
            global count
            count = 3
            root.destroy()


        def bk():
            global count
            count = -1
            root.destroy()


        def q():
            global count
            global op
            count = 4
            op=0
            root.destroy()


        count = -1
        while count != 4:
            if (count == -1):
                root = Tk()
                root.iconbitmap('fav.ico')
                root.title("Peek A Phone")
                root.state("zoomed")

                if (pomodoro == False):
                    CT1 = time.time()
                    root.after(600000 - int((CT1 - startTime) * 1000), lambda: pomodoroFn())

                # code for first frame
                crossF1 = Frame(root)
                crossF1.place(x=1490, y=0)
                crossB1 = Button(crossF1, text="X", height=1, width=5, font=('roboto', 10, 'bold'), bg="red", fg="white",
                                command=MMfunc)
                crossB1.pack()
                easy = Frame(root)
                balanced = Frame(root)
                difficultyLevel = Frame(root)
                easy.place(x=600, y=250)
                balanced.place(x=600, y=475)
                difficultyLevel.place(x=0, y=0)
                image1 = ImageTk.PhotoImage(Image.open("easy.png"))
                image2 = ImageTk.PhotoImage(Image.open("balanced.png"))
                image5 = Image.open("difficultyLevel.png")
                image5 = image5.resize((screen_width, screen_height))
                image5 = ImageTk.PhotoImage(image5)
                b1 = Button(easy, image=image1, command=e)
                b2 = Button(balanced, image=image2, command=b)
                l1 = Label(difficultyLevel, image=image5)
                l1.pack()
                b1.pack()
                b2.pack()
                frame_raise( difficultyLevel, easy, balanced,crossF1)
                root.mainloop()

            # code for second frame
            if (count == 0):
                root = Tk()
                root.title("Peek A Phone")
                root.state("zoomed")
                root.iconbitmap('fav.ico')
                if (pomodoro == False):
                    CT1 = time.time()
                    root.after(600000 - int((CT1 - startTime) * 1000), lambda: pomodoroFn())
                crossF1 = Frame(root)
                crossF1.place(x=1490, y=0)
                crossB1 = Button(crossF1, text="X", height=1, width=5, font=('roboto', 10, 'bold'), bg="red", fg="white",
                                command=MMfunc)
                crossB1.pack()
                startMissionButton = Frame(root)
                startMissionButton.place(x=770, y=650)
                mission1Start = Frame(root)
                mission1Start.place(x=0, y=0)
                img0 = ImageTk.PhotoImage(Image.open("backButton.png"))
                backButton = Frame(root, bg="black")
                backButton.place(x=400, y=650)
                b0 = Button(backButton, image=img0, bg="black", command=bk)
                b0.pack()
                img1 = Image.open("mission1Start.png")
                img1 = img1.resize((screen_width, screen_height))
                img1 = ImageTk.PhotoImage(img1)
                lab = Label(mission1Start, image=img1)
                lab.pack()
                img2 = ImageTk.PhotoImage(Image.open("startMissionButton.png"))
                b5 = Button(startMissionButton, image=img2, bg="black",
                            command=lambda: frame_raise( wallpaper1, messaging, gallery, backButton1,
                                                        submitAnswer, bar,crossF1))
                b5.pack()

                # code for level 1
                wallpaper1 = Frame(bg="black")
                wallpaper1.place(x=0, y=0)
                image12 = ImageTk.PhotoImage(Image.open("message.png"))
                msgWindow = Frame(root)
                msgWindow.place(x=0, y=10)
                chat1 = Frame(root, bg="black")
                chat1.place(x=0, y=10)
                houseNo = Frame(root, bg="black", padx=20)
                houseNo.place(x=0, y=0)
                messaging = Frame(root, bg="white")
                gallery = Frame(root, bg="white")
                back = Frame(root, bg="white")
                backButton1 = Frame(root)
                flag = Frame(root, bg="white")
                mom = Frame(root, bg="black")
                houseImage = Frame(root, bg="white")
                houseImage.place(x=20, y=170)
                galleryInterface = Frame(root, bg="black")
                galleryInterface.place(x=0, y=0)
                gallery.place(x=20, y=20)
                messaging.place(x=20, y=110)
                backButton1.place(x=750, y=700)
                mom.place(x=22, y=114)
                img3 = Image.open("wallpaper1.png")
                img3 = img3.resize((screen_width, screen_height))
                img3 = ImageTk.PhotoImage(img3)
                l3 = Label(wallpaper1, image=img3)
                l4 = Label(messaging, text="Whatsapp", font="comicsansms 7")
                l5 = Label(gallery, text="Gallery", font="comicsansms 7")
                l3.pack()
                img4 = ImageTk.PhotoImage(Image.open("message.png"))
                img5 = ImageTk.PhotoImage(Image.open("gallery.png"))
                img7 = ImageTk.PhotoImage(Image.open("backButton1.png"))
                img9 = Image.open("msgWindow.png")
                img9 = img9.resize((screen_width, screen_height))
                img9 = ImageTk.PhotoImage(img9)
                img10 = ImageTk.PhotoImage(Image.open("mom.png"))
                img11 = Image.open("chat.png")
                img11 = img11.resize((screen_width,screen_height))
                img11 = ImageTk.PhotoImage(img11)
                img12 = Image.open("galleryInterface.png")
                img12 = img12.resize((screen_width, screen_height))
                img12 = ImageTk.PhotoImage(img12)
                img13 = ImageTk.PhotoImage(Image.open("houseImage.png"))
                img14 = Image.open("houseNo.png")
                img14 = img14.resize((screen_width, screen_height))
                img14 = ImageTk.PhotoImage(img14)
                jpg1 = ImageTk.PhotoImage(Image.open("submitAnswer.png"))
                jpg2 = ImageTk.PhotoImage(Image.open("think.png"))
                b6 = Button(messaging, image=img4,
                            command=lambda: frame_raise(msgWindow, mom, backButton1, bar,crossF1))
                b7 = Button(gallery, image=img5,
                            command=lambda: frame_raise(galleryInterface, houseImage, backButton1, bar,crossF1))
                b9 = Button(backButton1, image=img7,
                            command=lambda: frame_raise( wallpaper1, messaging, gallery, backButton1,
                                                        submitAnswer, bar,crossF1))
                b6.pack()
                l4.pack()
                b7.pack()
                l5.pack()
                b9.pack()
                l6 = Label(msgWindow, image=img9)
                b11 = Button(mom, image=img10, command=lambda: frame_raise( chat1, backButton1, bar,crossF1), bg="black")
                b12 = Button(houseImage, image=img13, command=lambda: frame_raise( houseNo, backButton1, bar,crossF1))
                b12.pack()
                l6.pack()
                b11.pack()
                l7 = Label(chat1, image=img11)
                l8 = Label(galleryInterface, image=img12)
                l9 = Label(houseNo, image=img14)
                l7.pack()
                l8.pack()
                l9.pack()


                # answer screen
                def checker():
                    list1 = []
                    count = 0
                    b = a.get().lower()
                    for i in b:
                        list1.append(i)
                    for i in list1:
                        if (
                                i == '1' or i == '6' or i == 'a' or i == 'e' or i == 'k' or i == 'p' or i == 'r' or i == 's' or i == 't'):
                            count = count + 1
                    if (count == 13):
                        l13.pack()
                        l14.pack()
                        b15.pack()
                        b16.pack(pady=15)
                        frame_raise(winner,crossF1)
                        address.delete(0, END)
                    else:
                        l12.pack()


                answer = Frame(root)
                winner = Frame(root, bg="black", padx=700, pady=560, relief=SUNKEN, borderwidth=6)
                winner.place(x=0, y=0)
                answer.place(x=200, y=200)
                lb1 = Label(answer, image=jpg2)
                lb1.pack()
                bar = Frame(root, bg="black")
                bar.place(x=0, y=0)
                l15 = Label(bar, font="comicsansms 9", bg="black", fg="white")
                l15.pack(padx=740)


                def timer():
                    A = time.strftime('%H')
                    a = int(A)
                    b = time.strftime('%M')
                    c = time.strftime('%S')
                    d = time.strftime('%p')
                    if (d == 'PM'):
                        a = a - 12
                    l15.config(text=f"{a}:{b}:{c} {d}")
                    l15.after(1000, timer)


                timer()
                a = StringVar()
                address = Entry(answer, textvariable=a, font="comicsansms 23")
                b13 = Button(answer, text="SUBMIT ANSWER", bg="green", fg="white", font="algerian 15 bold",
                             command=checker)
                address.pack()
                b13.pack()
                submitAnswer = Frame(root, bg="white")
                submitAnswer.place(x=1100, y=645)
                b14 = Button(submitAnswer, image=jpg1, bg="green", fg="white", font="algerian 13 bold",
                             command=lambda: frame_raise(answer, backButton1,crossF1))
                b14.pack()
                l12 = Label(answer, text="Wrong Answer! Try Again", font="comicsansms 9")
                l13 = Label(winner, text="Congratulations!", font="algerian 19 bold", bg="black", fg="green")
                l14 = Label(winner, text="You Cracked It", font="algerian 15 bold", bg="black", fg="green")
                b15 = Button(winner, text="Play Again", font="comicsansms 15 bold", command=bk)
                b16 = Button(winner, text="Main Menu", font="comicsansms 15 bold", command=q)
                frame_raise(mission1Start, backButton, startMissionButton,crossF1)
                root.mainloop()

            if (count == 1):
                # code for balanced difficulty
                root = Tk()
                root.title("Peek A Phone")
                root.state("zoomed")
                root.iconbitmap('fav.ico')
                if (pomodoro == False):
                    CT1 = time.time()
                    root.after(600000 - int((CT1 - startTime) * 1000), lambda: pomodoroFn())
                crossF1 = Frame(root)
                crossF1.place(x=1490, y=0)
                crossB1 = Button(crossF1, text="X", height=1, width=5, font=('roboto', 10, 'bold'), bg="red", fg="white",
                                command=MMfunc)
                crossB1.pack()


                def checker():
                    list1 = []
                    count = 0
                    b = x.get().lower()
                    for i in b:
                        list1.append(i)
                    for i in list1:
                        if (i == 'c' or i == 'o' or i == 'n' or i == 'u' or i == 't'):
                            count = count + 1
                    if (count >= 7):
                        l8.pack()
                        l9.pack()
                        b9.pack()
                        b10.pack(pady=15)
                        frame_raise(winner,crossF1)
                        ingredient.delete(0, END)
                    else:
                        l7.pack()


                def checker1():
                    if (x1.get() == '1998'):
                        frame_raise(photoInterface, DG, code, backButton1, bar, allPhotos,crossF1)
                        e1.delete(0, END)
                    else:
                        l17.pack()


                def checker2():
                    list1 = []
                    count = 0
                    b = x2.get().lower()
                    for i in b:
                        list1.append(i)
                    for i in list1:
                        if (i == 'y' or i == 'u' or i == 'm'):
                            count = count + 1
                    if (count == 5):
                        frame_raise(coconut, backButton1, bar,crossF1)
                        e2.delete(0, END)
                    else:
                        l25.pack()
                def showPassword1fn():
                    e1.config(show="")
                    frame_raise(hidePassword1F)
                def showPassword2fn():
                    e2.config(show="")
                    frame_raise(hidePassword2F)
                def hidePassword1fn():
                    e1.config(show="*")
                    frame_raise(showPassword1F)
                def hidePassword2fn():
                    e2.config(show="*")
                    frame_raise(showPassword2F)
                secretRecipe = Frame(root)
                showPassword1F=Frame(root)
                showPassword2F=Frame(root)
                hidePassword1F = Frame(root)
                hidePassword2F = Frame(root)
                startMissionButton = Frame(root)
                backButton = Frame(root, bg="black")
                wallpaper2 = Frame(root)
                notepad = Frame(root)
                gallery = Frame(root)
                recipes = Frame(root)
                backButton1 = Frame(root)
                submitAnswer = Frame(root)
                think1 = Frame(root)
                answer = Frame(root)
                winner = Frame(root, bg="black", padx=700, pady=560, relief=SUNKEN, borderwidth=6)
                bar = Frame(root, bg="black")
                npInterface = Frame(root, pady=300)
                galleryPass = Frame(root, bg="white", pady=290)
                DG = Frame(root)
                photoInterface = Frame(root, bg="white", padx=600, pady=500)
                code = Frame(root)
                allPhotos = Frame(root)
                DGImage = Frame(root)
                codeImage = Frame(root)
                recipePass = Frame(root, bg="white", pady=370)
                coconut = Frame(root, bg="white", pady=300)
                coconut.place(x=0, y=0)
                showPassword1F.place(x=760,y=460)
                showPassword2F.place(x=760, y=580)
                hidePassword1F.place(x=760,y=460)
                hidePassword2F.place(x=760,y=580)
                recipePass.place(x=0, y=0)
                codeImage.place(x=0, y=0)
                DGImage.place(x=0, y=0)
                allPhotos.place(x=0, y=25)
                code.place(x=290, y=65)
                photoInterface.place(x=0, y=0)
                DG.place(x=0, y=65)
                galleryPass.place(x=0, y=0)
                npInterface.place(x=0, y=0)
                bar.place(x=0, y=0)
                winner.place(x=0, y=0)
                answer.place(x=200, y=200)
                backButton.place(x=400, y=700)
                secretRecipe.place(x=0, y=0)
                startMissionButton.place(x=770, y=700)
                wallpaper2.place(x=0, y=0)
                notepad.place(x=20, y=30)
                gallery.place(x=20, y=120)
                recipes.place(x=20, y=210)
                backButton1.place(x=750, y=700)
                submitAnswer.place(x=1100, y=645)
                img1 = Image.open("secretRecipe.png")
                img1 = img1.resize((screen_width, screen_height))
                img1 = ImageTk.PhotoImage(img1)
                img2 = ImageTk.PhotoImage(Image.open("startMissionButton.png"))
                img3 = ImageTk.PhotoImage(Image.open("backButton.png"))
                img4 = Image.open("wallpaper2.png")
                img4 = img4.resize((screen_width, screen_height))
                img4 = ImageTk.PhotoImage(img4)
                img5 = ImageTk.PhotoImage(Image.open("notepad.png"))
                img6 = ImageTk.PhotoImage(Image.open("gallery.png"))
                img7 = ImageTk.PhotoImage(Image.open("recipes.png"))
                img8 = ImageTk.PhotoImage(Image.open("backButton1.png"))
                img9 = ImageTk.PhotoImage(Image.open("submitAnswer.png"))
                img10 = ImageTk.PhotoImage(Image.open("think1.png"))
                img11 = ImageTk.PhotoImage(Image.open("DG.png"))
                img12 = ImageTk.PhotoImage(Image.open("code.png"))
                img13 = Image.open("DGImage.png")
                img13 = img13.resize((screen_width, screen_height))
                img13 = ImageTk.PhotoImage(img13)
                img14 = Image.open("codeImage.png")
                img14 = img14.resize((screen_width, screen_height))
                img14 = ImageTk.PhotoImage(img14)
                b1 = Button(startMissionButton, image=img2, bg="black",
                            command=lambda: frame_raise(wallpaper2, recipes, notepad, gallery
                                                        , submitAnswer, backButton1, bar,crossF1))
                showPassword1B=Button(showPassword1F,text="Show Password",command=showPassword1fn)
                showPassword2B=Button(showPassword2F, text="Show Password", command=showPassword2fn)
                hidePassword1B=Button(hidePassword1F,text="Hide Password ",command=hidePassword1fn)
                hidePassword2B = Button(hidePassword2F, text="Hide Password ", command=hidePassword2fn)
                showPassword1B.pack()
                showPassword2B.pack()
                hidePassword1B.pack()
                hidePassword2B.pack()
                b2 = Button(backButton, image=img3, bg="black", command=bk)
                b3 = Button(notepad, image=img5, command=lambda: frame_raise(npInterface, backButton1, bar,crossF1))
                b4 = Button(gallery, image=img6, command=lambda: frame_raise(galleryPass, backButton1, bar,showPassword1F,crossF1))
                b5 = Button(recipes, image=img7, command=lambda: frame_raise(recipePass, backButton1, bar,showPassword2F,crossF1))
                b6 = Button(backButton1, image=img8,
                            command=lambda: frame_raise(wallpaper2, recipes, notepad, gallery, backButton1,
                                                        submitAnswer, bar,crossF1))
                b7 = Button(submitAnswer, image=img9, command=lambda: frame_raise(answer, backButton1,crossF1))
                b8 = Button(answer, text="SUBMIT ANSWER", bg="green", fg="white", font="algerian 15 bold",
                            command=checker)
                b9 = Button(winner, text="Play Again", font="comicsansms 15 bold", command=bk)
                b10 = Button(winner, text="Main Menu", font="comicsansms 15 bold", command=q)
                b11 = Button(galleryPass, text="UNLOCK", font="comicsamsms 19", bg="purple", fg="white",
                             command=checker1)
                b12 = Button(DG, image=img11, command=lambda: frame_raise(DGImage, backButton1, bar,crossF1))
                b13 = Button(code, image=img12, command=lambda: frame_raise(codeImage, backButton1, bar,crossF1))
                b14 = Button(recipePass, text="UNLOCK", font="comicsamsms 19", bg="purple", fg="white",
                             command=checker2)
                b1.pack()
                b2.pack()
                b3.pack()
                b4.pack()
                b5.pack()
                b6.pack()
                b7.pack()
                b9.pack()
                b10.pack()
                b12.pack()
                b13.pack()
                l1 = Label(secretRecipe, image=img1)
                l2 = Label(wallpaper2, image=img4)
                l3 = Label(notepad, text="Notepad")
                l4 = Label(gallery, text="Gallery")
                l5 = Label(recipes, text="Recipes")
                l6 = Label(answer, image=img10)
                l7 = Label(answer, text="Wrong Answer! Try Again", font="comicsansms 9")
                l8 = Label(winner, text="Congratulations!", font="algerian 19 bold", bg="black", fg="green")
                l9 = Label(winner, text="You Cracked It", font="algerian 15 bold", bg="black", fg="green")
                l10 = Label(bar, font="comicsansms 9", bg="black", fg="white")
                l11 = Label(npInterface, text="My Final letter", font="algerian 30 bold", bg="white")
                l12 = Label(npInterface, text='''Dear Family,\n            If you are reading this,it means I'm already gone. But don't you feel
                                             sad for me , I've lived a full, enjoyable life 😄. And now that I'm gone, you can finally have 
                                             that secret cookie recipe you always asked me for. However, you'll have to work a little bit to get it!\n\n'''
                            , font="comicsansms 19", bg="white")
                l13 = Label(npInterface, text="Love you\nGrandma Dorothy", font="comicsansms 19", bg="white")
                l14 = Label(npInterface, text="First Hint : The year Google was founded.", font="comicsansms 19",
                            bg="white")
                l15 = Label(galleryPass, text="App Gallery is Password Protected", font="algerian 23 bold", bg="white",
                            padx=500)
                l16 = Label(galleryPass, text="Enter the password below", font="comicsansms 19", bg="white")
                l17 = Label(galleryPass, text="Wrong Password", font="comicsansms 19", bg="white")
                l18 = Label(allPhotos, text="All Photos", font="comicsansms 19 bold", padx=100, bg="white")
                l19 = Label(photoInterface, text="‌", bg="white")
                l20 = Label(DGImage, image=img13)
                l21 = Label(codeImage, image=img14)
                l22 = Label(recipePass, text="App recipes is Password Protected", font="algerian 23 bold", bg="white",
                            padx=500)
                l23 = Label(recipePass, text="Enter the password below", font="comicsansms 19", bg="white")
                l24 = Label(recipePass, text="Hint : BXPPB", font="comicsansms 19", bg="white")
                l25 = Label(recipePass, text="Wrong Password", font="comicsansms 19", bg="white")
                l26 = Label(coconut, text="Secret Cookie Recipe", font="algerian 23 bold", bg="white", padx=600)
                l27 = Label(coconut,
                            text="2 cups flour\n3 teaspoons baking powder\n1 teaspoon salt\n1/3 cup shortening\n2/3 cup milk\n1 egg",
                            font="comicsansms 19", bg="white")
                l28 = Label(coconut, text="Secret Ingredient: A tiny bit of Coconut", font="comicsansms 19 bold",
                            bg="white")
                l15.pack()
                l16.pack()
                l11.pack(padx=600, pady=30)
                l12.pack()
                l13.pack()
                l14.pack()
                l10.pack(padx=740)
                l18.pack()
                l19.pack()
                l20.pack()
                l21.pack()
                l22.pack()
                l23.pack()
                l24.pack()
                l26.pack()
                l27.pack()
                l28.pack()


                def timer():
                    A = time.strftime('%H')
                    a = int(A)
                    b = time.strftime('%M')
                    c = time.strftime('%S')
                    d = time.strftime('%p')
                    if (d == 'PM'):
                        a = a - 12
                    l10.config(text=f"{a}:{b}:{c} {d}")
                    l10.after(1000, timer)


                timer()

                l1.pack()
                l2.pack()
                l3.pack()
                l4.pack()
                l5.pack()
                l6.pack()
                x = StringVar()
                ingredient = Entry(answer, textvariable=x, font="comicsansms 23")
                ingredient.pack()
                b8.pack()
                x1 = StringVar()
                x2 = StringVar()
                e1 = Entry(galleryPass, textvariable=x1, font="comicsansms 19", borderwidth=6,show="*")
                e2 = Entry(recipePass, textvariable=x2, font="comicsansms 19", borderwidth=6,show="*")
                e1.pack(pady=50)
                e2.pack(pady=50)
                b11.pack()
                b14.pack()

                frame_raise(secretRecipe, startMissionButton, backButton,crossF1)
                root.mainloop()
    elif(op==4):
        li = ["rakshit", "priyam", "purav", "priyank", "rachit", "ramesh", "suresh", "stop"]


        def print_text():
            global x
            x = li[random.randint(0, len(li) - 1)]
            if running:
                updatename(x)
                root.after(650, lambda: print_text())

            # Define a function to stop the loop


        def on_stop():
            global running
            global x
            running = False
            if x == 'stop':
                msggreen()
                updatemsg("You won 🎊")
                root.after(600, lambda: BTMM())
            else:
                msgred()
                updatemsg("You lose 👎🏻")
                root.after(600, lambda: BTMM())


        def msgred():
            msg.configure(fg='red')


        def msggreen():
            msg.configure(fg='green')


        def updatename(x):
            names['text'] = x


        def updatemsg(x):
            msg['text'] = x


        running = True
        # main window
        root = Tk()
        root.title("Fastest Finger")
        root.iconbitmap('fav.ico')
        root.state('zoomed')
        if (pomodoro == False):
            CT1 = time.time()
            root.after(600000 - int((CT1 - startTime) * 1000), lambda: pomodoroFn())

        # heading
        crossF1 = Frame(root)
        crossF1.place(x=1490, y=0)
        crossB1 = Button(crossF1, text="X", height=1, width=5, font=('roboto', 10, 'bold'), bg="red", fg="white",
                        command=MMfunc)
        crossB1.pack()
        head = Frame(root)
        head.place(x=460, y=20)
        head_img = ImageTk.PhotoImage(Image.open("head1.png"))
        heading = Label(head, image=head_img)
        heading.pack()

        # messages
        mesg = Frame(root)
        mesg.place(x=670, y=750)
        msg = Label(mesg, text="", font=('', 25, 'bold'), fg="black")
        msg.pack()

        # names
        name = Frame(root)
        name.place(x=625, y=400)
        names = Label(name, text="priyam", font=('roboto', 50, 'bold'), fg="black")
        names.pack()

        # stop button
        stop1 = Frame(root)
        stop1.place(x=555, y=550)
        stop = Button(stop1, text="STOP", width=15, font=('roboto', 30, 'bold'), bg='#FFFF00', fg='#000000',
                      activebackground='red', activeforeground='white', command=lambda: on_stop())
        stop.pack()

        root.after(1000, lambda: print_text())
        root.mainloop()
    elif(op==5):
        c = 0


        # functions
        def frame_raise(frame, *more):
            frame.tkraise()
            for i in more:
                i.tkraise()


        def e():
            global tries
            tries = 5
            triesL.config(text=f"You have {tries} tries to guess the no.")
            frame_raise(GTN, rules, triesF, entryF, submitF, f1,crossF1)


        def b():
            global tries
            tries = 4
            triesL.config(text=f"You have {tries} tries to guess the no.")
            frame_raise(GTN, rules, triesF, entryF, submitF, f1,crossF1)


        def h():
            global tries
            tries = 3
            triesL.config(text=f"You have {tries} tries to guess the no.")
            frame_raise(GTN, rules, triesF, entryF, submitF, f1,crossF1)


        def submitfn():
            global tries
            if (a.get() >= 1 and a.get() <= 20):
                if (tries > 1):
                    if (a.get() == s):
                        checkerL.config(text="Congratulations! You guessed the number")
                        frame_raise(checkerF)
                        root.after(2000, lambda: frame_raise(PAF, MMF,crossF1))
                    elif (a.get() > s):
                        checkerL.config(text=f"Sorry! {a.get()} is wrong. My no. is less than that.")
                        triesL.config(text=f"You have {tries - 1} tries to guess the no.")
                        if (tries == 5):
                            l1.config(text=f"less than {a.get()}")
                        if (tries == 4):
                            l2.config(text=f"less than {a.get()}")
                        if (tries == 3):
                            l3.config(text=f"less than {a.get()}")
                        if (tries == 2):
                            l4.config(text=f"less than {a.get()}")
                        if (tries == 2):
                            triesL.config(text="Be Careful! This is your final chance")
                        frame_raise(checkerF, f1, f2, f3, f4,crossF1)
                        tries = tries - 1
                    elif (a.get() < s):
                        checkerL.config(text=f"Sorry! {a.get()} is wrong. My no. is more than that.")
                        triesL.config(text=f"You have {tries - 1} tries to guess the no.")
                        if (tries == 5):
                            l1.config(text=f"more than {a.get()}")
                        if (tries == 4):
                            l2.config(text=f"more than {a.get()}")
                        if (tries == 3):
                            l3.config(text=f"more than {a.get()}")
                        if (tries == 2):
                            l4.config(text=f"more than {a.get()}")
                        if (tries == 2):
                            triesL.config(text="Be Careful! This is your final chance")
                        frame_raise(checkerF, f1, f2, f3, f4,crossF1)
                        tries = tries - 1
                elif (tries == 1):
                    if (a.get() == s):
                        checkerL.config(text="Congratulations! You guessed the number")
                        frame_raise(checkerF,crossF1)
                        root.after(2000, lambda: frame_raise(PAF, MMF))
                    else:
                        checkerL.config(text=f"You lose! The no. was {s}")
                        frame_raise(checkerF,crossF1)
                        root.after(2000, lambda: frame_raise(PAF, MMF))
            else:
                checkerL.config(text="Please enter a no. between 1 and 20 only")
                frame_raise(checkerF,crossF1)





        while (c == 0):
            s = random.randint(1, 20)
            root = Tk()
            root.state("zoomed")
            root.title("Guess The Number")
            root.iconbitmap('fav.ico')
            if (pomodoro == False):
                CT1 = time.time()
                root.after(600000 - int((CT1 - startTime) * 1000), lambda: pomodoroFn())
            # frames
            crossF1 = Frame(root)
            crossF1.place(x=1490, y=0)
            crossB1 = Button(crossF1, text="X", height=1, width=5, font=('roboto', 10, 'bold'), bg="red", fg="white",
                            command=MMfunc)
            crossB1.pack()
            rules = Frame(root)
            rules.place(x=20, y=80)
            easy = Frame(root)
            balanced = Frame(root)
            hard = Frame(root)
            difficultyLevel = Frame(root)
            easy.place(x=600, y=250)
            balanced.place(x=600, y=425)
            hard.place(x=600, y=600)
            difficultyLevel.place(x=0, y=0)
            GTN = Frame(root)
            GTN.place(x=0, y=0)
            triesF = Frame(root)
            triesF.place(x=27, y=361)
            entryF = Frame(root)
            entryF.place(x=230, y=450)
            submitF = Frame(root)
            submitF.place(x=220, y=520)
            checkerF = Frame(root)
            checkerF.place(x=200, y=600)
            f1 = Frame(root)
            f1.place(x=1180, y=370)
            f2 = Frame(root)
            f2.place(x=1180, y=470)
            f3 = Frame(root)
            f3.place(x=1180, y=570)
            f4 = Frame(root)
            f4.place(x=1180, y=670)
            PAF = Frame(root)
            PAF.place(x=900, y=615)
            MMF = Frame(root)
            MMF.place(x=900, y=715)

            # images
            easyI = ImageTk.PhotoImage(Image.open("easy1.png"))
            balancedI = ImageTk.PhotoImage(Image.open("balanced1.png"))
            hardI = ImageTk.PhotoImage(Image.open("hard1.png"))
            difficultyLevelI = Image.open("difficultyLevel.png")
            difficultyLevelI = difficultyLevelI.resize((screen_width, screen_height))
            difficultyLevelI = ImageTk.PhotoImage(difficultyLevelI)
            GTNI = Image.open("GTN.png")
            GTNI = GTNI.resize((screen_width, screen_height))
            GTNI = ImageTk.PhotoImage(GTNI)

            # buttons
            easyB = Button(easy, image=easyI, command=e)
            balancedB = Button(balanced, image=balancedI, command=b)
            hardB = Button(hard, image=hardI, command=h)
            submitB = Button(submitF, text="SUBMIT", bg="white", fg="black", font=('Koning Display', 24, 'bold'),
                             command=submitfn)
            PAB = Button(PAF, text="Play Again", bg="white", fg="black", font=('Koning Display', 24, 'bold'),
                         command=lambda: root.destroy())
            MMB = Button(MMF, text="Main Menu", bg="white", fg="black", font=('Koning Display', 24, 'bold'),
                         command=lambda:BTMM())
            easyB.pack()
            balancedB.pack()
            hardB.pack()
            submitB.pack()
            PAB.pack()
            MMB.pack()

            # labels
            difficultyLevelL = Label(difficultyLevel, image=difficultyLevelI)
            difficultyLevelL.pack()
            GTNL = Label(GTN, image=GTNI)
            GTNL.pack()
            triesL = Label(triesF, text="", bg="white", fg="black", font=('Koning Display', 24, 'bold'))
            triesL.pack()
            checkerL = Label(checkerF, text="", bg="white", fg="black",
                             font=('Koning Display', 24, 'bold'))
            checkerL.pack()
            l1 = Label(f1, text="between 1 and 20", bg="white", fg="black", font=('Koning Display', 24, 'bold'))
            l1.pack()
            l2 = Label(f2, text="", bg="white", fg="black", font=('Koning Display', 24, 'bold'))
            l2.pack()
            l3 = Label(f3, text="", bg="white", fg="black", font=('Koning Display', 24, 'bold'))
            l3.pack()
            l4 = Label(f4, text="", bg="white", fg="black", font=('Koning Display', 24, 'bold'))
            l4.pack()

            # entries
            a = IntVar()
            entryE = Entry(entryF, textvariable=a, font=('Koning Display', 24, 'bold'), fg="black")
            entryE.pack()

            frame_raise(difficultyLevel, easy, balanced, hard,crossF1)
            root.mainloop()
    elif(op==6):

        pygame.init()


        clock = pygame.time.Clock()
        fps = 60

        screenwidth = 600
        screenheight = 600

        screen = pygame.display.set_mode((screenwidth, screenheight))
        pygame.display.set_caption("Flappy Bird")

        # define font
        font = pygame.font.SysFont('roboto', 60)

        # define colours
        white = (255, 255, 255)

        # define game variables
        ground_scroll = 0
        scroll_speed = 4
        flying = False
        game_over = False
        pipe_gap = 150
        pipe_frequency = 1500  # milliseconds
        last_pipe = pygame.time.get_ticks() - pipe_frequency
        score = 0
        pass_pipe = False

        # load images
        bg = pygame.image.load('background.png')
        ground_img = pygame.image.load('ground2.png')
        button_img = pygame.image.load('restart.png')


        def draw_text(text, font, text_col, x, y):
            img = font.render(text, True, text_col)
            screen.blit(img, (x, y))


        def reset_game():
            pipe_group.empty()
            flappy.rect.x = 100
            flappy.rect.y = int(screenheight / 2)
            score = 0
            return score


        class Bird(pygame.sprite.Sprite):
            def __init__(self, x, y):
                pygame.sprite.Sprite.__init__(self)
                self.images = []
                self.index = 0
                self.counter = 0
                for num in range(1, 4):
                    img = pygame.image.load(f'bird{num}.jfif')
                    self.images.append(img)
                self.image = self.images[self.index]
                self.rect = self.image.get_rect()
                self.rect.center = [x, y]
                self.vel = 0
                self.clicked = False

            def update(self):
                if flying == True:
                    # gravity
                    self.vel += 0.5
                    if self.vel > 8:
                        self.vel = 8
                    if self.rect.bottom < 500:
                        self.rect.y += int(self.vel)
                if game_over == False:

                    # jump
                    if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                        self.clicked = True
                        self.vel = -10
                    if pygame.mouse.get_pressed()[0] == 0:
                        self.clicked = False

                    # handle the animation
                    self.counter += 1
                    flap_cooldown = 5

                    if self.counter > flap_cooldown:
                        self.counter = 0
                        self.index += 1
                        if self.index >= len(self.images):
                            self.index = 0
                    self.image = self.images[self.index]

                    # rotate the bird
                    self.image = pygame.transform.rotate(self.images[self.index], self.vel * -2)
                else:
                    self.image = pygame.transform.rotate(self.images[self.index], -90)


        class Pipe(pygame.sprite.Sprite):
            def __init__(self, x, y, position):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load('Pipe.jfif')
                self.rect = self.image.get_rect()

                # position 1 is from the top,-1 is from the bottom
                if position == 1:
                    self.image = pygame.transform.flip(self.image, False, True)
                    self.rect.bottomleft = [x, y - int(pipe_gap / 2)]
                if position == -1:
                    self.rect.topleft = [x, y + int(pipe_gap / 2)]

            def update(self):
                self.rect.x -= scroll_speed
                if self.rect.right < 0:
                    self.kill()


        class Button():
            def __init__(self, x, y, image):
                self.image = image
                self.rect = self.image.get_rect()
                self.rect.topleft = (x, y)

            def draw(self):
                action = False
                # get mouse position
                pos = pygame.mouse.get_pos()

                # check if mouse is over the button
                if self.rect.collidepoint(pos):
                    if pygame.mouse.get_pressed()[0] == 1:
                        action = True

                # draw button
                screen.blit(self.image, (self.rect.x, self.rect.y))

                return action


        bird_group = pygame.sprite.Group()

        pipe_group = pygame.sprite.Group()

        flappy = Bird(100, int(screenheight / 2))

        bird_group.add(flappy)
        # create restart button instance
        button = Button((screenwidth // 2) - 50, (screenheight // 2) - 100, button_img)

        run = True
        while run:

            clock.tick(fps)

            # draw background
            screen.blit(bg, (0, 0))

            bird_group.draw(screen)
            bird_group.update()
            pipe_group.draw(screen)

            # draw thw ground
            screen.blit(ground_img, (ground_scroll, 500))

            # check the score
            if len(pipe_group) > 0:
                if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left \
                        and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right \
                        and pass_pipe == False:
                    pass_pipe = True
                if pass_pipe == True:
                    if bird_group.sprites()[0].rect.left >= pipe_group.sprites()[0].rect.right:
                        score = score + 1
                        pass_pipe = False

                draw_text(str(score), font, white, int(screenwidth / 2), 20)
            # look for collision
            if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy.rect.top < 0:
                game_over = True

            # check if bird has hit the ground
            if flappy.rect.bottom > 500:
                game_over = True
                flying = False
            if game_over == False and flying == True:

                # generate new pipes
                time_now = pygame.time.get_ticks()
                if time_now - last_pipe > pipe_frequency:
                    pipe_height = random.randint(-100, 100)
                    btm_pipe = Pipe(screenwidth, int(screenheight / 2) + pipe_height, -1)
                    top_pipe = Pipe(screenwidth, int(screenheight / 2) + pipe_height, 1)
                    pipe_group.add(btm_pipe)
                    pipe_group.add(top_pipe)
                    last_pipe = time_now
                # draw and scroll the ground
                ground_scroll -= scroll_speed
                if abs(ground_scroll) > 20:
                    ground_scroll = 0
                pipe_group.update()

            # check for game over and reset
            if game_over == True:
                def OnScreen(text, colour, x, y):
                    screenText = font.render(text, True, colour)
                    screen.blit(screenText, [x, y])
                o=1
                if(o==1):
                    OnScreen(f"Score : {score}", (0, 0, 255), 300, 100)
                    if(score>search_data(a1.get())[5]):
                        update_flappyscore(a1.get(),score)
                    OnScreen(f"High Score : {search_data(a1.get())[5]}",(0,0,255),250,300)
                    o=0
                if button.draw() == True:
                    game_over = False
                    score = reset_game()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
                    flying = True



            pygame.display.update()

        pygame.quit()
        op=0
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.15)
        pygame.mixer.music.load('mu.mp3')
        pygame.mixer.music.play()
    elif(op==7):
        pygame.init()


        def textOnScreen(text, colour, x, y):
            screenText = font.render(text, True, colour)
            gameWindow.blit(screenText, [x, y])


        def plotSnake(colour, snakeList, snakeSize):
            for x, y in snakeList:
                pygame.draw.rect(gameWindow, colour, [x, y, snakeSize, snakeSize])


        gameWindow = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
        clock = pygame.time.Clock()
        font = pygame.font.SysFont('helvetica', 55)
        pygame.display.set_caption("Snake Game")


        def gameLoop():
            pygame.init()
            gameWindow = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
            white = (255, 255, 255)
            black = (0, 0, 0)
            red = (255, 0, 0)
            green = (0, 255, 0)
            blue = (0, 0, 255)
            exitGame = False
            gameOver = False
            snakeX = 200
            snakeY = 400
            foodX = random.randint(100, screen_width - 50)
            foodY = random.randint(100, screen_height - 50)
            snakeSize = 20
            foodSize = 20
            fps = 40
            velocityX = 0
            velocityY = 0
            score = 0
            snakeLength = 1
            snakeList = []
            while exitGame == False:
                if (gameOver == True):
                    gameWindow.fill(black)
                    textOnScreen("Game Over!", red, screen_width / 2 - 150, screen_height / 2 - 100)
                    textOnScreen(f"Your score is {score}", red, screen_width / 2 - 170, screen_height / 2)
                    textOnScreen("Press m for main menu", red, screen_width / 2 - 235, screen_height / 2 + 200)
                    if(search_data(a1.get())[4]<score):
                        update_snakescore(a1.get(),score)
                    textOnScreen(f"High score : {search_data(a1.get())[4]}",red,screen_width/2-170,screen_height/2+100)
                    for event in pygame.event.get():
                        if (event.type == pygame.KEYDOWN):
                            if (event.key == pygame.K_m):
                                exitGame = True
                else:
                    for event in pygame.event.get():
                        if (event.type == pygame.QUIT):
                            exitGame = True
                        if (event.type == pygame.KEYDOWN):
                            if (event.key == pygame.K_RIGHT):
                                if (velocityX < 0):
                                    pass
                                else:
                                    velocityX = 3
                                    velocityY = 0
                                    fps += 5
                            if (event.key == pygame.K_LEFT):
                                if (velocityX > 0):
                                    pass
                                else:
                                    velocityX = -3
                                    velocityY = 0
                                    fps += 5
                            if (event.key == pygame.K_UP):
                                if (velocityY > 0):
                                    pass
                                else:
                                    velocityY = -3
                                    velocityX = 0
                                    fps += 5
                            if (event.key == pygame.K_DOWN):
                                if (velocityY < 0):
                                    pass
                                else:
                                    velocityY = 3
                                    velocityX = 0
                                    fps += 5
                    snakeX = snakeX + velocityX
                    snakeY = snakeY + velocityY
                    if (abs(foodX - snakeX) < 13 and abs(foodY - snakeY) < 13):
                        foodX = random.randint(100, screen_width - 50)
                        foodY = random.randint(100, screen_height - 50)
                        score = score + 1
                        snakeLength = snakeLength + 10

                    gameWindow.fill(green)
                    pygame.draw.rect(gameWindow, red, [foodX, foodY, foodSize, foodSize])
                    textOnScreen(f"Score: {score}", red, 5, 5)
                    head = []
                    head.append(snakeX)
                    head.append(snakeY)
                    snakeList.append(head)


                    if (len(snakeList) > snakeLength):
                        del snakeList[0]

                    if (snakeX < 0 or snakeX > screen_width or snakeY < 0 or snakeY > screen_height):
                        gameOver = True

                    if head in snakeList[:-1]:
                        gameOver=True


                    plotSnake(blue, snakeList, snakeSize)
                pygame.init()
                pygame.display.update()
                clock.tick(fps)
            pygame.quit()



        gameLoop()
        op = 0
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.15)
        pygame.mixer.music.load('mu.mp3')
        pygame.mixer.music.play()
    elif(op==8):
        root=Tk()
        root.state('zoomed')
        root.title("Coming Soon")
        root.iconbitmap('fav.ico')
        if (pomodoro == False):
            CT1 = time.time()
            root.after(600000 - int((CT1 - startTime) * 1000), lambda: pomodoroFn())
        comingSoonF=Frame(root)
        comingSoonF.place(x=0,y=0)
        comingSoonI = Image.open("comingsoon.png")
        comingSoonI = comingSoonI.resize((screen_width, screen_height))
        comingSoonI = ImageTk.PhotoImage(comingSoonI)
        comingSoonL=Label(comingSoonF,image=comingSoonI)
        comingSoonL.pack()
        CSF=Frame(root)
        CSF.place(x=650,y=715)
        CSB=Button(CSF,text="Main Menu",bg="white",fg="black",font=('Koning Display', 24, 'bold'),command=BTMM)
        CSB.pack()
        root.mainloop()