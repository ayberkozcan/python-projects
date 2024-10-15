from tkinter import *
import customtkinter as ctk
import os
from datetime import datetime

class NoteTakingApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_default_color_theme("dark-blue")
    
        self.title("Note Taking App")
        self.geometry("600x700")

        self.current_theme = "dark"

        self.font = "Helvetica"
        self.font_size = 20

        self.password = ""
        self.tag_combobox = ""

        self.access_note = False

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.theme_icon_path = os.path.join(BASE_DIR, "icons/theme_icon.png")
        self.edit_icon_path = os.path.join(BASE_DIR, "icons/edit_icon.png")
        self.delete_icon_path = os.path.join(BASE_DIR, "icons/bin_icon.png")

        self.widgets()

    def widgets(self):
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
            height=250,
            border_width=1,
            corner_radius=10
        )
        self.note_entry.pack(pady=10)

        self.tag_combobox = ctk.CTkComboBox(
            self,
            values=["None", "Personal", "Work", "Interest", "Shopping", "Reminders", "Other"],
        )
        self.tag_combobox.set("None")
        self.tag_combobox.pack(pady=10)

        self.save_note_button = ctk.CTkButton(
            self,
            text="Save Note",
            fg_color="#28a745",
            hover_color="#218838",
            command=self.create_note,
            width=50,
            height=50
        )
        self.save_note_button.place(x=50, y=420)

        self.customize_button = ctk.CTkButton(
            self,
            text="Customize",
            command=self.customize_text,
            width=50,
            height=50
        )
        self.customize_button.place(x=150, y=420)

        self.clear_screen_button = ctk.CTkButton(
            self,
            text="Clear Screen",
            command=self.clear_screen,
            width=50,
            height=50
        )
        self.clear_screen_button.place(x=250, y=420)

        self.set_password_button = ctk.CTkButton(
            self,
            text="Set Password",
            fg_color="#6c757d",
            hover_color="#5a6268",
            command=self.set_password_window,
            width=50,
            height=50
        )
        self.set_password_button.place(x=350, y=420)

        self.list_notes_button = ctk.CTkButton(
            self,
            text="Note List",
            fg_color="#17a2b8",
            hover_color="#138496",
            command=self.list_manage_notes,
            width=50,
            height=50
        )
        self.list_notes_button.place(x=490, y=420)

        self.result_label = ctk.CTkLabel(
            self,
            text="",
            font=("Helvetica", 20)
        )
        self.result_label.place(x=250, y=500)

        self.warning_label = ctk.CTkLabel(
            self,
            text="Don't forget to press the 'Update Note' button and select the tag after each change!",
            font=("Helvetica", 13),
            text_color="yellow"
        )

        theme_icon = PhotoImage(file=self.theme_icon_path)
        theme_icon = theme_icon.subsample(10, 10)

        self.theme_button = ctk.CTkButton(
            self,
            image=theme_icon,
            text="",
            command=self.switch_theme,
            width=40,
            height=40,
            fg_color="#4A90E2",
            hover_color="#357ABD"
        )
        self.theme_button.place(x=490, y=600)
        
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

        note_font = self.font
        note_font_size = self.font_size

        note_tag = self.tag_combobox.get()

        note_password = self.password

        if note_title.strip() == "":
            self.result_label.configure(text="Title is required!", text_color="red")
            return

        notes_directory = "notes/"
        if not os.path.exists(notes_directory):
            os.makedirs(notes_directory)

        note_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        note_data = f"Title: {note_title}\nDate: {note_date}\nFont: {note_font}\nFont Size: {note_font_size}\nPassword: {note_password}\nTag: {note_tag}\n\n{note_content}"

        with open(os.path.join(notes_directory, note_title + ".txt"), "w") as file:
            file.write(note_data)

        self.result_label.configure(text="Note Saved!", text_color="#03c000")
        
        self.password = ""
        #self.tag_combobox = "None"
        self.tag_combobox.set("None")

        self.title_note_entry.delete(0, END)
        self.note_entry.delete("1.0", END)

        self.after(1000, self.clear_message)

    def set_password_window(self):
        self.password_window = ctk.CTkToplevel(self)
        self.password_window.title("Set Password")
        self.password_window.geometry("250x250")

        self.password_window.grid_columnconfigure(0, weight=1)
        self.password_window.grid_columnconfigure(2, weight=1)

        set_password_label = ctk.CTkLabel(
            self.password_window,
            text="Password"
        )
        set_password_label.grid(row=0, column=1, padx=10, pady=10)

        self.set_password_entry = ctk.CTkEntry(
            self.password_window,
            placeholder_text="...",
            width=200,
            height=30,
            border_width=1,
            corner_radius=10
        )
        self.set_password_entry.grid(row=1, column=1, padx=10, pady=10)

        self.set_password_result_label = ctk.CTkLabel(
            self.password_window,
            text="",
            font=("Helvetica", 14)
        )
        self.set_password_result_label.grid(row=2, column=1, padx=10, pady=10)

        self.set_password_confirm_button = ctk.CTkButton(
            self.password_window,
            text="Confirm",
            command=self.set_password,
        )
        self.set_password_confirm_button.grid(row=3, column=1, padx=10, pady=10)

    def set_password(self):
        note_password_control = self.set_password_entry.get()

        if note_password_control == "":
            self.set_password_result_label.configure(text="Password cannot be empty!", text_color="red")
            self.set_password_result_label.after(3000, self.password_clear_message)     

        else:
            self.password = note_password_control
            self.set_password_result_label.configure(text="Password saved!", text_color="green")
            self.set_password_result_label.after(3000, self.password_window.destroy)

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
        self.font_comboBox.set(self.font)
        self.font_comboBox.grid(row=0, column=1, padx=10, pady=10)

        fontsize_label = ctk.CTkLabel(
            window,
            text="Size: "
        )
        fontsize_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.fontsize_comboBox = ctk.CTkComboBox(
            window,
            values=["10", "12", "14", "16", "18", "20", "22", "24", "26", "28", "30", "32", "34", "36", "38", "40"],
        )
        self.fontsize_comboBox.set(self.font_size)
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
            command=lambda: self.apply_font(),
            fg_color="#0bb200",
            hover_color="#099200"
        )
        save_font_changes_button.grid(row=3, column=1, padx=10, pady=10)

    def apply_font(self):
        self.font = self.font_comboBox.get()
        self.font_size = int(self.fontsize_comboBox.get())

        self.note_entry.configure(font=(self.font, self.font_size))

        self.font_result_label.configure(text="Font Saved!", text_color="green")
        self.after(2000, self.font_clear_message)    
        
    def list_manage_notes(self, window=None):
        notes_directory = "notes"
        files = os.listdir(notes_directory)
        
        notes = []
        
        for file_name in files:
            file_path = os.path.join(notes_directory, file_name)
            with open(file_path, "r") as file:
                lines = file.readlines()
                if len(lines) > 1:
                    note_title = lines[0].replace("Title: ", "").strip()
                    note_date = lines[1].replace("Date: ", "").strip()
                    note_tag = lines[5].replace("Tag: ", "").strip()
                else:
                    note_title = file_name.strip(".txt")
                    note_date = "Unknown"
                    note_tag = ""
            
            notes.append((file_name, note_title, note_date, note_tag))

        notes.sort(key=lambda x: x[2] if x[2] != "Unknown" else "9999-12-31")
        
        if window is None:
            window = ctk.CTkToplevel(self)
            window.title("Note List")
            window.geometry("500x300")
        
        self.window = window

        notes_scrollable_frame = ctk.CTkScrollableFrame(window, width=460, height=260)
        notes_scrollable_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        note_number_header = ctk.CTkLabel(notes_scrollable_frame, text="No", font=("Helvetica", 12, "bold"))
        note_number_header.grid(row=0, column=0, padx=10, pady=5)

        note_title_header = ctk.CTkLabel(notes_scrollable_frame, text="Title", font=("Helvetica", 12, "bold"))
        note_title_header.grid(row=0, column=1, padx=10, pady=5)

        note_date_header = ctk.CTkLabel(notes_scrollable_frame, text="Date", font=("Helvetica", 12, "bold"))
        note_date_header.grid(row=0, column=2, padx=10, pady=5)

        note_tag_header = ctk.CTkLabel(notes_scrollable_frame, text="Tag", font=("Helvetica", 12, "bold"))
        note_tag_header.grid(row=0, column=3, padx=10, pady=5)

        for i, (file_name, note_title, note_date, note_tag) in enumerate(notes, start=1):
            note_number_label = ctk.CTkLabel(notes_scrollable_frame, text=str(i) + ":")
            note_number_label.grid(row=i, column=0, padx=10, pady=5, sticky="w")

            note_title_label = ctk.CTkLabel(notes_scrollable_frame, text=note_title)
            note_title_label.grid(row=i, column=1, padx=10, pady=5)

            note_date_label = ctk.CTkLabel(notes_scrollable_frame, text=note_date)
            note_date_label.grid(row=i, column=2, padx=10, pady=5)

            note_tag_label = ctk.CTkLabel(notes_scrollable_frame, text=note_tag)
            note_tag_label.grid(row=i, column=3, padx=10, pady=5)

            edit_icon = PhotoImage(file=self.edit_icon_path)
            edit_icon = edit_icon.subsample(25, 25)

            edit_button = ctk.CTkButton(
                notes_scrollable_frame,
                image=edit_icon,
                text="",
                command=lambda file_name=file_name: self.edit_note(file_name),
                fg_color="#0bb200",
                hover_color="#099200",
                width=30
            )
            edit_button.grid(row=i, column=4, padx=10, pady=5)

            delete_icon = PhotoImage(file=self.delete_icon_path)
            delete_icon = delete_icon.subsample(25, 25)

            delete_button = ctk.CTkButton(
                notes_scrollable_frame,
                image=delete_icon,
                text="",
                command=lambda file_name=file_name: self.delete_note(file_name, window), 
                fg_color="#b20000",
                hover_color="#960000",
                width=30
            )
            delete_button.grid(row=i, column=5, padx=10, pady=5)

    def edit_note(self, file_name):
        notes_directory = "notes/"
        file_path = os.path.join(notes_directory, file_name)

        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                lines = file.readlines()
                if len(lines) > 1:
                    note_font = lines[2].replace("Font: ", "").strip()
                    note_font_size = lines[3].replace("Font Size: ", "").strip()
                    note_password = lines[4].replace("Password: ", "").strip()
                    note_tag = lines[5].replace("Tag: ", "").strip()

                    self.font = note_font
                    self.font_size = note_font_size

                    self.password = note_password

                    if self.password != "":  # If password exists
                        self.password_control_window = ctk.CTkToplevel(self)
                        self.password_control_window.title("Password")
                        self.password_control_window.geometry("250x250")

                        set_password_control_label = ctk.CTkLabel(
                            self.password_control_window,
                            text="Password"
                        )
                        set_password_control_label.grid(row=0, column=1, padx=10, pady=10)

                        self.set_password_control_entry = ctk.CTkEntry(
                            self.password_control_window,
                            placeholder_text="...",
                            width=200,
                            height=30,
                            border_width=1,
                            corner_radius=10
                        )
                        self.set_password_control_entry.grid(row=1, column=1, padx=10, pady=10)

                        self.set_password_control_result_label = ctk.CTkLabel(
                            self.password_control_window,
                            text="",
                            font=("Helvetica", 14)
                        )
                        self.set_password_control_result_label.grid(row=2, column=1, padx=10, pady=10)

                        self.set_password_control_confirm_button = ctk.CTkButton(
                            self.password_control_window,
                            text="Confirm",
                            command=lambda: self.password_control(note_font, note_font_size, note_tag, lines, file_name)
                        )
                        self.set_password_control_confirm_button.grid(row=3, column=1, padx=10, pady=10)
                    else: # If password doesn't exist
                        self.load_note_content(note_font, note_font_size, note_tag, lines, file_name)

    def password_control(self, note_font, note_font_size, note_tag, lines, file_name):
        if self.set_password_control_entry.get() == self.password:
            self.set_password_control_result_label.configure(text="Password correct!", text_color="green")
            self.access_note = True
            self.password_control_window.after(2000, self.password_control_window.destroy)

            self.load_note_content(note_font, note_font_size, note_tag, lines, file_name)
        else:
            self.set_password_control_result_label.configure(text="Try Again!", text_color="red")
            self.access_note = False
            self.set_password_control_entry.delete(0, END)

    def load_note_content(self, note_font, note_font_size, note_tag, lines, file_name):
        self.tag_combobox.set(note_tag)
        self.note_entry.configure(font=(note_font, int(note_font_size)))

        note_title = lines[0].replace("Title: ", "").strip()
        note_content = "".join(lines[7:])

        self.title_note_entry.delete(0, END)
        self.title_note_entry.insert(0, note_title)

        self.note_entry.delete("1.0", END)
        self.note_entry.insert("1.0", note_content)

        self.save_note_button.configure(
            text="Update Note",
            command=lambda: self.update_existing_note(file_name)
        )

        self.set_password_button.configure(
            text="Change Password",
            command=self.set_password_window
        )

        self.warning_label.place(x=50, y=620)
        self.warning_label.after(4000, self.warning_clear_message)

        self.result_label.configure(text="Note Loaded", text_color="yellow")

    def update_existing_note(self, file_name):
        note_content = self.note_entry.get("1.0", "end-1c")
        note_title = self.title_note_entry.get()

        note_tag = self.tag_combobox.get()
        #note_tag = self.tag_combobox
        
        note_password = self.password

        if note_title.strip() == "":
            self.result_label.configure(text="Title is required!", text_color="red")
            return
        
        notes_directory = "notes/"
        file_path = os.path.join(notes_directory, file_name)

        note_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        note_data = f"Title: {note_title}\nDate: {note_date}\nFont: {self.font}\nFont Size: {self.font_size}\nPassword: {note_password}\nTag: {note_tag}\n\n{note_content}"

        with open(file_path, "w") as file:
            file.write(note_data)

        self.result_label.configure(text="Note Updated!", text_color="green")

        self.access_note = False

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

    def warning_clear_message(self):
        self.warning_label.configure(text="")

    def font_clear_message(self):
        self.font_result_label.configure(text="")

    def password_clear_message(self):
        self.set_password_result_label.configure(text="")

    def clear_screen(self):
        self.access_note = False

        self.title_note_entry.delete(0, END)
        self.note_entry.delete("1.0", END)

        for widget in self.winfo_children():
            widget.destroy()

        self.widgets()

if __name__ == "__main__":
    app = NoteTakingApp()
    app.mainloop()
