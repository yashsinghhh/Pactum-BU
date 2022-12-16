import tkinter as tk
from tkinter import PhotoImage

# Create the main window
window = tk.Tk()
window.title("Order Product")

# Load the image file
image = PhotoImage(
    file="/home/itsomsarraf/Documents/GitHub/Pactum-BU/tkinter/product.png")

# Create label and entry widgets for name, description, address, and phone number
name_label = tk.Label(text="Name:")
description_label = tk.Label(text="Description:")
address_label = tk.Label(text="Address:")
phone_label = tk.Label(text="Phone:")
name_entry = tk.Entry(width=50)
description_entry = tk.Entry(width=50)
address_entry = tk.Entry(width=50)
phone_entry = tk.Entry(width=50)

# Create the "Order" button
order_button = tk.Button(text="Order")

# Display the image and labels
image_label = tk.Label(image=image)
image_label.pack()
name_label.pack(pady=5)
description_label.pack(pady=5)

# Display the entry widgets and "Order" button
name_entry.pack(pady=5)
description_entry.pack(pady=5)
address_label.pack(pady=5)
address_entry.pack(pady=5)
phone_label.pack(pady=5)
phone_entry.pack(pady=5)
order_button.pack(pady=5)

# Run the main loop
window.mainloop()
