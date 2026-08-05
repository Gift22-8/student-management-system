students = []
def view_students(students):
     for student in students:
                     print(student)
def add_student(students, name):
     name = name.strip()


     if not name:
      print("name can not be empty.")
      return


     if name in students:
            print("student already exists.")
            return
     
     students.append(name)
     print("Student added successfully!")  

def search_student(students, search_name):
        search_name = search_name.strip()


        if not search_name:
               print("name can not be  empty.")
               return "empty"


        if search_name in students:
               return search_name

        return None
    
def update_student(students):
       student_to_update = input("Enter the name of the student you want to update: ")
       student_to_update = student_to_update.strip()
       if  not student_to_update:
               print("name can not be empty.")
               return
       for index, student in enumerate(students):
                      if student == student_to_update:
                          new_name =input("Enter the new name for the student: ")
                          new_name = new_name.strip()

                          if not new_name:
                           print("Name can not be empty.")
                           return
                          
                          if new_name in students and new_name != student_to_update:
                           print("Student already exists.")
                           return
                      
                          students[index] = new_name
                          print("Student updated successfully!")
                          break             
def delete_student(students):
             student_to_delete = input("Enter the name the student you want to delete: ")
             student_to_delete = student_to_delete.strip()


             if not student_to_delete:
                    print("Name can not be empty.")
                    return

             
             if student_to_delete in students:
                   students.remove(student_to_delete)
                   print("student deleted successfully!")
             else:
                     print("student not found.")                                           
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
       add_student(students, name)

    elif option == "6":
       print("Goodbye!")
       break
    elif option == "2":
       view_students(students)
            
    elif option == "3":
        search_name = input("Enter student name to search: ")
        result = search_student(students, search_name)
        if result == "empty":
               pass
        elif result:
               print("student found:", result)
        else:
               print("student not found")

       
    elif option == "4":
           update_student(students)
    elif option == "5":
           delete_student(students)

       

