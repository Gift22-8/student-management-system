from main import StudentManager, connection, validate_student_data

import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
manager = StudentManager(connection)

root.title("Student Management System")
root.geometry("850x550")
root.minsize(750, 450)

# Header Section
header = tk.Frame(root, bg="#0f172a", height=60)
header.pack(fill="x", side="top")

title_label = tk.Label(
    header,
    text="Student Management System",
    font=("Arial", 20, "bold"),
    bg="#0f172a",
    fg="white",
    pady=15
)
title_label.pack()

# Sidebar Navigation Frame
sidebar = tk.Frame(root, width=200, bg="#1e293b")
sidebar.pack(side="left", fill="y")

# Main Content Area Frame
content = tk.Frame(root, bg="#f8fafc")
content.pack(side="right", fill="both", expand=True)

# Helper function to clear content frame before switching views
def clear_content():
    for widget in content.winfo_children():
        widget.destroy()

# ==================== VIEW 1: DASHBOARD ====================
def show_dashboard():
    clear_content()

    dashboard_title = tk.Label(
        content,
        text="Dashboard",
        font=("Arial", 22, "bold"),
        bg="#f8fafc",
        fg="#0f172a"
    )
    dashboard_title.pack(pady=30)

    # Student Count Card
    student_card = tk.Frame(
        content,
        width=240,
        height=120,
        bg="#1e293b",
        bd=1,
        relief="solid"
    )
    student_card.pack_propagate(False)
    student_card.pack(pady=20)

    count_val = manager.get_student_count()
    student_count = tk.Label(
        student_card,
        text=str(count_val),
        font=("Arial", 28, "bold"),
        bg="#1e293b",
        fg="white"
    )
    student_count.pack(pady=(20, 0))

    student_text = tk.Label(
        student_card,
        text="Total Students",
        font=("Arial", 12),
        bg="#1e293b",
        fg="#cbd5e1"
    )
    student_text.pack()

# ==================== EDIT STUDENT MODAL ====================
def open_edit_dialog(selected_values, refresh_callback):
    student_id = selected_values[0]

    edit_win = tk.Toplevel(root)
    edit_win.title("Edit Student")
    edit_win.geometry("400x480")
    edit_win.resizable(False, False)
    edit_win.transient(root)
    edit_win.grab_set()

    tk.Label(
        edit_win,
        text="Edit Student Details",
        font=("Arial", 16, "bold"),
        pady=15
    ).pack()

    form_frame = tk.Frame(edit_win, padx=20, pady=10)
    form_frame.pack(fill="both", expand=True)

    fields = ["Name", "Email", "Phone", "Age", "Department"]
    entries = {}

    initial_data = {
        "Name": selected_values[1],
        "Email": selected_values[2],
        "Phone": selected_values[3],
        "Age": selected_values[4],
        "Department": selected_values[5]
    }

    for idx, field in enumerate(fields):
        lbl = tk.Label(form_frame, text=f"{field}:", font=("Arial", 10, "bold"), anchor="w")
        lbl.grid(row=idx, column=0, sticky="w", pady=8)
        
        entry = tk.Entry(form_frame, font=("Arial", 10), width=25)
        entry.insert(0, str(initial_data[field]))
        entry.grid(row=idx, column=1, pady=8, padx=5)
        entries[field] = entry

    def save_changes():
        name = entries["Name"].get()
        email = entries["Email"].get()
        phone = entries["Phone"].get()
        age = entries["Age"].get()
        department = entries["Department"].get()

        is_valid, err = validate_student_data(name, email, phone, age, department)
        if not is_valid:
            messagebox.showerror("Validation Error", err, parent=edit_win)
            return

        try:
            manager.update_student(student_id, name, email, phone, age, department)
            messagebox.showinfo("Success", "Student updated successfully!", parent=edit_win)
            edit_win.destroy()
            refresh_callback()
        except Exception as e:
            messagebox.showerror("Database Error", str(e), parent=edit_win)

    btn_frame = tk.Frame(edit_win, pady=15)
    btn_frame.pack(fill="x")

    save_btn = tk.Button(
        btn_frame,
        text="Save Changes",
        font=("Arial", 10, "bold"),
        bg="#0284c7",
        fg="white",
        padx=15,
        pady=5,
        command=save_changes
    )
    save_btn.pack(side="right", padx=20)

    cancel_btn = tk.Button(
        btn_frame,
        text="Cancel",
        font=("Arial", 10),
        padx=15,
        pady=5,
        command=edit_win.destroy
    )
    cancel_btn.pack(side="right")

