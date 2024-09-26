from tkinter import *
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

        self.widgets()

    def switch_theme(self):

        if self.current_theme == "dark":
            ctk.set_appearance_mode("light")
            self.current_theme = "light"
        else:
            ctk.set_appearance_mode("dark")
            self.current_theme = "dark"

    def widgets(self):
        self.header_homepage = ctk.CTkLabel(
            self,
            text="To Do App",
            font=("Helvetica", 40)
        )
        self.header_homepage.pack(pady=50)


        theme_icon = PhotoImage(file=self.theme_icon_path)
        theme_icon = theme_icon.subsample(7, 7)

        self.theme_button = ctk.CTkButton(
            self,
            image=theme_icon,
            text="",
            command=self.switch_theme,
            width=40,
            height=40
        )
        self.theme_button.place(x=50, y=40)


        self.add_entry = ctk.CTkEntry(
            self,
            placeholder_text="Add a Task",
            width=200,
            height=30,
            border_width=1,
            corner_radius=10
            )
        self.add_entry.pack(pady=20)

if __name__ == "__main__":
    app = ToDoApp()
    app.mainloop()

# def edit(selection):
#     edit = input("Enter the task...\n")
#     task[selection-1] = edit

# def remove(selection):
#     task.remove(task[selection-1])

# def error_selection(selection):
#     while True:
#         try:    
#             selection = int(input("Enter a number: "))
#             break
#         except ValueError:
#             print("Invalid entry. Please enter a number")
#     return selection

# def display(task):
#     print("\nYour Tasks")
    
#     if len(task) == 0:
#         print("You don't have any task!\n")    
#     else:
#         print("---------------------------------")
#         i = 0
#         while i < len(task):
#             print(" * " + str(task[i]))
#             i = i + 1
#         print("---------------------------------")

# menu_inside_select = 0
# task = []
# i = 0
# usage_index = 0

# print("TO DO APP\n")

# time.sleep(1)

# print("Loading...\n")

# time.sleep(2)

# try:
#     with open("todoapp.txt", "x"):
#         pass
# except FileExistsError:
#     print("...\n")

# with open("todoapp.txt","r") as file:
#     task = file.readlines()

# while menu_inside_select != 4:
        
#     os.system('cls')
        
#     display(task)
        
#     time.sleep(1)
        
#     print("(1) Add new task")
#     print("(2) Edit task")
#     print("(3) Remove task")
#     print("(4) Quit")
    
#     menu_inside_select = error_selection(menu_inside_select)
    
#     if menu_inside_select == 1:
#         add = input("Enter the task: ")
#         task.append(add)
        
#     elif menu_inside_select == 2:
        
#         if len(task) == 0:
#             print("You don't have any task!")
#             break
        
#         print("Select the task you want to edit")
        
#         while True:
            
#             menu_inside_select = error_selection(menu_inside_select)
            
#             if menu_inside_select <= len(task):
#                 edit(menu_inside_select)
#                 break
#             else:
#                 print("Try again")
        
#     elif menu_inside_select == 3:
        
#         if len(task) == 0:
#             print("You don't have any task!")
#             break
        
#         print("Select the task you want to delete")
    
#         while True:                
#             menu_inside_select = error_selection(menu_inside_select)
            
#             if menu_inside_select <= len(task):
#                 remove(menu_inside_select)
#                 break
#             else:
#                 print("Try again")
        
#     elif menu_inside_select == 4:
        
#         print("See you later!!!")
#         time.sleep(2)
        
#         with open("todoapp.txt","w") as file:
#             i = 0
#             while i < len(task):
#                 file.write(task[i].rstrip() + "\n")
#                 i = i + 1
        
#         sys.exit()
    
#     else:
#         print("Try again")