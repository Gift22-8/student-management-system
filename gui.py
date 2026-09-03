import tkinter as tk

root = tk.Tk()

root.title("Student Management System")

root.geometry("800x500")

header = tk.Frame(root)
header.pack(fill="x")

title_label = tk.Label(
    root,
    text="Student Management System",
    font=("Arial", 24)
)

title_label.pack(pady=30)

sidebar = tk.Frame(root, width=200)
sidebar.pack(side="left", fill="y")

dashboard_button = tk.Button(
    sidebar,
    text="Dashboard"
)

dashboard_button.pack(fill="x", padx=10, pady=10)

students_button = tk.Button(
    sidebar,
    text="Students"
)

students_button.pack(fill="x", padx=10, pady=10)


add_button = tk.Button(
    sidebar,
    text="Add Student"
)

add_button.pack(fill="x", padx=10, pady=10)


search_button = tk.Button(
    sidebar,
    text="Search"
)

search_button.pack(fill="x", padx=10, pady=10)

content = tk.Frame(root)
content.pack(side="right", fill="both", expand=True)

root.mainloop()