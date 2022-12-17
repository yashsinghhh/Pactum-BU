import customtkinter
import tkinter as tk
from PIL import Image
class checkout():
    def __init__(self, masterwin, name, product_id, user_id, cur):
        self.main = masterwin
        self.name = name
        self.user_id = user_id
        self.product_id = product_id
        self.cursor = cur

    def order_placed(self, previous_frame, order_id):
        previous_frame.destroy()
        frame = customtkinter.CTkFrame(master=self.main)
        frame.pack(pady=10, padx=30, fill="both", expand=True)
        name = customtkinter.CTkLabel(master=frame, text=f"Order Placed", justify=tk.CENTER, font=("Arial", 20, "bold"))
        name.pack(pady=5, padx=5)
        order_id_label = customtkinter.CTkLabel(master=frame, text=f"Order ID: {order_id}", justify=tk.CENTER, font=("Arial", 20, "bold"))
        order_id_label.pack(pady=5, padx=5)
        product = self.cursor.execute("SELECT * FROM products WHERE id = ?", (self.product_id,)).fetchall()[0]
        product_image = customtkinter.CTkImage(light_image=Image.open(f"{product[2]}.png"),
                                            dark_image=Image.open(f"{product[2]}.png"),
                                            size=(100, 100))
        product_image_label = customtkinter.CTkLabel(master=frame, image=product_image, text="")
        product_image_label.pack(pady=5, padx=5)
        product_name = customtkinter.CTkLabel(master=frame, text=f"Product: {product[2]}", justify=tk.CENTER, font=("Arial", 20, "bold"))
        product_name.pack(pady=5, padx=5)
        product_price = customtkinter.CTkLabel(master=frame, text=f"Price: ₹{product[5]}", justify=tk.CENTER, font=("Arial", 20, "bold"))
        product_price.pack(pady=5, padx=5)
        thanks = customtkinter.CTkLabel(master=frame, text=f"Thank you for shopping with us!", justify=tk.CENTER, font=("Arial", 20, "bold"))
        thanks.pack(pady=5, padx=5)
        quit = customtkinter.CTkButton(master=frame, text="Quit", command=self.main.destroy)
        quit.pack(pady=5, padx=5)


    def order(self, address, phone, previous_frame):
        seller_id = self.cursor.execute("SELECT seller_id FROM products WHERE id = ?", (self.product_id,)).fetchall()[0][0]
        self.cursor.execute("INSERT INTO orders (product_id, user_id, seller_id, address, phone) VALUES (?,?,?,?,?)", (self.product_id, self.user_id, seller_id, address, phone))
        order_id = self.cursor.execute("SELECT id FROM orders WHERE product_id = ? AND user_id = ? AND seller_id = ? AND address = ? AND phone = ?", (self.product_id, self.user_id, seller_id, address, phone)).fetchall()[0][0]
        self.order_placed(previous_frame, order_id) 

    def create_frame(self,previous_frame):
        previous_frame.destroy()
        frame = customtkinter.CTkFrame(master=self.main)
        frame.pack(pady=10, padx=30, fill="both", expand=True)
        name = customtkinter.CTkLabel(master=frame, text=f"Checkout", justify=tk.CENTER, font=("Arial", 20, "bold"))
        name.pack(pady=5, padx=5)
        self.cursor.execute("SELECT * FROM products WHERE id = ?", (self.product_id,))
        data = self.cursor.fetchall()
        product_name = customtkinter.CTkLabel(master=frame, text=f"Product: {data[0][2]}", justify=tk.CENTER, font=("Arial", 20, "bold"))
        product_name.pack(pady=5, padx=5)
        product_price = customtkinter.CTkLabel(master=frame, text=f"Price: ₹{data[0][5]}", justify=tk.CENTER, font=("Arial", 20, "bold"))
        product_price.pack(pady=5, padx=5)
        address_label= customtkinter.CTkLabel(master=frame, text="Address:", justify=tk.CENTER, font=("Arial", 10))
        address_label.pack(pady=5, padx=5)
        address_entry = customtkinter.CTkEntry(master=frame, width=150, height=50)
        address_entry.pack(pady=5, padx=5)
        phone_label= customtkinter.CTkLabel(master=frame, text="Phone:", justify=tk.CENTER, font=("Arial", 10))
        phone_label.pack(pady=5, padx=5)
        phone_entry = customtkinter.CTkEntry(master=frame, width=150,height=50)
        phone_entry.pack(pady=5, padx=5)
        order_button = customtkinter.CTkButton(master=frame, text="Order", command=lambda: self.order(address_entry.get(), phone_entry.get(), frame))
        order_button.pack(pady=5, padx=5)

