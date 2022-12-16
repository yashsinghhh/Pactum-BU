import tkinter
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("400x400")
app.title("PactumBU")


frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, text="PactumBU", justify=tkinter.CENTER, anchor=tkinter.CENTER, font=("Arial", 20, "bold"))
label_1.pack(pady=10, padx=10, side="top", fill="both", expand=True)

app.mainloop()