import tkinter as tk
from tkinter import messagebox


class SimpleInterestCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Interest Calculator")
        self.resizable(False, False)
        self.configure(bg="#f5f5f5")

        self.principal_var = tk.StringVar()
        self.rate_var = tk.StringVar()
        self.time_var = tk.StringVar()
        self.result_var = tk.StringVar(value="")

        self._build_form()

    def _build_form(self):
        title = tk.Label(
            self, text="Simple Interest Calculator", font=("Segoe UI", 16, "bold"),
            bg="#f5f5f5", pady=12
        )
        title.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=16)

        fields = [
            ("Principal (₹)", self.principal_var),
            ("Rate (% per year)", self.rate_var),
            ("Time (years)", self.time_var),
        ]

        for i, (label_text, var) in enumerate(fields, start=1):
            label = tk.Label(self, text=label_text, font=("Segoe UI", 11), bg="#f5f5f5", anchor="w")
            label.grid(row=i, column=0, sticky="w", padx=(16, 8), pady=6)

            entry = tk.Entry(self, textvariable=var, font=("Segoe UI", 11), width=18, relief="solid", bd=1)
            entry.grid(row=i, column=1, sticky="ew", padx=(0, 16), pady=6)

        button_row = len(fields) + 1
        calc_btn = tk.Button(
            self, text="Calculate", font=("Segoe UI", 11, "bold"), bg="#ff9500", fg="white",
            activebackground="#ffb143", bd=0, command=self.calculate
        )
        calc_btn.grid(row=button_row, column=0, sticky="ew", padx=(16, 8), pady=(12, 6), ipady=6)

        clear_btn = tk.Button(
            self, text="Clear", font=("Segoe UI", 11, "bold"), bg="#d4d4d2", fg="black",
            activebackground="#e0e0e0", bd=0, command=self.clear_fields
        )
        clear_btn.grid(row=button_row, column=1, sticky="ew", padx=(0, 16), pady=(12, 6), ipady=6)

        result_label = tk.Label(
            self, textvariable=self.result_var, font=("Segoe UI", 12, "bold"),
            bg="#f5f5f5", fg="#1a7f37", pady=10
        )
        result_label.grid(row=button_row + 1, column=0, columnspan=2, sticky="nsew", padx=16)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def calculate(self):
        try:
            principal = float(self.principal_var.get())
            rate = float(self.rate_var.get())
            time = float(self.time_var.get())
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid numbers for all fields.")
            return

        if principal < 0 or rate < 0 or time < 0:
            messagebox.showerror("Invalid input", "Values cannot be negative.")
            return

        interest = (principal * rate * time) / 100
        total_amount = principal + interest
        self.result_var.set(
            f"Interest: ₹{interest:,.2f}   |   Total Amount: ₹{total_amount:,.2f}"
        )

    def clear_fields(self):
        self.principal_var.set("")
        self.rate_var.set("")
        self.time_var.set("")
        self.result_var.set("")


if __name__ == "__main__":
    app = SimpleInterestCalculator()
    app.mainloop()
