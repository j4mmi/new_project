import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.resizable(False, False)

        self.expression = ""
        self.display_var = tk.StringVar(value="0")

        display = tk.Entry(
            self, textvariable=self.display_var, font=("Segoe UI", 24),
            justify="right", bd=0, bg="#f5f5f5", state="readonly",
            readonlybackground="#f5f5f5", relief="flat"
        )
        display.grid(row=0, column=0, columnspan=4, sticky="nsew", ipady=20, padx=8, pady=(8, 4))

        buttons = [
            ("C", 1, 0), ("(", 1, 1), (")", 1, 2), ("/", 1, 3),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
            ("0", 5, 0), (".", 5, 1), ("⌫", 5, 2), ("=", 5, 3),
        ]

        for (text, row, col) in buttons:
            style = self._button_style(text)
            btn = tk.Button(
                self, text=text, font=("Segoe UI", 16), bd=0,
                command=lambda t=text: self.on_button(t), **style
            )
            btn.grid(row=row, column=col, sticky="nsew", padx=4, pady=4, ipady=10)

        for i in range(6):
            self.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)

        self.bind("<Key>", self.on_key)

    def _button_style(self, text):
        if text == "=":
            return {"bg": "#ff9500", "fg": "white", "activebackground": "#ffb143"}
        if text in ("C", "⌫"):
            return {"bg": "#d4d4d2", "fg": "black", "activebackground": "#e0e0e0"}
        if text in ("/", "*", "-", "+", "(", ")"):
            return {"bg": "#e6e6e6", "fg": "#ff9500", "activebackground": "#f0f0f0"}
        return {"bg": "#ffffff", "fg": "black", "activebackground": "#f0f0f0"}

    def on_button(self, text):
        if text == "C":
            self.expression = ""
        elif text == "⌫":
            self.expression = self.expression[:-1]
        elif text == "=":
            self.evaluate()
            return
        else:
            self.expression += text

        self.display_var.set(self.expression if self.expression else "0")

    def evaluate(self):
        allowed = set("0123456789+-*/(). ")
        if not self.expression or any(ch not in allowed for ch in self.expression):
            self.display_var.set("Error")
            self.expression = ""
            return
        try:
            result = eval(self.expression, {"__builtins__": {}}, {})
            self.expression = str(result)
            self.display_var.set(self.expression)
        except (SyntaxError, ZeroDivisionError, ValueError):
            self.display_var.set("Error")
            self.expression = ""

    def on_key(self, event):
        char = event.char
        if char in "0123456789+-*/().":
            self.expression += char
            self.display_var.set(self.expression)
        elif event.keysym == "Return":
            self.evaluate()
        elif event.keysym == "BackSpace":
            self.expression = self.expression[:-1]
            self.display_var.set(self.expression if self.expression else "0")
        elif event.keysym == "Escape":
            self.expression = ""
            self.display_var.set("0")


if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
