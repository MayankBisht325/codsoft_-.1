import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x450")
root.resizable(False, False)
tasks = []
def update_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)
def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append(task)
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")
def delete_task():
    try:
        selected = task_listbox.curselection()[0]
        tasks.pop(selected)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

title_label = tk.Label(root, text="To-Do List", font=("Helvetica", 20, "bold"))
title_label.pack(pady=10)

task_entry = tk.Entry(root, width=45, font=("Helvetica", 15))
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", width=15, command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Selected Task", width=20, command=delete_task)
delete_button.pack(pady=5)

task_listbox = tk.Listbox(root, width=40, height=15, font=("Helvetica", 12))
task_listbox.pack(pady=10)

root.mainloop()