# ==================== VIEW 2: STUDENTS DIRECTORY ====================
def show_students():
    clear_content()

    title_label = tk.Label(
        content,
        text="Students Directory",
        font=("Arial", 22, "bold"),
        bg="#f8fafc",
        fg="#0f172a"
    )
    title_label.pack(pady=(20, 10))

    # Action Toolbar Frame
    toolbar = tk.Frame(content, bg="#f8fafc")
    toolbar.pack(fill="x", padx=20, pady=(0, 10))

    # Table Frame
    table_frame = tk.Frame(content)
    table_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))

    student_table = ttk.Treeview(
        table_frame,
        columns=("id", "name", "email", "phone", "age", "department"),
        show="headings"
    )

    student_table.heading("id", text="ID")
    student_table.heading("name", text="Name")
    student_table.heading("email", text="Email")
    student_table.heading("phone", text="Phone")
    student_table.heading("age", text="Age")
    student_table.heading("department", text="Department")

    student_table.column("id", width=50, anchor="center")
    student_table.column("name", width=140)
    student_table.column("email", width=180)
    student_table.column("phone", width=110)
    student_table.column("age", width=50, anchor="center")
    student_table.column("department", width=150)

    scrollbar = ttk.Scrollbar(
        table_frame,
        orient="vertical",
        command=student_table.yview
    )
    student_table.configure(yscrollcommand=scrollbar.set)

    student_table.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    def load_table_data():
        for item in student_table.get_children():
            student_table.delete(item)
        students = manager.get_all_students()
        for student in students:
            student_table.insert(
                "",
                "end",
                values=(
                    student.id,
                    student.name,
                    student.email,
                    student.phone,
                    student.age,
                    student.department
                )
            )

    def delete_selected_student():
        selected_item = student_table.selection()
        if not selected_item:
            messagebox.showwarning("Selection Required", "Please select a student to delete.")
            return

        student_values = student_table.item(selected_item[0])["values"]
        student_id = student_values[0]
        student_name = student_values[1]

        confirm = messagebox.askyesno(
            "Confirm Delete",
            f"Are you sure you want to delete student '{student_name}' (ID: {student_id})?"
        )
        if confirm:
            manager.delete_student(student_id)
            load_table_data()
            messagebox.showinfo("Deleted", "Student deleted successfully.")

    def edit_selected_student():
        selected_item = student_table.selection()
        if not selected_item:
            messagebox.showwarning("Selection Required", "Please select a student to edit.")
            return
        student_values = student_table.item(selected_item[0])["values"]
        open_edit_dialog(student_values, load_table_data)

    edit_button = tk.Button(
        toolbar,
        text="Edit Student",
        font=("Arial", 10, "bold"),
        bg="#0284c7",
        fg="white",
        padx=10,
        pady=3,
        command=edit_selected_student
    )
    edit_button.pack(side="left", padx=(0, 10))

    delete_button = tk.Button(
        toolbar,
        text="Delete Student",
        font=("Arial", 10, "bold"),
        bg="#ef4444",
        fg="white",
        padx=10,
        pady=3,
        command=delete_selected_student
    )
    delete_button.pack(side="left")

    load_table_data()

# ==================== VIEW 3: ADD STUDENT ====================
def show_add_student():
    clear_content()

    title_label = tk.Label(
        content,
        text="Add New Student",
        font=("Arial", 22, "bold"),
        bg="#f8fafc",
        fg="#0f172a"
    )
    title_label.pack(pady=20)

    form_frame = tk.Frame(content, bg="#f8fafc", padx=40, pady=20)
    form_frame.pack()

    fields = ["Name", "Email", "Phone", "Age", "Department"]
    entries = {}

    for idx, field in enumerate(fields):
        lbl = tk.Label(
            form_frame,
            text=f"{field}:",
            font=("Arial", 11, "bold"),
            bg="#f8fafc",
            fg="#334155",
            anchor="w"
        )
        lbl.grid(row=idx, column=0, sticky="w", pady=10)

        entry = tk.Entry(form_frame, font=("Arial", 11), width=30)
        entry.grid(row=idx, column=1, pady=10, padx=10)
        entries[field] = entry

    def submit_new_student():
        name = entries["Name"].get()
        email = entries["Email"].get()
        phone = entries["Phone"].get()
        age = entries["Age"].get()
        department = entries["Department"].get()

        is_valid, err = validate_student_data(name, email, phone, age, department)
        if not is_valid:
            messagebox.showerror("Validation Error", err)
            return

        try:
            manager.add_student(name, email, phone, age, department)
            messagebox.showinfo("Success", "Student added successfully!")
            show_students()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    submit_btn = tk.Button(
        form_frame,
        text="Add Student",
        font=("Arial", 11, "bold"),
        bg="#16a34a",
        fg="white",
        padx=20,
        pady=6,
        command=submit_new_student
    )
    submit_btn.grid(row=len(fields), column=1, sticky="e", pady=20, padx=10)

