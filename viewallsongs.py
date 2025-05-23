from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox, ttk
import tkinter as tk
import pymysql
mypass = "root"
mydatabase="music"

con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()
grt=None

def viewallsongs(rt):
    global grt
    grt=rt
    root = Tk()
    root.title("View All Songs")
    root.minsize(width=40, height=4)
    root.geometry("1000x400")

    tree = ttk.Treeview(root, column=("c1", "c2", "c3", "c4", "c5",), show='headings')
    tree.column("#1", anchor=tk.CENTER)
    tree.heading("#1", text="Title")
    tree.column("#2", anchor=tk.CENTER)
    tree.heading("#2", text="Artist")
    tree.column("#3", anchor=tk.CENTER)
    tree.heading("#3", text="Album")
    tree.column("#4", anchor=tk.CENTER)
    tree.heading("#4", text="Genre")
    tree.column("#5", anchor=tk.CENTER)
    tree.heading("#5", text="Release Year")
    tree.grid(sticky=(N, S, W, E))
    root.treeview = tree
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    tree.pack(expand=True, fill=BOTH)

    try:
        cur.execute(
            "select track.title, artist.artist_name, album.album_name, genre.genre_name, track.rlsyr from track join album join artist join genre on track.artist_id=artist.id and track.album_id=album.id and track.genre_id=genre.id order by track.title;")
        rows = cur.fetchall()
        con.commit()
        for i in rows:
            tree.insert("", tk.END, values=i)
    except:
        messagebox.showinfo('Error', "Failed To Fetch Songs From The Database")

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=lambda: [root.destroy(), grt.deiconify()])
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()