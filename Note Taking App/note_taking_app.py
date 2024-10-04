from tkinter import *
import customtkinter as ctk
import os

class NoteTakingApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_default_color_theme("dark-blue")
    
        self.title("Note Taker")
        self.geometry("600x600")

        self.current_theme = "dark"

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.theme_icon_path = os.path.join(BASE_DIR, "icons/theme_icon.png")

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
        self.theme_button.place(x=500, y=500)
        
        self.note_entry = ctk.CTkTextbox(
            self,
            width=500,
            height=300,
            border_width=1,
            corner_radius=10
        )
        self.note_entry.pack(pady=20)

        save_note_button = ctk.CTkButton(
            self,
            text="Save Note",
            fg_color="#bb0000",
            hover_color="#a70000",
            command=self.save_note,
            width=50,
            height=50
        )
        save_note_button.place(x=50, y=350)

        self.result_label = ctk.CTkLabel(
            self,
            text="",
            font=("Helvetica", 20)
        )
        self.result_label.place(x=250, y=450)
        
    def switch_theme(self):
        if self.current_theme == "dark":
            ctk.set_appearance_mode("light")
            self.current_theme = "light"
        else:
            ctk.set_appearance_mode("dark")
            self.current_theme = "dark"

    def save_note(self):
        note_content = self.note_entry.get("1.0", "end-1c")

        with open("notes.txt", "w") as file:
            file.write(note_content)

        self.result_label.configure(text="Note Saved!", text_color="#03c000")
        
        self.note_entry.delete("1.0", END)

        self.after(1000, self.clear_message)

    def clear_message(self):
        self.result_label.configure(text="")

if __name__ == "__main__":
    app = NoteTakingApp()
    app.mainloop()
