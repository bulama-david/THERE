import tkinter as tk
import random
import string

class PasswordGenerator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Password Generator")
        self.geometry("400x400")

        self.create_widgets()

    def create_widgets(self):
        # Label for the password length
        label = tk.Label(self, text="Password Length:", font=("Arial", 18))
        label.grid(row=0, column=0)

        # Entry for the password length
        self.length_var = tk.IntVar()
        entry = tk.Entry(self, textvariable=self.length_var, font=("Arial", 18), width=5)
        entry.grid(row=0, column=1)

        # Button to generate the password
        button = tk.Button(self, text="Generate", font=("Arial", 18), width=10, height=2, command=self.generate_password)
        button.grid(row=0, column=2)

        # Label to display the generated password
        self.password_var = tk.StringVar()
        password_label = tk.Label(self, textvariable=self.password_var, font=("Arial", 18))
        password_label.grid(row=1, column=0, columnspan=3)

    def generate_password(self):
        length = self.length_var.get()
        if length < 1:
            self.password_var.set("Error: Length must be at least 1")
        else:
            password = "".join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
            self.password_var.set(password)

if __name__ == "__main__":
    app = PasswordGenerator()
    app.mainloop()