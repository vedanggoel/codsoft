
import tkinter as tk
import random
import string

# Function to generate a random password
def generate_password():
    length = int(length_entry.get())
    if length < 4:
        password_var.set("Password length must be at least 4 characters")
        return
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    password_var.set(password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create a label for the password
password_label = tk.Label(root, text="Generated Password:")
password_label.pack()

# Create a variable to store the generated password
password_var = tk.StringVar()
password_var.set("")

# Display the generated password
password_display = tk.Label(root, textvariable=password_var, font=("Helvetica", 16))
password_display.pack()

# Create a label and entry for password length
length_label = tk.Label(root, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

# Create a button to generate a password
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

root.mainloop()
