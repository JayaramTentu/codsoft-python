import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import datetime


root = tk.Tk()
root.title("Professional To-Do List")
root.geometry("750x750")
root.resizable(width=False,height=False)
root.config(bg="#e3f2fd")


tasks = []


def show_error(message):
    error_label.config(text=message)
    error_label.after(3000, lambda: error_label.config(text=""))  


def add_task():
    task_text = task_entry.get().strip()
    due_date = due_date_picker.get()
    
    if task_text:
        tasks.append({"name": task_text, "completed": False, "due_date": due_date})
        task_entry.delete(0, tk.END)
        update_task_list()
    else:
        show_error("Please enter a valid task.")

def remove_task(task_index):
    tasks.pop(task_index)
    update_task_list()

def toggle_task_status(task_index):
    tasks[task_index]["completed"] = not tasks[task_index]["completed"]
    update_task_list()

def update_task_list():

    for widget in task_frame.winfo_children():
        widget.destroy()

    for i, task in enumerate(tasks):
        
        task_bg = "#ffffff" if not task["completed"] else "#d1e7dd"
        task_card = tk.Frame(task_frame, bg=task_bg, pady=10, padx=10, bd=0, relief="flat")
        task_card.pack(fill="x", pady=5, padx=15)

        
        task_text = tk.Label(
            task_card,
            text=f"{task['name']} (Due: {task['due_date']})",
            bg=task_bg,
            fg="#333333" if not task["completed"] else "#888888",
            font=("Arial", 12, "italic" if task["completed"] else "normal"),
            wraplength=250,
        )
        task_text.pack(side="left", padx=(0, 10))

        complete_button_text = "✓" if task["completed"] else "✔"
        complete_button_color = "#28a745" if not task["completed"] else "#ffc107"
        complete_button = tk.Button(
            task_card,
            text=complete_button_text,
            bg=complete_button_color,
            fg="white",
            font=("Arial", 12, "bold"),
            width=3,
            command=lambda index=i: toggle_task_status(index)
        )
        complete_button.pack(side="right", padx=5)

      
        delete_button = tk.Button(
            task_card,
            text="✖",
            bg="#dc3545",
            fg="white",
            font=("Arial", 10, "bold"),
            command=lambda index=i: remove_task(index)
        )
        delete_button.pack(side="right", padx=5)

container_frame = tk.Frame(root, bg="#e3f2fd")
container_frame.grid(row=0, column=0, sticky="n", pady=10)


error_label = tk.Label(container_frame, text="", fg="red", bg="#e3f2fd", font=("Arial", 12, "bold"))
error_label.pack(pady=(5, 0))


input_frame = tk.Frame(container_frame, bg="#e3f2fd")
input_frame.pack(pady=10, fill="x")

task_label = tk.Label(input_frame, text="Enter Task:", bg="#e3f2fd", fg="#333333", font=("Arial", 12))
task_label.grid(row=0, column=0, padx=(10, 5), pady=(10, 5), sticky="e")


task_entry = tk.Entry(input_frame, font=("Arial", 14), width=18, bg="#ffffff", fg="#333333", relief="solid", bd=1)
task_entry.grid(row=0, column=1, padx=(5, 10), pady=(10, 5), sticky="w")


date_label = tk.Label(input_frame, text="Select the Date:", bg="#e3f2fd", fg="#333333", font=("Arial", 12))
date_label.grid(row=0, column=2, padx=(10, 5), pady=(10, 5), sticky="e")


due_date_picker = DateEntry(input_frame, width=12, font=("Arial", 12), background="#007bff", foreground="white", borderwidth=2)
due_date_picker.set_date(datetime.now())  
due_date_picker.grid(row=0, column=3, padx=(5, 10), pady=(10, 5), sticky="w")


add_button = tk.Button(
    input_frame,
    text="Add Task",
    bg="#007bff",
    fg="white",
    font=("Arial", 11, "bold"),
    relief="flat",
    width=10,
    command=add_task
)
add_button.grid(row=0, column=4, padx=(5, 10), pady=(10, 5), sticky="w")


task_frame = tk.Frame(container_frame, bg="#e3f2fd")
task_frame.pack(fill="both", expand=True, pady=(5, 10))


root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()
