from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

mypass = "root"
mydatabase="music"
con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()
global_main_root = None


def deletesong(aid):
    title = songInfo1.get()
    global artist_id
    artist_id = aid
    try:
        # Check if the artist_id of the song matches the artist_id of the logged-in user
        cur.execute("SELECT * FROM track WHERE title = %s AND artist_id = %s", (title, artist_id))
        song = cur.fetchone()

        if song is not None:
            cur.execute(
                "DELETE FROM track, album USING track JOIN album JOIN artist ON track.artist_id = artist.id AND track.album_id = album.id WHERE track.title = %s AND artist.id = %s",
                (title, artist_id))
            con.commit()
            messagebox.showinfo('Success', "Song Record Deleted Successfully")
        else:
            messagebox.showinfo("Error", "You do not have permission to delete this song.")
    except:
        messagebox.showinfo("Please Check Song Title")

    songInfo1.delete(0, END)
    root.destroy()
    global_main_root.deiconify()

def delete(rt,aid):
    global img, songInfo1, songInfo2, songInfo3, songInfo4, songInfo5, Canvas1, con, cur, root,aid1,global_main_root
    aid1=aid
    global_main_root = rt
    root = Toplevel()
    root.title("Delete Music Recordd")
    root.minsize(width=400, height=400)
    root.geometry("800x600")

    background_image = Image.open("delete.jpg")
    [imageSizeWidth, imageSizeHeight] = background_image.size
    newImageSizeWidth = int(imageSizeWidth * 0.8)
    newImageSizeHeight = int(imageSizeHeight * 0.8)
    background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.Resampling.LANCZOS)
    img = ImageTk.PhotoImage(background_image)

    Canvas1 = Canvas(root)
    Canvas1.create_image(300, 340, image=img)
    Canvas1.config(bg="black", width=newImageSizeWidth, height=newImageSizeHeight)
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#dfdee2", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Delete Song Record", font='Helvetica 14 bold', bg="#010103", fg='white', )
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg="#010103")
    labelFrame.place(relx=0.25, rely=0.4, relwidth=0.5, relheight=0.2)

    lb2 = Label(labelFrame, text="Song Title:", font='Helvetica 11 bold', bg="#000000", fg='white')
    lb2.place(relx=0.05, rely=0.5)

    songInfo1 = Entry(labelFrame)
    songInfo1.place(relx=0.3, rely=0.5, relwidth=0.62)

    SubmitBtn = Button(root, text="Submit", font='Helvetica 11 bold', bg="#010103", fg='white', command=lambda: deletesong(aid1))
    SubmitBtn.place(relx=0.28, rely=0.75, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", font='Helvetica 11 bold', bg="#010103", fg='white', command=lambda: [root.destroy(), global_main_root.deiconify()])
    quitBtn.place(relx=0.53, rely=0.75, relwidth=0.18, relheight=0.08)

    root.mainloop()