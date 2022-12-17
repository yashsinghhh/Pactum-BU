import tkinter as tk
import customtkinter
from user import user
from PIL import Image
class buyer(user):
    def buy(self,product_id, previous_frame):
        from checkout1 import checkout

        checkout = checkout(self.main,self.name,product_id,self.id,self.cursor)
        checkout.create_frame(previous_frame)

    def create_frame(self,previous_frame):
        # Destroy prvious frame, create new frame with seller products and orders
        previous_frame.destroy()
        frame = customtkinter.CTkFrame(master=self.main)
        frame.pack(pady=10, padx=30, fill="both", expand=True)
        name = customtkinter.CTkLabel(master=frame, text=f"Hello {self.name}!", justify=tk.CENTER, font=("Arial", 20, "bold"))
        name.pack(pady=5, padx=5)
        self.cursor.execute(f"SELECT * FROM products")
        products = self.cursor.fetchall()
        outer_frame = customtkinter.CTkFrame(frame)
        for product in products:
            products_frame = customtkinter.CTkFrame(frame)
            products_frame.pack(pady=10, padx=10, fill="x")
            my_image = customtkinter.CTkImage(light_image=Image.open(f"{product[2]}.png"),
                                            dark_image=Image.open(f"{product[2]}.png"),
                                            size=(100, 100))
            product_image = customtkinter.CTkLabel(products_frame, image=my_image, text="")
            product_image.grid(row=0, column=0, padx=10, pady=0, ipady=10)
            product_name = customtkinter.CTkLabel(products_frame, text=f"{product[2]}", justify=tk.CENTER, font=("Arial", 20, "bold"))
            product_name.grid(row=0, column=1, padx=10, pady=0, ipady=10)
            product_price = customtkinter.CTkLabel(products_frame, text=f"₹{product[5]}", justify=tk.CENTER, font=("Arial", 20))
            product_price.grid(row=0, column=2, padx=10, pady=0, ipady=10)
            buy_button = customtkinter.CTkButton(products_frame, text="Buy", command=lambda product_id=product[0]: self.buy(product_id, previous_frame=frame))
            buy_button.grid(row=0, column=3, padx=10, pady=0, ipady=10)