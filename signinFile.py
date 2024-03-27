from tkinter import *
from tkinter import ttk
import sqlite3

def login():
    email = email_entry.get()
    password = password_entry.get()

    conn = sqlite3.connect('SignUpInfo.db')
    c = conn.cursor()

    c.execute('''SELECT * FROM users WHERE email=? AND password=?''', (email, password))
    user = c.fetchone()

    if user:
        status_label.config(text="Login Successful", foreground="green")
    else:
        status_label.config(text="Email or Password Incorrect", foreground="red")

    conn.close()

root = Tk()
root.geometry("250x200")
root.title("Login")

email_label = ttk.Label(root, text="Email:")
email_label.pack()
email_entry = ttk.Entry(root)
email_entry.pack()

password_label = ttk.Label(root, text="Password:")
password_label.pack()
password_entry = ttk.Entry(root, show="*")
password_entry.pack()

signin_button = ttk.Button(root, text="Sign In", command=login)
signin_button.pack()

status_label = ttk.Label(root, text="")
status_label.pack()

root.mainloop()