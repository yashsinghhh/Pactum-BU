import tkinter
import customtkinter
import sqlite3
import time

connection=sqlite3.connect("./database.db")
cur= connection.cursor()
customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("400x400")
app.title("PactumBU")


frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, text="PactumBU", justify=tkinter.CENTER, anchor=tkinter.CENTER, font=("Arial", 20, "bold"))
label_1.pack(pady=10, padx=10, side="top", fill="both", expand=True)

label_2 = customtkinter.CTkLabel(master=frame_1, text="Loading...", justify=tkinter.CENTER, anchor=tkinter.CENTER, font=("Arial", 10, "bold"))
label_2.pack(padx=10, side="top", fill="both", expand=True)
frame_2 = customtkinter.CTkFrame(master=app)


login_label = customtkinter.CTkLabel(master=frame_2, text="Login", justify=tkinter.CENTER, anchor=tkinter.CENTER, font=("Arial", 20, "bold"))
login_label.pack(pady=10, padx=10, side="top", fill="both", expand=True)

email = customtkinter.CTkEntry(master=frame_2, height=14, placeholder_text="Email")
email.pack(pady=10, padx=10, side="top", expand=True)

password_validation = customtkinter.CTkEntry(master=frame_2, show="*", placeholder_text="Password")
password_validation.pack(pady=10, padx=10, side="top", expand=True)

def login():
    user_email = email.get()
    password = password_validation.get()
    cur.execute("SELECT * FROM account WHERE email = ? AND password = ?", (user_email, password))
    data = cur.fetchall()
    if len(data) > 0:
        print("Login successful")
    else:
        print("Login failed")
    

login_button = customtkinter.CTkButton(master=frame_2, text="Login", command=login)
login_button.pack(pady=10, padx=10, side="top", expand=True)


def remove_splash():
    label_1.destroy()
    label_2.destroy()
    frame_1.destroy()
    frame_2.pack(pady=20, padx=60, fill="both", expand=True)

label_1.after(2000, remove_splash)


app.mainloop()