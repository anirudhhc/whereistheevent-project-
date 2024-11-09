import tkinter as tk
from tkinter import ttk

# Initialize main window
root = tk.Tk()
root.geometry("400x400")
root.title("Length Converter App")

# Conversion function
def convert_length():
    try:
        meters = float(entry_meters.get())
        centimeters = meters * 100
        result_label.config(text=f"{centimeters} cm")
    except ValueError:
        result_label.config(text="Please enter a valid number")

# Create and place widgets
# Label for meter input
label_meters = ttk.Label(root, text="Enter length in meters:")
label_meters.pack(pady=10)

# Entry for meter input
entry_meters = ttk.Entry(root, width=20)
entry_meters.pack(pady=5)

# Convert button
convert_button = ttk.Button(root, text="Convert to Centimeters", command=convert_length)
convert_button.pack(pady=10)

# Label to display result
result_label = ttk.Label(root, text="0 cm", font=("Arial", 14))
result_label.pack(pady=20)

# Run the main loop
root.mainloop()
