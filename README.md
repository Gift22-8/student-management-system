# Student Management System

A desktop application for managing student records, built using **Python**, **Tkinter**, **SQLite**, **OOP**, and **unittest**.

This project demonstrates software engineering fundamentals: modular architecture, separation of database logic from user interfaces, input validation, robust error handling, automated testing, and Git version control.

---

## 🌟 Key Features

* **Interactive Tkinter Dashboard**: View live statistics including total enrolled student count.
* **Students Directory (`ttk.Treeview`)**: View all stored students in an organized grid table with columns for ID, Name, Email, Phone, Age, and Department.
* **Edit Student Modal**: Select a student record from the table to open a populated edit form, validate changes, and update SQLite records seamlessly.
* **Add New Student**: Dedicated form interface with real-time input validation (email format, positive integer age, numeric phone, non-empty fields).
* **Search System**: Search student records instantly by Name, Email, Department, or ID.
* **Delete Student with Safety Dialog**: Remove student records with confirmation prompts (`messagebox.askyesno`) to prevent accidental deletion.
* **Database Persistence**: Automatic table creation and schema migration using SQLite (`students.db`).
* **Automated Unit Test Suite**: Comprehensive tests covering database CRUD operations and input validation functions.

---

## 🛠️ Technologies Used

* **Language**: Python 3
* **GUI Framework**: Tkinter & `ttk` (Treeview, Toplevel, Scrollbars, Frames, Messagebox)
* **Database**: SQLite3
* **Software Architecture**: Object-Oriented Programming (OOP) & Layer Decoupling
* **Testing**: Python `unittest` framework
* **Version Control**: Git & GitHub (Feature Branch & Pull Request workflow)

---

## 📁 Project Structure

```text
student-management-system/
├── main.py          # Database models (Student, StudentManager), SQLite table setup & CLI
├── gui.py           # Tkinter Graphical User Interface & event handlers
├── test_main.py     # Automated unit tests for database CRUD and validation
├── students.db      # SQLite database file (generated automatically)
├── README.md        # Project documentation
└── .gitignore       # Git ignore rules
```

---

## 🚀 How to Run the Application

### 1. Launch the Desktop GUI
Open your terminal in the project directory and run:

```bash
python gui.py
```

### 2. Launch the CLI Version (Optional)
```bash
python main.py
```

*Note: The SQLite database file (`students.db`) is created automatically upon initial launch.*

---

## 🧪 Running Automated Tests

To execute the unit test suite and verify database CRUD operations:

```bash
python -m unittest test_main.py
```

Expected Output:
```text
.....
----------------------------------------------------------------------
Ran 5 tests in 0.005s

OK
```

---

## 🗄️ Database Schema

The SQLite database table `students` consists of the following fields:

| Field Name | Type | Description |
| :--- | :--- | :--- |
| `id` | `INTEGER PRIMARY KEY` | Auto-incrementing unique student identifier |
| `name` | `TEXT` | Full name of the student |
| `email` | `TEXT` | Student email address |
| `phone` | `TEXT` | Contact phone number (numeric) |
| `age` | `INTEGER` | Age in years (> 0) |
| `department` | `TEXT` | Academic department / program |

---

## 🔀 Git & GitHub Workflow

This project follows professional Git development practices:
1. Feature development on isolated branches (`feature/edit-student`, `feature/add-student`, `feature/search-student`, `feature/ui-and-docs`).
2. Local execution & unit test verification prior to commits.
3. Logical commits with clear descriptive messages.
4. Pushing feature branches to GitHub remote (`origin`).
5. Pull Request review & merge integration into `master`.