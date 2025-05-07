from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql
from viewdm import *
from viewindie import *
from viewpop import *
from viewrap import *
from viewdm import *

mypass = "root"
mydatabase="music"

con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()
grt=None

def viewplaylists(rt):
    global grt
    grt=rt
    root = Toplevel()
    root.title("View Playlists")
    root.minsize(width=400, height=400)
    root.geometry("800x600")

    mypass = "root"
    mydatabase = "music"

    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cur = con.cursor()

    background_image = Image.open("viewplaylists.jpg")
    [imageSizeWidth, imageSizeHeight] = background_image.size
    newImageSizeWidth = int(imageSizeWidth * 0.25)
    newImageSizeHeight = int(imageSizeHeight * 0.25)
    background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight),  Image.Resampling.LANCZOS)
    img = ImageTk.PhotoImage(background_image)

    Canvas1 = Canvas(root)
    Canvas1.create_image(300, 340, image=img)
    Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#dbd1c6", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="View Playlists", font='Helvetica 14 bold', bg="#6b4c38", fg='white', )
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    btn1 = Button(root, text="Electronic Dance Music", font='Helvetica 10 bold', bg='black', fg='white',
                  command=lambda: [root.withdraw(), viewdm(root)])
    btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

    btn2= Button(root, text="Ultimate Indie", font='Helvetica 10 bold', bg='black', fg='white', command=lambda: [root.withdraw(), viewindie(root)])
    btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)
    btn3 = Button(root, text="Make Me Pop", font='Helvetica 10 bold', bg='black', fg='white', command=lambda: [root.withdraw(), viewpop(root)])
    btn3.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

    btn4 = Button(root, text="Chill Rap", font='Helvetica 10 bold', bg='black', fg='white', command=lambda: [root.withdraw(), viewrap(root)])
    btn4.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

    quitBtn = Button(root, text="QUIT", font='Helvetica 10 bold', bg='black', fg='white', command=lambda: [root.destroy(), grt.deiconify()])
    quitBtn.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)

    root.mainloop()