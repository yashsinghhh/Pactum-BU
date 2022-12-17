import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Product Entry")

# Create label and entry widgets for name, price, and description
name_label = tk.Label(text="Name:")
price_label = tk.Label(text="Price:")
description_label = tk.Label(text="Description:")
name_entry = tk.Entry(width=50)
price_entry = tk.Entry(width=50)
description_entry = tk.Entry(width=50)

# Create the submit button and "Add Image" button
submit_button = tk.Button(text="Submit")
add_image_button = tk.Button(text="Add Image")

# Center the widgets using the pack layout manager
name_label.pack(pady=5)
name_entry.pack(pady=5)
price_label.pack(pady=5)
price_entry.pack(pady=5)
description_label.pack(pady=5)
description_entry.pack(pady=5)
submit_button.pack(pady=5)
add_image_button.pack(pady=5)

# Run the main loop
window.mainloop()
