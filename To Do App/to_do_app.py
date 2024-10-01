from tkinter import *
from datetime import datetime
import customtkinter as ctk
import os

class ToDoApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_default_color_theme("dark-blue")

        self.title("To Do")
        self.geometry("500x800")
        
        self.current_theme = "dark"

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.theme_icon_path = os.path.join(BASE_DIR, "icons/theme_icon.png")
        self.add_task_icon_path = os.path.join(BASE_DIR, "icons/add_task_icon.png")
        self.trash_can_icon_path = os.path.join(BASE_DIR, "icons/trash_can_icon.png")
        self.confirmation_icon_path = os.path.join(BASE_DIR, "icons/confirmation_icon.png")

        self.widgets()
        self.task_list()

    def switch_theme(self):

        if self.current_theme == "dark":
            ctk.set_appearance_mode("light")
            self.current_theme = "light"
        else:
            ctk.set_appearance_mode("dark")
            self.current_theme = "dark"

    def create_task(self):
        self.add_entry_button.pack_forget()
        self.add_entry.pack(pady=10)
        self.add_task_button.pack(pady=10)

    def add_task(self):
        try:
            with open("tasks.txt", "r") as file:
                tasks = file.readlines()
        except FileNotFoundError:
            tasks = []

        if len(tasks) >= 8:
            self.result.configure(text="Task limit reached! (8 max)", text_color="red")
        else:
            task = self.add_entry.get()

            if task:
                current_date = datetime.now().strftime("%d/%m/%Y")
                with open("tasks.txt", "a") as file:
                    file.write(f"{current_date} - {task}\n")
                self.result.configure(text="Task Saved!", text_color="green")
                self.task_list()
                self.add_entry.delete(0, END)
            else:
                self.result.configure(text="No task entered!", text_color="red")
        
        self.after(2000, self.clear_message)

        self.add_entry.pack_forget()
        self.add_task_button.pack_forget()
        self.add_entry_button.pack(side="bottom", pady=10)

    def clear_message(self):
        self.result.configure(text="")

    def complete_task(self, task_index):
        try:
            with open("tasks.txt", "r") as file:
                lines = file.readlines()

            if 0 <= task_index - 1 < len(lines):
                if lines[task_index - 1].startswith("[x]"):
                    lines[task_index - 1] = f"{lines[task_index - 1].lstrip('[x]').strip()}\n"
                else:
                    lines[task_index - 1] = f"[x] {lines[task_index - 1].strip()}\n"
            
                with open("tasks.txt", "w") as file:
                    file.writelines(lines)

            self.task_list()

        except FileNotFoundError:
            self.result.configure(text="No Tasks Available...", text_color="gray")

    def task_list(self):
        if hasattr(self, 'records_frame'):
            self.records_frame.destroy()

        try:
            with open("tasks.txt", "r") as file:
                tasks = file.readlines()

            if tasks:
                self.task_labels = []

                self.records_frame = ctk.CTkFrame(self)
                self.records_frame.pack(pady=10, fill="x")

                for i, task in enumerate(tasks, start=1):
                    formatted_task = task.strip()

                    if formatted_task.startswith("[x]"):
                        task_label = ctk.CTkLabel(master=self.records_frame, text=formatted_task[4:], font=("Helvetica", 20, "overstrike"))
                    else:
                        task_label = ctk.CTkLabel(master=self.records_frame, text=formatted_task, font=("Helvetica", 20))

                    task_label.grid(row=i, column=0, padx=10, pady=5, sticky='w')
                    self.task_labels.append(task_label)

                    completed_button = ctk.CTkButton(master=self.records_frame, image=self.confirmation_icon, text="", command=lambda idx=i: self.complete_task(idx), width=30)
                    completed_button.grid(row=i, column=1, padx=10, pady=5)

                    delete_button = ctk.CTkButton(master=self.records_frame, image=self.trash_can_icon, text="", command=lambda idx=i: self.delete_task(idx), fg_color="red", width=30)
                    delete_button.grid(row=i, column=2, padx=10, pady=5)

            else:
                self.result.configure(text="No Tasks Available...", text_color="gray")

        except FileNotFoundError:
            self.result.configure(text="No Tasks Available...", text_color="gray")


    def delete_task(self, task_index):
        try:
            with open("tasks.txt", "r") as file:
                lines = file.readlines()

            if 0 <= task_index - 1 < len(lines):
                del lines[task_index - 1]

                with open("tasks.txt", "w") as file:
                    file.writelines(lines)

            self.task_list()

        except FileNotFoundError:
            self.result.configure(text="No Tasks Available...", text_color="gray")

    def widgets(self):
        self.header_homepage = ctk.CTkLabel(
            self,
            text="To Do App",
            font=("Helvetica", 40)
        )
        self.header_homepage.pack(pady=50)

        theme_icon = PhotoImage(file=self.theme_icon_path)
        theme_icon = theme_icon.subsample(8, 8)

        self.theme_button = ctk.CTkButton(
            self,
            image=theme_icon,
            text="",
            command=self.switch_theme,
            width=40,
            height=40
        )
        self.theme_button.place(x=400, y=40)

        self.add_entry = ctk.CTkEntry(
            self,
            placeholder_text="...",
            width=200,
            height=30,
            border_width=1,
            corner_radius=10
            )
        
        self.add_entry.bind("<Return>", lambda event: self.add_task())

        add_task_icon = PhotoImage(file=self.add_task_icon_path)
        add_task_icon = add_task_icon.subsample(10, 10)

        self.add_entry_button = ctk.CTkButton(
            self,
            image=add_task_icon,
            text="",
            command=self.create_task,
            width=40,
            height=40
        )
        self.add_entry_button.pack(side="bottom", pady=50)

        self.add_task_button = ctk.CTkButton(
            self,
            text="Add Task",
            command=self.add_task,
            width=100,
            height=40
        )

        self.result = ctk.CTkLabel(
            self,
            text="",
            font=("Helvetica", 28),
        )
        self.result.pack(pady=50)

        self.trash_can_icon = PhotoImage(file=self.trash_can_icon_path)
        self.trash_can_icon = self.trash_can_icon.subsample(20, 20)

        self.confirmation_icon = PhotoImage(file=self.confirmation_icon_path)
        self.confirmation_icon = self.confirmation_icon.subsample(20, 20)

if __name__ == "__main__":
    app = ToDoApp()
    app.mainloop()