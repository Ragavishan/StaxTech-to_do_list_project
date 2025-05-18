import tkinter as tk
from tkinter import messagebox
import json
import os

TASK_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f)

def add_task():
    task = entry.get()
    if task:
        tasks.append({"task": task, "completed": False})
        entry.delete(0, tk.END)
        update_listbox()
        save_tasks(tasks)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def mark_done():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks[index]["completed"] = True
        update_listbox()
        save_tasks(tasks)
    else:
        messagebox.showwarning("Selection Error", "Please select a task to mark as done.")

def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        del tasks[index]
        update_listbox()
        save_tasks(tasks)
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        status = "✓" if task["completed"] else "✗"
        listbox.insert(tk.END, f"[{status}] {task['task']}")

root = tk.Tk()
root.title("To-Do List App")

tasks = load_tasks()

frame = tk.Frame(root)
frame.pack(pady=10)

entry = tk.Entry(frame, width=40)
entry.pack(side=tk.LEFT, padx=(0, 10))

add_btn = tk.Button(frame, text="Add Task", command=add_task)
add_btn.pack(side=tk.LEFT)

listbox = tk.Listbox(root, width=60)
listbox.pack(pady=10)

done_btn = tk.Button(root, text="Mark as Done", command=mark_done)
done_btn.pack(pady=(0, 5))

delete_btn = tk.Button(root, text="Delete Task", command=delete_task)
delete_btn.pack()

update_listbox()

root.mainloop()