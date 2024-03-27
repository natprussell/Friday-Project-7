from tkinter import *
from tkinter import ttk
import sqlite3

def login():
    email = email_entry.get()
    password = password_entry.get()

    # Connect to the database
    conn = sqlite3.connect('SignUpInfo.db')
    c = conn.cursor()

    # Check if email and password exist in the database
    c.execute('''SELECT * FROM users WHERE email=? AND password=?''', (email, password))
    user = c.fetchone()

    if user:
        # Login successful
        status_label.config(text="Login Successful", foreground="green")
    else:
        # Email or password incorrect
        status_label.config(text="Email or Password Incorrect", foreground="red")

    # Close database connection
    conn.close()

# Create main window
root = Tk()
root.geometry("250x200")
root.title("Login")

# Create labels and entry boxes
email_label = ttk.Label(root, text="Email:")
email_label.pack()
email_entry = ttk.Entry(root)
email_entry.pack()

password_label = ttk.Label(root, text="Password:")
password_label.pack()
password_entry = ttk.Entry(root, show="*")
password_entry.pack()

# Create sign in button
signin_button = ttk.Button(root, text="Sign In", command=login)
signin_button.pack()

# Create status label
status_label = ttk.Label(root, text="")
status_label.pack()

root.mainloop()