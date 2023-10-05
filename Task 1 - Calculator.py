
import tkinter as tk

# Function to update the display
def update_display(value):
    current = display_var.get()
    if current == "0":
        display_var.set(value)
    else:
        display_var.set(current + value)

# Function to perform calculations
def calculate():
    try:
        result = str(eval(display_var.get()))
        display_var.set(result)
    except Exception as e:
        display_var.set("Error")

# Function to clear the display
def clear():
    display_var.set("0")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create a display
display_var = tk.StringVar()
display_var.set("0")
display = tk.Entry(root, textvariable=display_var, font=("Helvetica", 20), justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=10, ipady=10)

# Define the calculator buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

# Create and place the buttons in the grid
row_val = 1
col_val = 0
for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, font=("Helvetica", 16), command=lambda b=button: update_display(b) if b != "=" else calculate()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Create a clear button
tk.Button(root, text="C", padx=20, pady=20, font=("Helvetica", 16), command=clear).grid(row=row_val, column=col_val)
root.mainloop()
