import tkinter
import customtkinter as tk
import time
tk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
tk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = tk.CTk()
app.geometry("400x400")
app.title("Pactum BU")

main_frame= tk.CTkFrame(master=app)
main_frame.pack(pady=20, padx=20, fill="both", expand=True)

splash = tk.CTkFrame(master=main_frame)
splash.grid(row=0, column=0, pady=20, padx=20, sticky="nsew")

label_1 = tk.CTkLabel(master=splash, justify=tkinter.CENTER, text="Pactum BU")
label_1.pack(pady=10, padx=10, expand=True)

login = tk.CTkFrame(master=main_frame)
login.grid(row=0, column=0, pady=20, padx=20, sticky="nsew")

label_2 = tk.CTkLabel(master=login, justify=tkinter.LEFT, text="Login")
label_2.pack(pady=10, padx=10, expand=True)

splash.tkraise()

app.mainloop()