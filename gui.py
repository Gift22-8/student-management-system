from main import StudentManager, connection

import tkinter as tk
from tkinter import ttk

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

def show_students():
   dashboard_title.config(text="students")
   student_count.pack_forget()
   student_text.pack_forget()


   student_table = ttk.Treeview(
    content,
    columns=("id", "name", "email", "phone", "age", "department"),
    show="headings"
)

   student_table.heading("id", text="ID")
   student_table.heading("name", text="Name")
   student_table.heading("email", text="Email")
   student_table.heading("phone", text="Phone")
   student_table.heading("age", text="Age")
   student_table.heading("department", text="Department")

   students = manager.get_all_students()

   for student in students:
    print(student.name)

   student_table.pack()

students_button = tk.Button(
    sidebar,
    text="Students",
    command = show_students
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