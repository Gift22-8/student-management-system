import sqlite3
connection = sqlite3.connect("students.db")
cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS students (
      id INTEGER PRIMARY KEY,
      name TEXT
)
""")
connection.commit()

  
def add_student(name):
     name = name.strip()


     if not name:
      print("name can not be empty.")
      return

     cursor.execute(
          "INSERT INTO students (name) VALUES (?)",
          (name,)
          )
     connection.commit()

     print("Student added successfully!")  

def search_student(search_name):
        search_name = search_name.strip()


        if not search_name:
               print("name can not be  empty.")
               return 


        cursor.execute(
            "SELECT * FROM students WHERE name = ?",
                (search_name,)    )

        student = cursor.fetchone()
        if student is None:
               print("student not found.")
               return
        print("student found!")
    
def update_student():
       try:
         student_id =int(input("Enter the id of the student you want to update: "))

       except ValueError:
             print("Invalid input. Please enter a valid integer for the student id.")
             return
       
       new_name =input("Enter the new name for the student: ")
       new_name = new_name.strip()

       if not new_name:
           print("Name can not be empty.")
           return
                          
       cursor.execute(
          "UPDATE students SET name = ? WHERE id = ?",
        (new_name, student_id)
                           ) 
       if not cursor.rowcount:
             print("student not found.")
             return   
       connection.commit()
       print("student updated successfully!")         
def delete_student():
        try:
          student_id = int(input("Enter the id the student you want to delete: "))
        except ValueError:
             
             print("Invalid input. Please enter a valid integer for the student id.")
             return


        cursor.execute(
                   "DELETE FROM students WHERE id = ?",
                    (student_id,)
                    )

             
        if cursor.rowcount == 0:
                   print("student not found.")
                   return
             
        connection.commit()
        print("student deleted successfully!")   
class Student:
     def __init__(self, id, name):
           self.id =id
           self.name = name
class StudentManager:
        def __init__(self, connection):
           self.connection = connection

        def view_students(self):
           cursor = self.connection.cursor()
           cursor.execute("SELECT * FROM students")
           students = cursor.fetchall()

           for student in students:
                student_obj = Student(student[0], student[1])
                print(student_obj.id, student_obj.name)


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
       add_student(name)

    elif option == "6":
       print("Goodbye!")
       connection.close()
       break
    
    elif option == "2":
      manager.view_students()
            
    elif option == "3":
        search_name = input("Enter student name to search: ")
        search_student(search_name)

    elif option == "4":
           update_student()

    elif option == "5":
           delete_student()
    else:
         print("Invalid option. Please enter a valid option (1-6).")

      

