import tkinter as tk
from tkinter import ttk

EMOTIONS = ["Happy", "Sad", "Angry", "Anxious", "Excited", "Tired"]


def main():
    root = tk.Tk()
    root.title("Mood Reader")
    root.geometry("350x180")
    root.resizable(False, False)

    prompt = tk.Label(root, text="How do you feel today?", font=("Segoe UI", 12))
    prompt.pack(pady=(20, 10))

    mood_var = tk.StringVar(value=EMOTIONS[0])
    dropdown = ttk.Combobox(root, textvariable=mood_var, values=EMOTIONS, state="readonly")
    dropdown.pack(pady=5)

    def on_ok():
        print(f"Selected mood: {mood_var.get()}")
        root.destroy()

    button_frame = tk.Frame(root)
    button_frame.pack(side="bottom", fill="x", padx=10, pady=10)

    ok_button = tk.Button(button_frame, text="OK", width=8, command=on_ok)
    ok_button.pack(side="right")

    root.mainloop()


if __name__ == "__main__":
    main()
