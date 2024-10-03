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

        theme_button = ctk.CTkButton(
            self,
            image=theme_icon,
            text="",
            command=self.switch_theme,
            width=40,
            height=40
        )
        theme_button.place(x=500, y=500)
        
        note_entry = ctk.CTkTextbox(
            self,
            width=500,
            height=200,
            border_width=1,
            corner_radius=10
        )
        note_entry.pack(pady=20)
        
    def switch_theme(self):
        if self.current_theme == "dark":
            ctk.set_appearance_mode("light")
            self.current_theme = "light"
        else:
            ctk.set_appearance_mode("dark")
            self.current_theme = "dark"

if __name__ == "__main__":
    app = NoteTakingApp()
    app.mainloop()
