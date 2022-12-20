import tkinter
import customtkinter
import sqlite3
import time


user_name = ""
user_id = 0
seller=False

connection=sqlite3.connect("./database.db",isolation_level=None)
cur= connection.cursor()
customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("800x800")
app.title("PactumBU")


frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, text="PactumBU", justify=tkinter.CENTER, anchor=tkinter.CENTER, font=("Arial", 40, "bold"))
label_1.pack(pady=10, padx=10, side="top", fill="both", expand=True)

label_2 = customtkinter.CTkLabel(master=frame_1, text="Loading...", justify=tkinter.CENTER, anchor=tkinter.CENTER, font=("Arial", 20, "bold"))
label_2.pack(padx=10, side="top", fill="both", expand=True)
frame_2 = customtkinter.CTkFrame(master=app)


login_label = customtkinter.CTkLabel(master=frame_2, text="Login", justify=tkinter.CENTER, anchor=tkinter.CENTER, font=("Arial", 40, "bold"))
login_label.pack(pady=10, padx=10, side="top", fill="both", expand=True)

email = customtkinter.CTkEntry(master=frame_2, height=50, placeholder_text="Email")
email.pack(pady=10, padx=10, side="top", fill="x")

password_validation = customtkinter.CTkEntry(master=frame_2, height=50, show="*", placeholder_text="Password")
password_validation.pack(pady=10, padx=10, side="top", fill="x")

def login():
    global user_name
    global user_id
    global seller
    user_email = email.get()
    password = password_validation.get()
    cur.execute("SELECT * FROM account WHERE email = ? AND password = ?", (user_email, password))
    data = cur.fetchall()
    response = customtkinter.CTkToplevel(app)
    response.geometry("400x400")
    if len(data) > 0:
        user_name = data[0][1]
        user_id = data[0][0]
        if data[0][4] == 1:
            seller = True
        res_label = customtkinter.CTkLabel(master=response, text="Login successful", justify=tkinter.CENTER, anchor=tkinter.CENTER, font=("Arial", 20, "bold"))
        res_label.pack(pady=10, padx=10, side="top", fill="both", expand=True)
        def proceed():
            global seller
            response.destroy()
            if seller:
                import seller
                s= seller.seller(app, user_name, user_id, cur)
                s.create_frame(frame_2)
            else:
                import buyer
                b = buyer.buyer(app, user_name, user_id, cur)
                b.create_frame(frame_2)              

        proceed_button = customtkinter.CTkButton(master=response, text="Proceed", command=proceed)
        proceed_button.pack(pady=10, padx=10, side="top", expand=True)  


    else:
        res_label = customtkinter.CTkLabel(master=response, text="Login Failed", justify=tkinter.CENTER, anchor=tkinter.CENTER, font=("Arial", 20, "bold"))
        res_label.pack(pady=10, padx=10, side="top", fill="both", expand=True)        
        res_label.after(3000, lambda: response.destroy())
    

login_button = customtkinter.CTkButton(master=frame_2, text="Login", command=login)
login_button.pack(pady=10, padx=10, side="top", expand=True)


def remove_splash():
    label_1.destroy()
    label_2.destroy()
    frame_1.destroy()
    frame_2.pack(pady=20, padx=60, fill="both", expand=True)

label_1.after(2000, remove_splash)


app.mainloop()
