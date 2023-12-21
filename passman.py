import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import os

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Manager")

        # Configure style
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#AED6F1')  # Light blue
        self.style.configure('TButton', background='#3498DB', foreground='#000000', relief=tk.FLAT)  # Blue button with black text
        self.style.map('TButton', background=[('pressed', '#2980B9')])  # Darker blue when pressed
        self.style.configure('TLabel', background='#AED6F1', font=('Arial', 11), foreground='#000000')  # Black text
        self.style.configure('Header.TLabel', font=('Arial', 18, 'bold'), foreground='#000000')  # Black text

        # Create and place GUI components
        self.header_label = ttk.Label(root, text="Password Manager", style='Header.TLabel')
        self.header_label.grid(row=0, column=0, columnspan=2, pady=(10, 20))

        self.place_label = ttk.Label(root, text="Place/Service:")
        self.place_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)

        self.place_var = tk.StringVar()
        self.place_entry = ttk.Entry(root, textvariable=self.place_var)
        self.place_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        self.length_label = ttk.Label(root, text="Password Length:")
        self.length_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)

        self.length_var = tk.StringVar(value=12)
        self.length_entry = ttk.Entry(root, textvariable=self.length_var)
        self.length_entry.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

        self.generate_button = ttk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.result_label = ttk.Label(root, text="")
        self.result_label.grid(row=4, column=0, columnspan=2, pady=10)

        self.copy_button = ttk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.grid(row=5, column=0, pady=10, sticky=tk.W + tk.E)

        self.save_button = ttk.Button(root, text="Save Password", command=self.save_password)
        self.save_button.grid(row=5, column=1, pady=10, sticky=tk.W + tk.E)

    def generate_password(self):
        length = int(self.length_var.get())
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        self.result_label.config(text=f"Generated Password: {password}")
        self.generated_password = password

    def copy_to_clipboard(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.generated_password)
        self.root.update()  # required for clipboard changes to take effect
        print("Password copied to clipboard!")

        # Show a message box indicating that the password has been copied
        copied_message = f"Password copied to clipboard:\n{self.generated_password}"
        messagebox.showinfo("Copied to Clipboard", copied_message)

    def save_password(self):
        place = self.place_var.get()
        password = self.generated_password

        try:
            with open("passwords.txt", "a") as file:
                file.write(f"Place/Service: {place}\n")
                file.write(f"Password: {password}\n")
                file.write("-" * 30 + "\n")

            file_location = os.path.abspath("passwords.txt")
            print("Password saved successfully to:", file_location)

            # Show a message box indicating that the password has been saved
            saved_message = f"Password saved successfully!\nFile location: {file_location}"
            messagebox.showinfo("Saved Password", saved_message)
        except Exception as e:
            print(f"Error saving password: {e}")
            messagebox.showerror("Error", f"Error saving password: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.configure(bg='#AED6F1')  # Set background color for the entire window
    root.geometry("400x300")  # Set window size
    root.mainloop()
