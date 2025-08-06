import tkinter as tk
from tkinter import messagebox, simpledialog

class Alumni:
    def __init__(self, name, email, batch, password):
        self.name = name
        self.email = email
        self.batch = batch
        self.password = password
        self.posts = []

class AlumniConnectApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Alumni Connect")
        self.alumni_list = []
        self.logged_in_user = None
        self.wall = []

        self.create_main_menu()

    def create_main_menu(self):
        self.clear_window()
        tk.Label(self.root, text="Welcome to Alumni Connect", font=("Arial", 18)).pack(pady=10)

        tk.Button(self.root, text="Register", width=20, command=self.register).pack(pady=5)
        tk.Button(self.root, text="Login", width=20, command=self.login).pack(pady=5)
        tk.Button(self.root, text="Post Message", width=20, command=self.post_message).pack(pady=5)
        tk.Button(self.root, text="View Wall", width=20, command=self.view_wall).pack(pady=5)
        tk.Button(self.root, text="List Alumni", width=20, command=self.list_alumni).pack(pady=5)
        tk.Button(self.root, text="Logout", width=20, command=self.logout).pack(pady=5)
        tk.Button(self.root, text="Exit", width=20, command=self.root.quit).pack(pady=5)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def register(self):
        name = simpledialog.askstring("Register", "Enter name:")
        email = simpledialog.askstring("Register", "Enter email:")
        batch = simpledialog.askstring("Register", "Enter batch (e.g., 2022):")
        password = simpledialog.askstring("Register", "Create a password:", show='*')

        if not all([name, email, batch, password]):
            messagebox.showerror("Error", "All fields are required!")
            return

        for alumni in self.alumni_list:
            if alumni.email == email:
                messagebox.showwarning("Warning", "Email already registered!")
                return

        new_alumni = Alumni(name, email, batch, password)
        self.alumni_list.append(new_alumni)
        messagebox.showinfo("Success", "Registration successful!")

    def login(self):
        email = simpledialog.askstring("Login", "Enter email:")
        password = simpledialog.askstring("Login", "Enter password:", show='*')

        for alumni in self.alumni_list:
            if alumni.email == email and alumni.password == password:
                self.logged_in_user = alumni
                messagebox.showinfo("Welcome", f"Welcome, {alumni.name}!")
                return

        messagebox.showerror("Login Failed", "Invalid email or password.")

    def logout(self):
        if self.logged_in_user:
            messagebox.showinfo("Logout", f"Goodbye, {self.logged_in_user.name}!")
            self.logged_in_user = None
        else:
            messagebox.showwarning("Not Logged In", "No user is currently logged in.")

    def post_message(self):
        if not self.logged_in_user:
            messagebox.showwarning("Login Required", "Please log in first.")
            return

        message = simpledialog.askstring("Post Message", "Write your message:")
        if message:
            entry = f"{self.logged_in_user.name} ({self.logged_in_user.batch}): {message}"
            self.wall.append(entry)
            self.logged_in_user.posts.append(message)
            messagebox.showinfo("Posted", "Message posted successfully.")

    def view_wall(self):
        self.clear_window()
        tk.Label(self.root, text="Shared Wall", font=("Arial", 16)).pack(pady=10)

        if not self.wall:
            tk.Label(self.root, text="No messages yet.").pack()
        else:
            for msg in self.wall:
                tk.Label(self.root, text=msg, wraplength=400, justify="left").pack(anchor="w", padx=10)

        tk.Button(self.root, text="Back", command=self.create_main_menu).pack(pady=10)

    def list_alumni(self):
        self.clear_window()
        tk.Label(self.root, text="Registered Alumni", font=("Arial", 16)).pack(pady=10)

        if not self.alumni_list:
            tk.Label(self.root, text="No alumni registered yet.").pack()
        else:
            for alumni in self.alumni_list:
                info = f"{alumni.name} | Batch: {alumni.batch} | Email: {alumni.email}"
                tk.Label(self.root, text=info).pack(anchor="w", padx=10)

        tk.Button(self.root, text="Back", command=self.create_main_menu).pack(pady=10)

# Start GUI
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x500")
    app = AlumniConnectApp(root)
    root.mainloop()
    

