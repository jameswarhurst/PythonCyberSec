import sqlite3
import tkinter as tk

DB_NAME = 'vulnerable.db'

# Create a vulnerable SQLite database and insert sample data
def create_database():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # Create a users table
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 username TEXT NOT NULL,
                 password TEXT NOT NULL)''')

    # Insert sample data
    c.execute("INSERT INTO users (username, password) VALUES ('admin', 'password')")
    c.execute("INSERT INTO users (username, password) VALUES ('guest', 'guest123')")

    conn.commit()
    conn.close()

# Initialize the vulnerable database
create_database()

# Login function
def login():
    username = entry_username.get()
    password = entry_password.get()

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # Vulnerable to SQL injection
    query = "SELECT * FROM users WHERE username='%s' AND password='%s'" % (username, password)
    c.execute(query)
    user = c.fetchone()

    conn.close()

    if user:
        lbl_result.config(text="Login successful!")
    else:
        lbl_result.config(text="Invalid credentials. Please try again.")

# Create the main window
window = tk.Tk()
window.title("Vulnerable Login Lab")

# Create labels and entry fields
lbl_username = tk.Label(window, text="Username:")
lbl_username.pack()
entry_username = tk.Entry(window)
entry_username.pack()

lbl_password = tk.Label(window, text="Password:")
lbl_password.pack()
entry_password = tk.Entry(window, show="*")
entry_password.pack()

# Create a login button
btn_login = tk.Button(window, text="Login", command=login)
btn_login.pack()

# Create a label for displaying the login result
lbl_result = tk.Label(window, text="")
lbl_result.pack()

# Run the Tkinter event loop
window.mainloop()
