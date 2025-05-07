import tkinter as tk  # Import tkinter as tk
import pymysql
from tkinter import *
from tkinter import Canvas
import re
from PIL import ImageTk, Image
from tkinter import messagebox
from main2 import start   # Add this line

mypass = "root"
mydatabase="music"
con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()  # Make cur a global variable


def register_user():
    u=0
    for widget in root.winfo_children():
        if not isinstance(widget, tk.Canvas):  # Keep the Canvas with the background image
            widget.destroy()

        # Create new frame for login form
    regis_frame = tk.Frame(root, bg='lightgray')
    regis_frame.place(relx=0.5, rely=0.5, anchor='center')
    def on_username_entered():

        username = username_entry.get()

        # Check if the username already exists
        cur.execute("SELECT * FROM UserCredentials WHERE username = %s", (username,))
        if cur.fetchone() is not None:
            messagebox.showinfo("Error", "Username already exists.")
            if messagebox.askyesno("Query", "Do you want to login instead?"):

                login_user()
            else:
                messagebox.showinfo("Info", "Please choose a different username.")
            return

        password_label.pack()
        password_entry.pack()
        password_button.pack()

    def on_password_entered():
        username = username_entry.get()
        password = password_entry.get()

        cur.execute("INSERT INTO UserCredentials (username, password) VALUES (%s, %s)", (username, password))

        # Insert a new artist with the same name as the username into the Artist table
        cur.execute("INSERT INTO Artist (artist_name) VALUES (%s)", (username,))
        con.commit()
        messagebox.showinfo("Success", "User registered successfully.")
        u=1
        # Call the login_user function after the user has been successfully registered
        login_user()

    username_label = tk.Label(regis_frame, text="Username", font='Helvetica 16 bold', bg='black',
                              fg='white')  # Add to login_frame
    username_entry = tk.Entry(regis_frame, font=("Helvetica", 16))  # Add to login_frame
    username_button = tk.Button(regis_frame, text="Next", command=on_username_entered)

    password_label = tk.Label(regis_frame, text="Password", font='Helvetica 16 bold', bg='black',
                              fg='white')  # Add to login_frame
    password_entry = tk.Entry(regis_frame, show="*", font=("Helvetica", 16))  # Add to login_frame
    password_button = tk.Button(regis_frame, text="Register", command=on_password_entered)




    username_label.pack()
    username_entry.pack()
    username_button.pack()
    return u


def login_user():
    for widget in root.winfo_children():
        if not isinstance(widget, tk.Canvas):  # Keep the Canvas with the background image
            widget.destroy()

        # Create new frame for login form
    login_frame = tk.Frame(root, bg='lightgray')
    login_frame.place(relx=0.5, rely=0.5, anchor='center')


    def on_login_click1():
        username = username_entry.get()
        password = password_entry.get()
        try:
            # Check if the username and password match a user in the UserCredentials table
            cur.execute("SELECT * FROM UserCredentials WHERE username = %s AND password = %s", (username, password))
            user = cur.fetchone()

            if user is not None:
                messagebox.showinfo("Success", "Login successful.")
                #cur.execute("SELECT id FROM Artist WHERE artist_name = %s", (username,))
                #artist_id = cur.fetchone()[0]
                cur.execute("SELECT id, artist_name FROM Artist WHERE artist_name = %s", (username,))
                artist_id, artist_name = cur.fetchone()
                # Display the artist_id in the root window
                #artist_id_label = tk.Label(root, text=f"Artist ID: {artist_id}")
                #artist_id_label.pack()

                root.destroy()
                start(root,artist_id,artist_name)
                return True
            else:
                messagebox.showinfo("Error", "Invalid username or password.")
                return False
        except pymysql.Error as e:
            messagebox.showinfo("Error", f"Failed to login user: {str(e)}")

    username_label = tk.Label(login_frame, text="Username", font='Helvetica 16 bold', bg='black', fg='white') # Add to login_frame
    username_entry = tk.Entry(login_frame, font=("Helvetica", 16))  # Add to login_frame
    password_label = tk.Label(login_frame, text="Password", font='Helvetica 16 bold', bg='black', fg='white') # Add to login_frame
    password_entry = tk.Entry(login_frame, show="*", font=("Helvetica", 16))  # Add to login_frame


    username_label.pack()
    username_entry.pack()
    password_label.pack()
    password_entry.pack()

    login_button = tk.Button(login_frame, text="Login", font='Helvetica 10 bold', bg='black', fg='white',
                             command=on_login_click1)
    login_button.pack()
def on_register_login_click():

    s=register_user()
    if s==1:
        login_user()


def on_login_click():


    login_user()

global  img ,Canvas1
root = tk.Tk()
root.title("Welcome Page")
root.minsize(width=400,height=400)
root.geometry("800x600")

background_image = Image.open("main.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size
newImageSizeWidth = int(imageSizeWidth * 0.7)
newImageSizeHeight = int(imageSizeHeight * 0.7)
background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.Resampling.LANCZOS)
img = ImageTk.PhotoImage(background_image)

Canvas1 = tk.Canvas(root)
Canvas1.create_image(300, 340, image=img)
Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
Canvas1.pack(expand=True, fill=tk.BOTH)

register_login_button = tk.Button(root, text="Register and Login",font='Helvetica 10 bold', bg='black', fg='white', command=on_register_login_click)
register_login_button.place(relx=0.28, rely=0.3, relwidth=0.45, relheight=0.1)

login_button = tk.Button(root, text="Login", command=on_login_click)
login_button.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

root.mainloop()