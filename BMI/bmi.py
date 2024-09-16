from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

root.title("Tkinter - BMI Calculator")
root.geometry("600x750")

current_theme = "dark"

def switch_theme():
    global current_theme
    if current_theme == "dark":
        customtkinter.set_appearance_mode("light")
        current_theme = "light"
    else:
        customtkinter.set_appearance_mode("dark")
        current_theme = "dark"

def clear_screen():
    h_entry.delete(0, END)
    w_entry.delete(0, END)
    results.configure(text="")
    h_entry.focus()

def get_bmi():
    if validate_input():
        our_height = int(h_entry.get())/100 * int(h_entry.get())/100
        our_weight = int(w_entry.get())

        if our_weight == 0:
            results.configure(text="Weight cannot be 0!", text_color="red")
            return

        bmi = our_weight / our_height
        bmi_rounded = round(bmi, 1)
        
        results.configure(text=f"{str(bmi_rounded)}")

        if bmi_rounded > 0 and bmi_rounded < 18.5:
            results.configure(text=f"{str(bmi_rounded)}\nUnderweight", text_color="lightblue")
        elif bmi_rounded >= 18.5 and bmi_rounded <= 24.9:
            results.configure(text=f"{str(bmi_rounded)}\nNormal", text_color="lightgreen")
        elif bmi_rounded >= 25.0 and bmi_rounded <= 29.9:
            results.configure(text=f"{str(bmi_rounded)}\nOverweight", text_color="#FFD700")
        elif bmi_rounded >= 30.0 and bmi_rounded <= 34.9:
            results.configure(text=f"{str(bmi_rounded)}\nObese", text_color="orange")
        elif bmi_rounded >= 35.0:
            results.configure(text=f"{str(bmi_rounded)}\nExtreme Obese", text_color="red")
        else:
            results.configure(text="Please enter valid numbers.", text_color="red")
    
def validate_input():
    try:
        height = float(h_entry.get())
        weight = float(w_entry.get())
        return True
    except ValueError:
        results.configure(text="Please enter valid numbers.", text_color="red")
        return False

# Switch Theme
theme_icon = PhotoImage(file="theme_icon.png")
theme_icon = theme_icon.subsample(7, 7)

theme_button = customtkinter.CTkButton(master=root, image=theme_icon, text="", command=switch_theme, width=40, height=40)
theme_button.place(x=500, y=40)

# Header
header = customtkinter.CTkLabel(master=root,
    text="BMI Calculator",
    font=("Helvetica", 40),)
header.pack(pady=50)

# Entry Boxes
h_entry = customtkinter.CTkEntry(master=root, 
    placeholder_text="Height (cm)", 
    width=200, 
    height=30, 
    border_width=1,
    corner_radius=10)
h_entry.pack(pady=20)

w_entry = customtkinter.CTkEntry(master=root, 
    placeholder_text="Weight (kg)", 
    width=200, 
    height=30, 
    border_width=1,
    corner_radius=10)
w_entry.pack(pady=20)

# Buttons
button_1 = customtkinter.CTkButton(master=root,
    text="Calculate",
    width=190,
    height=40,
    compound="top",
    command=get_bmi)
button_1.pack(pady=20)

button_2 = customtkinter.CTkButton(master=root,
    text="Clear Screen",
    width=190,
    height=40,
    fg_color="#D35B58",
    hover_color="#C77C78",
    command=clear_screen)
button_2.pack(pady=20)

# Results
results = customtkinter.CTkLabel(master=root,
    text="",
    font=("Helvetica", 28))
results.pack(pady=50)

# Exit Button
button_3 = customtkinter.CTkButton(master=root,
    text="Exit",
    width=190,
    height=40,
    compound="top",
    command=root.destroy)
button_3.pack(pady=20)

root.mainloop()