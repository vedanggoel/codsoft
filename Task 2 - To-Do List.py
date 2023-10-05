
import tkinter as tk

# Function to add a task to the list
def add_task():
    task = task_entry.get()
    if task:
        todo_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)

# Function to remove a selected task
def remove_task():
    selected_task = todo_list.curselection()
    if selected_task:
        todo_list.delete(selected_task)

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create a task entry field
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

# Create an "Add Task" button
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

# Create a listbox to display tasks
todo_list = tk.Listbox(root, width=30)
todo_list.pack()

# Create a "Remove Task" button
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()

root.mainloop()
