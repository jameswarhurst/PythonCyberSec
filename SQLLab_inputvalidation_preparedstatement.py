import sqlite3
import tkinter as tk

DB_NAME = 'vulnerable.db'


def create_database():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 username TEXT NOT NULL,
                 password TEXT NOT NULL)''')


    c.execute("INSERT INTO users (username, password) VALUES ('admin', 'password')")
    c.execute("INSERT INTO users (username, password) VALUES ('guest', 'guest123')")

    conn.commit()
    conn.close()


create_database()


def login():
    username = entry_username.get()
    password = entry_password.get()

    # Input validation
    if "'" in username or "'" in password:
        lbl_result.config(text="Invalid input. Please try again.")
        return

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # Prepared statement
    query = "SELECT * FROM users WHERE username=? AND password=?"
    c.execute(query, (username, password))
    user = c.fetchone()

    conn.close()

    if user:
        lbl_result.config(text="Login successful!")
    else:
        lbl_result.config(text="Invalid credentials. Please try again.")

window = tk.Tk()
window.title("Vulnerable Login Lab")


lbl_username = tk.Label(window, text="Username:")
lbl_username.pack()
entry_username = tk.Entry(window)
entry_username.pack()

lbl_password = tk.Label(window, text="Password:")
lbl_password.pack()
entry_password = tk.Entry(window, show="*")
entry_password.pack()

btn_login = tk.Button(window, text="Login", command=login)
btn_login.pack()


lbl_result = tk.Label(window, text="")
lbl_result.pack()

window.mainloop()
