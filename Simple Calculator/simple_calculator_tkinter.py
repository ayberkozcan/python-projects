import tkinter as tk
from tkinter import messagebox

def collect(x, y):
    return x + y

def ext(x, y):
    return x - y

def imp(x, y):
    return x * y

def div(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero is not allowed.")
        return None

def calculate():
    try:
        no1 = int(entry1.get())
        no2 = int(entry2.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")
        return
    
    operation = operation_var.get()
    if operation == "Addition":
        result = collect(no1, no2)
    elif operation == "Subtraction":
        result = ext(no1, no2)
    elif operation == "Multiplication":
        result = imp(no1, no2)
    elif operation == "Division":
        result = div(no1, no2)
    
    if result is not None:
        result_label.config(text=f"Result: {result}")

root = tk.Tk()
root.title("Simple Calculator")

label1 = tk.Label(root, text="Enter the first number:")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Enter the second number:")
label2.pack()

entry2 = tk.Entry(root)
entry2.pack()

operation_var = tk.StringVar(value="Addition")
operation_menu = tk.OptionMenu(root, operation_var, "Addition", "Subtraction", "Multiplication", "Division")
operation_menu.pack()


# Buttons

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

result_label = tk.Label(root, text="Result: ")
result_label.pack()

quit_button = tk.Button(root, text="Quit", command=root.quit)
quit_button.pack()

root.mainloop()
