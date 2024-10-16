import customtkinter as ctk

class CalculatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_default_color_theme("dark-blue")

        self.title("Calculator")
        self.control = 0
        self.numbers = [0, 0]
        self.result = ctk.StringVar()
        self.equal_control = 0  # Eşittir için kontrol mekanizması

        self.widgets()

    def widgets(self):
        self.result_entry = ctk.CTkEntry(
            self,
            textvariable=self.result,
            state="readonly",
            height=100,
            width=450,
            font=("Helvetica", 30))
        self.result_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        buttons = [
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2),
            ("0", 5, 1)
        ]

        for (text, row, column) in buttons:
            button = ctk.CTkButton(
                self,
                text=text,
                command=lambda t=text: self.append_number(t),
                fg_color="#4A90E2",
                hover_color="#6EB5FF",
                height=70,
                width=100,
                font=("Helvetica", 20))
            button.grid(row=row, column=column, padx=10, pady=10)

        operations = [
            ("+", self.collect), ("-", self.ext), ("*", self.imp), ("/", self.div)
        ]

        for (text, command) in operations:
            button = ctk.CTkButton(
                self,
                text=text,
                command=lambda cmd=command: self.set_operation(cmd),
                height=70,
                width=100,
                font=("Helvetica", 20))
            button.grid(row=operations.index((text, command))+2, column=3, padx=5, pady=5)

        equals_button = ctk.CTkButton(
            self,
            text="=",
            command=self.calculate,
            height=70,
            width=100,
            font=("Helvetica", 20))
        equals_button.grid(row=5, column=2, padx=5, pady=5)

        clear_button = ctk.CTkButton(
            self,
            text="C",
            command=self.clear,
            height=70,
            width=100,
            font=("Helvetica", 20))
        clear_button.grid(row=5, column=0, padx=5, pady=5)

        self.bind_keys()

    def on_key_press(self, event):
        key = event.char
        if key.isdigit():
            self.append_number(key)
        elif key == "+":
            self.set_operation(self.collect)
        elif key == "-":
            self.set_operation(self.ext)
        elif key == "*":
            self.set_operation(self.imp)
        elif key == "/":
            self.set_operation(self.div)
        elif key == "=" or key == "\r":
            self.calculate()
        elif key.lower() == "c":
            self.clear()

    def bind_keys(self):
        self.bind("<Key>", self.on_key_press)

    def append_number(self, number):
        current_text = self.result.get()
        self.result.set(current_text + number)

    def set_operation(self, operation):
        if self.result.get() != "":
            if self.control == 0:
                self.numbers[0] = int(self.result.get())
            else:
                self.numbers[1] = int(self.result.get())
            self.result.set("")

        self.operation = operation
        self.control = 1
        self.equal_control = 0

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
        if self.result.get() != "":
            if self.equal_control == 0:
                self.numbers[1] = int(self.result.get())

        result = self.operation(self.numbers[0], self.numbers[1])

        if isinstance(result, str):
            self.result.set(result)
        else:
            self.result.set(result)
            self.numbers[0] = result

        self.equal_control = 1

    def clear(self):
        self.numbers = [0, 0]
        self.control = 0
        self.equal_control = 0
        self.result.set("")


if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()
