import tkinter as tk
from tkinter import ttk

def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def toggle_task():
    selected_task = task_list.curselection()
    if selected_task:
        task_index = selected_task[0]
        task_text = task_list.get(task_index)
        if task_text.startswith("[Completed] "):
            task_text = task_text.replace("[Completed] ", "")
        else:
            task_text = f"[Completed] {task_text}"
        task_list.delete(task_index)
        task_list.insert(tk.END, task_text)

def clear_task():
    selected_task = task_list.curselection()
    if selected_task:
        task_index = selected_task[0]
        task_list.delete(task_index)

def clear_all_tasks():
    task_list.delete(0, tk.END)

app = tk.Tk()
app.title("To-Do List")

label = tk.Label(app, text="Enter Task:")
label.pack()
task_entry = tk.Entry(app)
task_entry.pack()

list_label = tk.Label(app, text="To-Do List:")
list_label.pack()
task_list = tk.Listbox(app)
task_list.pack()

add_button = ttk.Button(app, text="Add Task", command=add_task)
toggle_button = ttk.Button(app, text="Toggle Task", command=toggle_task)
clear_button = ttk.Button(app, text="Clear Task", command=clear_task)
clear_all_button = ttk.Button(app, text="Clear All Tasks", command=clear_all_tasks)

add_button.pack()
toggle_button.pack()
clear_button.pack()
clear_all_button.pack()

style = ttk.Style()
style.configure("TButton", padding=6, font=("Helvetica", 12))

app.mainloop()
