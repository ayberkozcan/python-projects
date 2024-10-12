from tkinter import *
import customtkinter as ctk
import os
from datetime import datetime

class NoteTakingApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_default_color_theme("dark-blue")
    
        self.title("Note Taker")
        self.geometry("600x700")

        self.current_theme = "dark"

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.theme_icon_path = os.path.join(BASE_DIR, "icons/theme_icon.png")
        self.edit_icon_path = os.path.join(BASE_DIR, "icons/edit_icon.png")
        self.delete_icon_path = os.path.join(BASE_DIR, "icons/bin_icon.png")

        self.widgets()

    def widgets(self):
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
        self.theme_button.place(x=500, y=600)
        
        self.title_note_entry = ctk.CTkEntry(
            self,
            placeholder_text="Title...",
            width=500,
            height=40,
            border_width=1,
            corner_radius=10
        )
        self.title_note_entry.pack(pady=20)
        
        self.note_entry = ctk.CTkTextbox(
            self,
            width=500,
            height=300,
            border_width=1,
            corner_radius=10
        )
        self.note_entry.pack(pady=10)

        self.save_note_button = ctk.CTkButton(
            self,
            text="Save Note",
            fg_color="#bb0000",
            hover_color="#a70000",
            command=self.create_note,
            width=50,
            height=50
        )
        self.save_note_button.place(x=50, y=420)

        self.list_notes_button = ctk.CTkButton(
            self,
            text="Notes",
            command=self.list_manage_notes,
            width=50,
            height=50
        )
        self.list_notes_button.place(x=500, y=420)

        self.customize_button = ctk.CTkButton(
            self,
            text="Customize",
            command=self.customize_text,
            width=50,
            height=50
        )
        self.customize_button.place(x=150, y=420)

        self.result_label = ctk.CTkLabel(
            self,
            text="",
            font=("Helvetica", 20)
        )
        self.result_label.place(x=250, y=500)
        
    def switch_theme(self):
        if self.current_theme == "dark":
            ctk.set_appearance_mode("light")
            self.current_theme = "light"
        else:
            ctk.set_appearance_mode("dark")
            self.current_theme = "dark"

    def create_note(self):
        note_content = self.note_entry.get("1.0", "end-1c")
        note_title = self.title_note_entry.get()

        if note_title.strip() == "":
            self.result_label.configure(text="Title is required!", text_color="red")
            return

        notes_directory = "notes/"
        if not os.path.exists(notes_directory):
            os.makedirs(notes_directory)

        note_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        note_data = f"Title: {note_title}\nDate: {note_date}\n\n{note_content}"

        with open(os.path.join(notes_directory, note_title + ".txt"), "w") as file:
            file.write(note_data)

        self.result_label.configure(text="Note Saved!", text_color="#03c000")
        
        self.title_note_entry.delete(0, END)
        self.note_entry.delete("1.0", END)

        self.after(1000, self.clear_message)

    def customize_text(self):
        window = ctk.CTkToplevel(self)
        window.title("Customize")
        window.geometry("250x250")

        font_label = ctk.CTkLabel(
            window,
            text="Font: "
        )
        font_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.font_comboBox = ctk.CTkComboBox(
            window,
            values=["Helvetica", "Arial", "Verdana", "Tahoma"],
        )
        self.font_comboBox.set("Helvetica")
        self.font_comboBox.grid(row=0, column=1, padx=10, pady=10)

        fontsize_label = ctk.CTkLabel(
            window,
            text="Size: "
        )
        fontsize_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.fontsize_comboBox = ctk.CTkComboBox(
            window,
            values=["2", "4", "6", "8", "10", "12", "14", "16", "18", "20", "22", "24", "26", "28", "30"],
        )
        self.fontsize_comboBox.set("20")
        self.fontsize_comboBox.grid(row=1, column=1, padx=10, pady=10)

        self.font_result_label = ctk.CTkLabel(
            window,
            text="",
            font=("Helvetica", 20)
        )
        self.font_result_label.grid(row=2, column=1, padx=10, pady=10)

        window.grid_rowconfigure(3, weight=1)

        save_font_changes_button = ctk.CTkButton(
            window,
            text="Save Changes",
            fg_color="green",
            command=lambda: self.apply_font()
        )
        save_font_changes_button.grid(row=3, column=1, padx=10, pady=10)

    def apply_font(self):
        font = self.font_comboBox.get()
        font_size = int(self.fontsize_comboBox.get())

        self.note_entry.configure(font=(font, font_size))

        self.font_result_label.configure(text="Font Saved!", text_color="green")
        self.after(2000, self.font_clear_message)    
        
    def list_manage_notes(self, window=None):
        notes_directory = "notes"
        files = os.listdir(notes_directory)

        if window is None:
            window = ctk.CTkToplevel(self)
            window.title("List of Notes")
            window.geometry("400x300")
        
        self.window = window

        for i, file_name in enumerate(files, start=1):
            file_path = os.path.join(notes_directory, file_name)
            with open(file_path, "r") as file:
                lines = file.readlines()
                if len(lines) > 1:
                    note_title = lines[0].replace("Title: ", "").strip()
                    note_date = lines[1].replace("Date: ", "").strip()
                else:
                    note_title = file_name.strip(".txt")
                    note_date = "Unknown"

            formatted_label = f"{note_title} ({note_date})"

            label = ctk.CTkLabel(window, text=formatted_label)
            label.grid(row=i, column=0, padx=10, pady=5, sticky="w")

            edit_icon = PhotoImage(file=self.edit_icon_path)
            edit_icon = edit_icon.subsample(25, 25)

            edit_button = ctk.CTkButton(
                window,
                image=edit_icon,
                text="",
                command=lambda file_name=file_name: self.edit_note(file_name),
                fg_color="green",
                width=30
            )
            edit_button.grid(row=i, column=1)

            delete_icon = PhotoImage(file=self.delete_icon_path)
            delete_icon = delete_icon.subsample(25, 25)

            delete_button = ctk.CTkButton(
                window,
                image=delete_icon,
                text="",
                command=lambda file_name=file_name: self.delete_note(file_name, window), 
                fg_color="red",
                width=30
            )
            delete_button.grid(row=i, column=2)

        window.grid_rowconfigure(len(files)+1, weight=1)

        self.clear_screen_button = ctk.CTkButton(
            window,
            text="Clear Screen",
            command=self.clear_screen
        )
        self.clear_screen_button.grid(row=len(files) + 2, column=1, pady=10)

    def edit_note(self, file_name):
        notes_directory = "notes/"
        file_path = os.path.join(notes_directory, file_name)

        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                lines = file.readlines()
                if len(lines) > 1:
                    note_title = lines[0].replace("Title: ", "").strip()
                    note_content = "".join(lines[3:])

                self.title_note_entry.delete(0, END)
                self.title_note_entry.insert(0, note_title)

                self.note_entry.delete("1.0", END)
                self.note_entry.insert("1.0", note_content)

            self.save_note_button.configure(
                text="Update Note",
                command=lambda: self.update_existing_note(file_name)
            )
            self.result_label.configure(text="Note Loaded", text_color="yellow")
        else:
            self.result_label.configure(text="Note not found!", text_color="red")

        self.after(2000, self.clear_message)    

    def update_existing_note(self, file_name):
        note_content = self.note_entry.get("1.0", "end-1c")
        note_title = self.title_note_entry.get()

        if note_title.strip() == "":
            self.result_label.configure(text="Title is required!", text_color="red")
            return
        
        notes_directory = "notes/"
        file_path = os.path.join(notes_directory, file_name)

        note_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        note_data = f"Title: {note_title}\nDate: {note_date}\n\n{note_content}"

        with open(file_path, "w") as file:
            file.write(note_data)

        self.result_label.configure(text="Note Updated!", text_color="green")

        self.title_note_entry.delete(0, END)
        self.note_entry.delete("1.0", END)

        self.save_note_button.configure(
            text="Save Note",
            command=self.create_note
        )

        self.after(2000, self.clear_message)

    def delete_note(self, file_name, window):
        notes_directory = "notes/"
        file_path = os.path.join(notes_directory, file_name)

        if os.path.exists(file_path):
            os.remove(file_path)
            self.result_label.configure(text=f"{file_name} deleted!", text_color="red")
            self.update_note_list(window)
        else:
            self.result_label.configure(text="File not found!", text_color="red")

        self.after(2000, self.clear_message)

    def update_note_list(self, window):
        for widget in window.winfo_children():
            widget.destroy()
        
        self.list_manage_notes(window)

    def clear_message(self):
        self.result_label.configure(text="")

    def font_clear_message(self):
        self.font_result_label.configure(text="")

    def clear_screen(self):
        self.title_note_entry.delete(0, END)
        self.note_entry.delete("1.0", END)

        for widget in self.winfo_children():
            widget.destroy()

        self.widgets()

if __name__ == "__main__":
    app = NoteTakingApp()
    app.mainloop()
