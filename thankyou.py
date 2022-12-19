import tkinter as tk


window = tk.Tk()
window.title("Order Confirmation")


thank_you_label = tk.Label(
    text="Thank you for your order!", padx=20, pady=20, anchor="center")
thank_you_label.pack()


order_id_label = tk.Label(text="Order ID: 0001",
                          padx=20, pady=20, anchor="center")
order_id_label.pack()


order_placed_label = tk.Label(
    text="Your order has been placed.", padx=20, pady=20, anchor="center")
order_placed_label.pack()

window.mainloop()
