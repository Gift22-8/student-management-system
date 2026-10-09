import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()

# Connect to the SQLite database and create the students table.
cursor.execute("""CREATE TABLE IF NOT EXISTS students (
      id INTEGER PRIMARY KEY,
      name TEXT
)
""")

# Add new columns if they don't already exist.
cursor.execute("PRAGMA table_info(students)")
columns = [column[1] for column in cursor.fetchall()]

if "email" not in columns:
    cursor.execute("ALTER TABLE students ADD COLUMN email TEXT")

if "phone" not in columns:
    cursor.execute("ALTER TABLE students ADD COLUMN phone TEXT")

if "age" not in columns:
    cursor.execute("ALTER TABLE students ADD COLUMN age INTEGER")

if "department" not in columns:
    cursor.execute("ALTER TABLE students ADD COLUMN department TEXT")



connection.commit()

# Represents a student and stores their information.
class Student:
    def __init__(self, student_id, name, email, phone, age, department):
        self.id = student_id
        self.name = name
        self.email = email
        self.phone = phone
        self.age = age
        self.department = department

def validate_student_data(name, email, phone, age, department):
    """Validates student record inputs. Returns (is_valid: bool, message: str)."""
    name = (name or "").strip()
    if not name:
        return False, "Name cannot be empty."

    email = (email or "").strip()
    if not email or "@" not in email:
        return False, "Invalid email. Must contain '@'."

    phone = (phone or "").strip()
    if not phone or not phone.isdigit():
        return False, "Invalid phone number. Numbers only."

    try:
        age_int = int(str(age).strip())
        if age_int <= 0:
            return False, "Age must be greater than 0."
    except ValueError:
        return False, "Invalid age. Please enter a valid number."

    department = (department or "").strip()
    if not department:
        return False, "Department cannot be empty."

    return True, ""


# Handles database operations for students.
class StudentManager:
    def __init__(self, connection):
        self.connection = connection

    def get_student_count(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM students")
        count = cursor.fetchone()[0]
        return count
    
    def get_all_students(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()

        return [
            Student(
                student[0], 
                student[1],
                student[2],
                student[3],
                student[4],
                student[5]
            )
            for student in students
        ]

    def get_student_by_id(self, student_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
        row = cursor.fetchone()
        if row:
            return Student(row[0], row[1], row[2], row[3], row[4], row[5])
        return None

    def delete_student(self, student_id):
        cursor = self.connection.cursor()
        cursor.execute(
            "DELETE FROM students WHERE id = ?",
            (student_id,)
        )
        self.connection.commit()
        return cursor.rowcount > 0

    def view_students(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()

        for student in students:
            student_obj = Student(
                student[0], 
                student[1],
                student[2],
                student[3],
                student[4],
                student[5]
            )
            
            print("ID:", student_obj.id)
            print("Name:", student_obj.name)
            print("Email:", student_obj.email)
            print("Phone Number:", student_obj.phone)
            print("Age:", student_obj.age)
            print("Department:", student_obj.department)
            print("-" * 30)

    def search_student(self, search_term):
        search_term = (search_term or "").strip()
        if not search_term:
            return self.get_all_students()

        cursor = self.connection.cursor()
        like_query = f"%{search_term}%"
        cursor.execute(
            """SELECT * FROM students 
               WHERE name LIKE ? OR email LIKE ? OR department LIKE ? OR CAST(id AS TEXT) = ?""",
            (like_query, like_query, like_query, search_term)
        )
        students = cursor.fetchall()

        return [
            Student(
                student[0], 
                student[1],
                student[2],
                student[3],
                student[4],
                student[5]
            )
            for student in students
        ]

    def add_student(self, name, email, phone, age, department):
        is_valid, err = validate_student_data(name, email, phone, age, department)
        if not is_valid:
            raise ValueError(err)

        name = name.strip().title()
        email = email.strip()
        phone = phone.strip()
        age = int(age)
        department = department.strip().title()

        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO students (name, email, phone, age, department) VALUES (?, ?, ?, ?, ?)",
            (name, email, phone, age, department)
        )
        self.connection.commit()
        print("Student added successfully!")
        return cursor.lastrowid

    def update_student(self, student_id, name, email, phone, age, department):
        is_valid, err = validate_student_data(name, email, phone, age, department)
        if not is_valid:
            raise ValueError(err)

        name = name.strip().title()
        email = email.strip()
        phone = phone.strip()
        age = int(age)
        department = department.strip().title()

        cursor = self.connection.cursor()
        cursor.execute(
            """UPDATE students 
               SET name = ?, email = ?, phone = ?, age = ?, department = ?
               WHERE id = ?""", 
            (name, email, phone, age, department, student_id)
        )
        if cursor.rowcount == 0:
            print("Student not found")
            return False

        self.connection.commit()
        print("Student updated successfully!")
        return True




# Runs the main menu and handles user interaction.
def main():

    manager = StudentManager(connection)
    
    while True:
        print("=" * 40)
        print("       STUDENT MANAGEMENT SYSTEM")
        print("=" * 40)
        print()
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        option = input("Enter your choice (1-6): ")

        if option == "1":
            name = input("Enter student name: ")
            name = name.strip().title()

            if not name:
                print("Name cannot be empty.")
                continue
            
            email = input("Enter student email: ")
            email = email.strip()
            
            if "@" not in email:
              print("Invalid email. Please enter a valid email address.")
              continue
            
            phone = input("Enter student phone number: ")
            phone = phone.strip()

            if not phone.isdigit():
                print("Invalid phone number. Please enter numbers only.")
                continue

            age = input("Enter student age: ")
            age = age.strip()

            try:
               age = int(age)
            except ValueError:
               print("Invalid age. Please enter a number.")
               continue

            if age <= 0:
               print("Age must be greater than 0.")
               continue
             
            department = input("Enter student department: ")
            department = department.strip().title()

            if not department:
                print("Department cannot be empty.")
                continue

            manager.add_student(name, email, phone, age, department)

        elif option == "2":
            manager.view_students()

        elif option == "3":
            search_name = input("Enter student name to search: ")
            manager.search_student(search_name)

        elif option == "4":
            manager.update_student()

        elif option == "5":
            manager.delete_student()

        elif option == "6":
            print("Goodbye!")
            connection.close()
            break
    
        else:
            print("Invalid option. Please enter a valid option (1-6).")
if __name__ == "__main__":
    main()