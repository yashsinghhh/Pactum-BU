import tkinter as tk
import customtkinter
from PIL import Image
from user import user

class seller(user):

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
        canvas.pack(side="left", fill="x")
        self.cursor.execute(f"SELECT * FROM products WHERE seller_id = {self.id}")
        products = self.cursor.fetchall()
        for product in products:
            products_frame = customtkinter.CTkFrame(canvas)
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
        #button_1 = customtkinter.CTkButton(canvas, text="Add Product")
        #button_1.pack(padx=20, pady=20)
        canvas2 = tk.Canvas(tabview.tab("Your Orders"), background=tabview.tab("Your Orders")["bg"], bd=0, highlightthickness=0)
        canvas2.pack(side="left", fill="x")
        self.cursor.execute(f"SELECT * FROM orders WHERE seller_id = {self.id}")
        orders = self.cursor.fetchall()
        for order in orders:
            self.cursor.execute(f"SELECT * FROM products WHERE id = {order[1]}")
            product = self.cursor.fetchall()[0]
            order_frame = customtkinter.CTkFrame(canvas2)
            order_frame.pack(pady=10, padx=10, fill="x")
            my_image = customtkinter.CTkImage(light_image=Image.open(f"{product[2]}.png"),
                                            dark_image=Image.open(f"{product[2]}.png"),
                                            size=(100, 100))
            object_image = customtkinter.CTkLabel(order_frame, image=my_image, text="")
            object_image.grid(row=0, column=0, padx=10, pady=0, ipady=10)
            product_name = customtkinter.CTkLabel(order_frame, text=f"{product[2]}\n₹{product[5]}", justify=tk.CENTER, font=("Arial", 20))
            product_name.grid(row=0, column=1, padx=10, pady=0, ipady=10)
            order_c = customtkinter.CTkLabel(order_frame, text=f"{order[4]}\n{order[3]}", justify=tk.CENTER, font=("Arial", 20))
            order_c.grid(row=0, column=2, padx=10, pady=0, ipady=10)