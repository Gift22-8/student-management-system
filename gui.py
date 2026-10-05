from main import StudentManager, connection

import tkinter as tk

root = tk.Tk()

manager = StudentManager(connection)

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

dashboard_title = tk.Label(
    content,
    text="Dashboard",
    font=("Arial", 22)
)

dashboard_title.pack(pady=30)

student_card = tk.Frame(
    content,
    width=200,
    height=100,
    bg="#1e293b",
    bd=1,
    relief="solid"
)
student_card.pack_propagate(False)
student_card.pack(pady=20)

student_count = tk.Label(
    student_card,
    text=str(manager.get_student_count()),
    font=("Arial", 24),
    bg="#1e293b",
    fg="white"
)

student_count.pack(pady=(15, 0))


student_text = tk.Label(
    student_card,
    text="Total Students",
    font=("Arial", 12),
    bg="#1e293b",
    fg="white"
)

student_text.pack()

root.mainloop()