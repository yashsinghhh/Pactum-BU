import tkinter as tk
import customtkinter
class buyer():
    def __init__(self, masterwin, name, id, cur):
        self.main = masterwin
        self.name = name
        self.id = id
        self.cursor = cur

    def create_frame(self,previous_frame):
        # Destroy prvious frame, create new frame with seller products and orders
        previous_frame.destroy()
        frame = customtkinter.CTkFrame(master=self.main)
        frame.pack(pady=10, padx=30, fill="both", expand=True)
        name = customtkinter.CTkLabel(master=frame, text=f"Hello {self.name}!", justify=tk.CENTER, font=("Arial", 20, "bold"))
        name.pack(pady=5, padx=5)

