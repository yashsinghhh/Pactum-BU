import customtkinter
import tkinter as tk
class seller():
    def __init__(self, masterwin, name, product_id, user_id, cur):
        self.main = masterwin
        self.name = name
        self.user_id = user_id
        self.product_id = product_id
        self.cursor = cur

    def order(self, address, phone, previous_frame):
        seller_id = self.cursor.execute("SELECT seller_id FROM products WHERE product_id = ?", (self.product_id,)).fetchall()[0][0]
        self.cursor.execute("INSERT INTO orders (product_id, user_id, seller_id, address, phone) VALUES (?,?,?,?,?)", (self.product_id, self.user_id, seller_id, address, phone))
        order_id = self.cursor.execute("SELECT order_id FROM orders WHERE product_id = ? AND user_id = ? AND seller_id = ? AND address = ? AND phone = ?", (self.product_id, self.user_id, seller_id, address, phone)).fetchall()[0][0]
        previous_frame.destroy()

    def create_frame(self,previous_frame):
        previous_frame.destroy()
        frame = customtkinter.CTkFrame(master=self.main)
        frame.pack(pady=10, padx=30, fill="both", expand=True)
        name = customtkinter.CTkLabel(master=frame, text=f"Checkout", justify=tk.CENTER, font=("Arial", 20, "bold"))
        name.pack(pady=5, padx=5)
        self.cursor.execute("SELECT * FROM products WHERE product_id = ?", (self.product_id,))
        data = self.cursor.fetchall()
        product_name = customtkinter.CTkLabel(master=frame, text=f"Product: {data[0][1]}", justify=tk.CENTER, font=("Arial", 20, "bold"))
        product_name.pack(pady=5, padx=5)
        product_price = customtkinter.CTkLabel(master=frame, text=f"Price: {data[0][2]}", justify=tk.CENTER, font=("Arial", 20, "bold"))
        product_price.pack(pady=5, padx=5)
        address_label= customtkinter.CTkLabel(master=frame, text="Address:", justify=tk.CENTER, font=("Arial", 10))
        address_label.pack(pady=5, padx=5)
        address_entry = customtkinter.CTkEntry(master=frame, width=50)
        address_entry.pack(pady=5, padx=5)
        phone_label= customtkinter.CTkLabel(master=frame, text="Phone:", justify=tk.CENTER, font=("Arial", 10))
        phone_label.pack(pady=5, padx=5)
        phone_entry = customtkinter.CTkEntry(master=frame, width=50)
        phone_entry.pack(pady=5, padx=5)
        order_button = customtkinter.CTkButton(master=frame, text="Order", command=lambda: self.order(address_entry.get(), phone_entry.get(), frame))
        order_button.pack(pady=5, padx=5)

