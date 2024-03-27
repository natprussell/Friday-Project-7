import tkinter as tk
import sqlite3

def signup():
    email = email_entry.get()
    password = password_entry.get()
    reenter_password = reenter_password_entry.get()

    if "@" not in email:
        status_label.config(text="Invalid email format. Please enter a valid email.")

    elif password == reenter_password:
        # Save to database
        conn = sqlite3.connect('SignUpInfo.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users (email TEXT, password TEXT)''')
        c.execute('''INSERT INTO users (email, password) VALUES (?, ?)''', (email, password))
        conn.commit()
        conn.close()

        # Clear entries
        email_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        reenter_password_entry.delete(0, tk.END)

        # Inform user
        status_label.config(text="Sign up successful!")
    else:
        # Inform user
        status_label.config(text="Passwords do not match. Please try again.")


root = tk.Tk()
root.title("Sign Up")
root.geometry("250x250")

# Create labels and entry boxes
email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

reenter_password_label = tk.Label(root, text="Re-enter Password:")
reenter_password_label.pack()
reenter_password_entry = tk.Entry(root, show="*")
reenter_password_entry.pack()

# Create sign up button
signup_button = tk.Button(root, text="Sign up now", command=signup)
signup_button.pack()

# Create status label
status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
