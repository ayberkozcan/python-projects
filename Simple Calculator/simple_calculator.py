import customtkinter as ctk

class CalculatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Calculator")
        self.geometry("800*600")

        self.result = ctk.StringVar()

        self.widgets()

    def widgets(self):
        self.result_entry = ctk.CTkEntry(self, textvariable=self.result, state="readonly", width=200)
        self.result_entry.grid(row=0, column=0, pady=20)

        buttons = [ 
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2),               
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2),   
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2),   
            ("0", 5, 1)          
        ]

        for (text, row, column) in buttons:
            button = ctk.CTkButton(self, text=text, command=lambda t=text: self.append_number(t))
            button.grid(row=row, column=column, padx=10, pady=10)

        operations = [
            ("+", self.collect), ("-", self.ext), ("*", self.imp), ("/", self.div)
        ]

        for (text, command) in operations:
            button = ctk.CTkButton(self, text=text, command=lambda cmd=command: self.set_operation(cmd))
            button.grid(row=operations.index((text, command))+2, column=3, padx=10, pady=10)

        equals_button = ctk.CTkButton(self, text="=", command=self.calculate)
        equals_button.grid(row=5, column=2, padx=10, pady=10)

        clear_button = ctk.CTkButton(self, text="C", command=self.clear)
        clear_button.grid(row=5, column=0, padx=10, pady=10)

    def append_number(self, number):
        current_text = self.result.get()
        self.result.set(current_text + number)

    def set_operation(self, operation):
        self.first_number = int(self.result.get())
        self.result.set("")
        self.operation = operation

    def collect(self, x, y):
        return x + y

    def ext(self, x, y):
        return x - y

    def imp(self, x, y):
        return x * y

    def div(self, x, y):
        if y == 0:
            return "Division by zero is not allowed."
        return x / y

    def calculate(self):
        second_number = int(self.result.get())
        result = self.operation(self.first_number, second_number)
        
        if isinstance(result, str):
            self.result.set(result)
        else:
            self.result.set(result)

    def clear(self):
        self.result.set("")

if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()