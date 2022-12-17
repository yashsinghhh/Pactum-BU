import tkinter as tk
import customtkinter


class seller():
    def __init__(self, masterwin, name, id):
        self.main = masterwin
        self.name = name
        self.id = id

    def create_frame(self,previous_frame):
        # Destroy prvious frame, create new frame with seller products and orders
        previous_frame.destroy()
        frame = customtkinter.CTkFrame(master=self.main)
        frame.pack(pady=10, padx=30, fill="both", expand=True)
        name = customtkinter.CTkLabel(master=frame, text=f"Hello {self.name}!", justify=tk.CENTER, font=("Arial", 20, "bold"))
        name.pack(pady=5, padx=5)
        tabview = customtkinter.CTkTabview(frame)
        tabview.pack(padx=5, pady=5, fill= "both", expand=True)
        tabview.add("Your Products")  # add tab at the end
        tabview.add("Your Orders")  # add tab at the end
        tabview.set("Your Products")  # set currently visible tab
        canvas = tk.Canvas(tabview.tab("Your Products"),  background=tabview.tab("Your Products")["bg"], bd=0, highlightthickness=0)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar = customtkinter.CTkScrollbar(tabview.tab("Your Products"), orientation="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        button_1 = customtkinter.CTkButton(canvas, text="Add Product")
        button_1.pack(padx=20, pady=20)


