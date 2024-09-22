from tkinter import *
import customtkinter
from datetime import datetime
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.dates import DateFormatter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

root.title("Tkinter - BMI Calculator")
root.geometry("600x800")

current_theme = "dark"

def switch_theme():
    global current_theme

    if current_theme == "dark":
        customtkinter.set_appearance_mode("light")
        current_theme = "light"
    else:
        customtkinter.set_appearance_mode("dark")
        current_theme = "dark"

def focus_next_entry(event, next_entry):
    next_entry.focus()

def show_previous_data():
    global header

    for widget in root.winfo_children():
        if header_homepage != widget:
            widget.pack_forget()
            widget.place_forget()
        
    homepage_icon = PhotoImage(file="icons/homepage_icon.png")
    homepage_icon = homepage_icon.subsample(9, 9)

    homepage_button = customtkinter.CTkButton(master=root, image=homepage_icon, text="", command=show_homepage, width=40, height=40)
    homepage_button.place(x=500, y=40)

    try:
        df = read_data_to_dataframe()

        if not df.empty:
            records_frame = customtkinter.CTkFrame(master=root)
            records_frame.pack(pady=10, fill="x")

            for i, row in enumerate(df.itertuples(), start=1):
                height = row[1]
                weight = row[2]
                date_str = row[3].strftime('%d/%m/%Y')

                formatted_line = f"{height} cm - {weight} kg - {date_str}"

                record_label = customtkinter.CTkLabel(master=records_frame, text=formatted_line, font=("Helvetica", 20))
                record_label.grid(row=i, column=0, padx=10, pady=5, sticky='w')

                delete_button = customtkinter.CTkButton(master=records_frame, text="Delete", command=lambda idx=i: delete_record(idx), fg_color="red", width=30)
                delete_button.grid(row=i, column=1, padx=10, pady=5)

            graph_frame = customtkinter.CTkFrame(master=root)
            graph_frame.pack(pady=20, fill="both", expand=True)

            plot_weight_over_time(df, graph_frame)

        else:
            header = customtkinter.CTkLabel(master=root, text="No Data Available", font=("Helvetica", 25), text_color="red")
            header.pack(pady=10)

    except FileNotFoundError:
        header = customtkinter.CTkLabel(master=root, text="No Data Available", font=("Helvetica", 25), text_color="red")
        header.pack(pady=10)

def delete_record(record_index):
    try:
        with open("bmi_data.txt", "r") as file:
            lines = file.readlines()

        if 0 < record_index < len(lines):
            del lines[record_index]

            with open("bmi_data.txt", "w") as file:
                file.writelines(lines)
            
        show_previous_data()

    except FileNotFoundError:
        header.configure(text="No Data Available", text_color="red")

def show_homepage():
    global header_homepage

    for widget in root.winfo_children():
        if header_homepage != widget:
            widget.pack_forget()
            widget.place_forget()

    theme_button.place(x=50, y=40)
    records_button.place(x=500, y=40)

    h_entry.pack(pady=20)
    w_entry.pack(pady=20)
    button_1.pack(pady=20)
    button_2.pack(pady=20)
    results.pack(pady=50)
    button_3.pack(pady=20)

def clear_screen():
    h_entry.delete(0, END)
    w_entry.delete(0, END)
    results.configure(text="")
    h_entry.focus()

    save_button.pack_forget()

def get_bmi():
    if validate_input():
        if int(h_entry.get()) <= 0:
            results.configure(text="Please enter valid height!", text_color="red")
            return

        if int(w_entry.get()) <= 0:
            results.configure(text="Please enter valid weight!", text_color="red")
            return

        our_height = int(h_entry.get())/100 * int(h_entry.get())/100
        our_weight = int(w_entry.get())

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

        save_button.pack(pady=20)
    
def validate_input():
    try:
        height = float(h_entry.get())
        weight = float(w_entry.get())
        return True
    except ValueError:
        results.configure(text="Please enter valid numbers.", text_color="red")
        save_button.pack_forget()
        return False
    
def save_data():
    now = datetime.now()
    day = now.day
    month = now.month
    year = now.year

    file_exists = os.path.isfile("bmi_data.txt")

    with open("bmi_data.txt", "a") as file:
        if not file_exists:
            file.write("Height, Weight, Day, Month, Year\n")

        file.write(f"{h_entry.get()}, {w_entry.get()}, {day}, {month}, {year}\n")

    results.configure(text="Data saved.", text_color="green")
    
    save_button.pack_forget()
    
def read_data_to_dataframe():
    try:
        with open("bmi_data.txt", "r") as file:
            lines = file.readlines()

        data = []
        for line in lines[1:]:
            line = line.strip()
            height, weight, day, month, year = line.split(", ")
            date_str = f"{day}/{month}/{year}"
            data.append([int(height), int(weight), date_str])

        df = pd.DataFrame(data, columns=["Height (cm)", "Weight (kg)", "Date"])
        df['Date'] = pd.to_datetime(df['Date'], format="%d/%m/%Y")
        return df

    except FileNotFoundError:
        print("File not found!")
        return pd.DataFrame()

def plot_weight_over_time(df, parent_frame):
    df["Date"] = pd.to_datetime(df["Date"])

    fig, ax = plt.subplots(figsize=(5, 5))
    ax.plot(df['Date'], df['Weight (kg)'], marker='o', linestyle='-', color='blue')

    date_format = DateFormatter("%m-%d")
    ax.xaxis.set_major_formatter(date_format)

    plt.xticks(rotation=45)

    ax.set_xlabel("Date")
    ax.set_ylabel("Weight (kg)")
    ax.set_title("Weight Change Over Time")
    ax.grid(True)

    canvas = FigureCanvasTkAgg(fig, master=parent_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=10)

# Switch Theme
theme_icon = PhotoImage(file="icons/theme_icon.png")
theme_icon = theme_icon.subsample(7, 7)

theme_button = customtkinter.CTkButton(master=root, 
    image=theme_icon, 
    text="",
    command=switch_theme, 
    width=40, 
    height=40)
theme_button.place(x=50, y=40)

# Records
records_icon = PhotoImage(file="icons/history.png")
records_icon = records_icon.subsample(9, 9)

records_button = customtkinter.CTkButton(master=root, 
    image=records_icon, 
    text="", 
    command=show_previous_data, 
    width=40, 
    height=40)
records_button.place(x=500, y=40)

# Header
header_homepage = customtkinter.CTkLabel(master=root,
    text="BMI Calculator",
    font=("Helvetica", 40))
header_homepage.pack(pady=50)

# Entry Boxes
h_entry = customtkinter.CTkEntry(master=root, 
    placeholder_text="Height (cm)", 
    width=200, 
    height=30, 
    border_width=1,
    corner_radius=10)
h_entry.pack(pady=20)
h_entry.bind("<Return>", lambda event: focus_next_entry(event, w_entry))

w_entry = customtkinter.CTkEntry(master=root, 
    placeholder_text="Weight (kg)", 
    width=200, 
    height=30, 
    border_width=1,
    corner_radius=10)
w_entry.pack(pady=20)
w_entry.bind("<Return>", lambda event: button_1.invoke())

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

save_button = customtkinter.CTkButton(master=root,
    text="Save Data",
    width=190,
    height=40,
    command=save_data)
save_button.pack_forget()

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
button_3.pack(side=BOTTOM, pady=20)

root.mainloop()