# ==================== VIEW 4: SEARCH STUDENT ====================
def show_search():
    clear_content()

    title_label = tk.Label(
        content,
        text="Search Students",
        font=("Arial", 22, "bold"),
        bg="#f8fafc",
        fg="#0f172a"
    )
    title_label.pack(pady=(20, 10))

    search_bar_frame = tk.Frame(content, bg="#f8fafc")
    search_bar_frame.pack(fill="x", padx=20, pady=(0, 15))

    lbl = tk.Label(
        search_bar_frame,
        text="Search (Name, Email, Dept, ID):",
        font=("Arial", 10, "bold"),
        bg="#f8fafc"
    )
    lbl.pack(side="left", padx=(0, 10))

    search_entry = tk.Entry(search_bar_frame, font=("Arial", 11), width=30)
    search_entry.pack(side="left", padx=(0, 10))

    table_frame = tk.Frame(content)
    table_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))

    student_table = ttk.Treeview(
        table_frame,
        columns=("id", "name", "email", "phone", "age", "department"),
        show="headings"
    )

    student_table.heading("id", text="ID")
    student_table.heading("name", text="Name")
    student_table.heading("email", text="Email")
    student_table.heading("phone", text="Phone")
    student_table.heading("age", text="Age")
    student_table.heading("department", text="Department")

    student_table.column("id", width=50, anchor="center")
    student_table.column("name", width=140)
    student_table.column("email", width=180)
    student_table.column("phone", width=110)
    student_table.column("age", width=50, anchor="center")
    student_table.column("department", width=150)

    scrollbar = ttk.Scrollbar(
        table_frame,
        orient="vertical",
        command=student_table.yview
    )
    student_table.configure(yscrollcommand=scrollbar.set)

    student_table.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    def perform_search():
        query = search_entry.get().strip()
        for item in student_table.get_children():
            student_table.delete(item)
        
        results = manager.search_student(query)
        for student in results:
            student_table.insert(
                "",
                "end",
                values=(
                    student.id,
                    student.name,
                    student.email,
                    student.phone,
                    student.age,
                    student.department
                )
            )

    def reset_search():
        search_entry.delete(0, tk.END)
        perform_search()

    search_btn = tk.Button(
        search_bar_frame,
        text="Search",
        font=("Arial", 10, "bold"),
        bg="#0284c7",
        fg="white",
        padx=12,
        pady=3,
        command=perform_search
    )
    search_btn.pack(side="left", padx=(0, 5))

    reset_btn = tk.Button(
        search_bar_frame,
        text="Reset",
        font=("Arial", 10),
        padx=12,
        pady=3,
        command=reset_search
    )
    reset_btn.pack(side="left")

    perform_search()

# ==================== SIDEBAR BUTTONS ====================
btn_style = {
    "font": ("Arial", 11, "bold"),
    "bg": "#334155",
    "fg": "white",
    "activebackground": "#475569",
    "activeforeground": "white",
    "bd": 0,
    "pady": 8
}

dashboard_button = tk.Button(
    sidebar,
    text="Dashboard",
    command=show_dashboard,
    **btn_style
)
dashboard_button.pack(fill="x", padx=10, pady=10)

students_button = tk.Button(
    sidebar,
    text="Students",
    command=show_students,
    **btn_style
)
students_button.pack(fill="x", padx=10, pady=10)

add_button = tk.Button(
    sidebar,
    text="Add Student",
    command=show_add_student,
    **btn_style
)
add_button.pack(fill="x", padx=10, pady=10)

search_button = tk.Button(
    sidebar,
    text="Search",
    command=show_search,
    **btn_style
)
search_button.pack(fill="x", padx=10, pady=10)

# Load default view on start
show_dashboard()

if __name__ == "__main__":
    root.mainloop()