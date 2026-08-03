students = []
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
       students.append(name)
       print("Student added successfully!")

    elif option == "6":
       print("Goodbye!")
       break
    elif option == "2":
         if not students:
               print("No students found.")
         else:
             print("students:")
             for student in students:
                 print(student)
    elif option == "3":
         search_name = input("Enter student name to search: ")
         if search_name in students:   
             print("student found!")
         else:
             print("student not found.")
    elif option == "4":
             student_to_update = input("Enter the name of the student you want to update: ")
             for index, student in enumerate(students):
                if student == student_to_update:
                    new_name =input("Enter the new name for the student: ")
                    students[index] = new_name
                    print("Student updated successfully!")
                    break
    elif option == "5":
        student_to_delete = input("Enter the name the student you want to delete: ")
        if student_to_delete in students:
            students.remove(student_to_delete)
            print("student deleted succssfullly!")
        else:
            print("student not found.")

       

