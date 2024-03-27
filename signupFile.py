from tkinter import *
from tkinter import ttk
import sqlite3

root = Tk()
root.geometry("150x150")
root.title("Sign Up")


def signup():
    email = email_entry.get()
    password = password_entry.get()
    reenter_password = reenter_password_entry.get()

    if password == reenter_password:
        conn = sqlite3.connect('SignUpInfo.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users (email TEXT, password TEXT)''')
        c.execute('''INSERT INTO users (email, password) VALUES (?, ?)''', (email, password))
        conn.commit()
        conn.close()

        email_entry.delete(0, ttk.END)
        password_entry.delete(0, ttk.END)
        reenter_password_entry.delete(0, ttk.END)

        status_label.config(text="Sign up successful!")
    else:
        status_label.config(text="Passwords do not match. Please try again.")

email_label = ttk.Label(root, text="Email:")
email_label.pack()
email_entry = ttk.Entry(root)
email_entry.pack()

password_label = ttk.Label(root, text="Password:")
password_label.pack()
password_entry = ttk.Entry(root, show="*")
password_entry.pack()

reenter_password_label = ttk.Label(root, text="Re-enter Password:")
reenter_password_label.pack()
reenter_password_entry = ttk.Entry(root, show="*")
reenter_password_entry.pack()

signup_button = ttk.Button(root, text="Sign up now", command=signup)
signup_button.pack()

status_label = ttk.Label(root, text="")
status_label.pack()

root.mainloop()