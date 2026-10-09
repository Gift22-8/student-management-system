import unittest
import sqlite3
from main import StudentManager, validate_student_data

class TestStudentManager(unittest.TestCase):
    def setUp(self):
        self.connection = sqlite3.connect(":memory:")

        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT,
            phone TEXT,
            age INTEGER,
            department TEXT
            )
        """)
        self.connection.commit()

        self.manager = StudentManager(self.connection)

    def tearDown(self):
        self.connection.close()    

    def test_add_student(self):
        self.manager.add_student(
            "Test Student",
            "test@gmail.com",
            "0912345678",
            21,
            "Software Engineering")

        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM students")
        student = cursor.fetchone()

        self.assertEqual(student[1], "Test Student")
        self.assertEqual(student[2], "test@gmail.com")
        self.assertEqual(student[3], "0912345678")
        self.assertEqual(student[4], 21)
        self.assertEqual(student[5], "Software Engineering")

    def test_search_student(self):
        self.manager.add_student(
            "Test Student",
            "test@gmail.com",
            "0912345678",
            21,
            "Software Engineering"
        )

        results = self.manager.search_student("Test")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "Test Student")
        self.assertEqual(results[0].email, "test@gmail.com")

    def test_update_student(self):
        self.manager.add_student(
            "Old Name",
            "old@gmail.com",
            "0911111111",
            20,
            "Computer Science"
        )  

        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT id FROM students WHERE name = ?", 
            ("Old Name",)
        )
        student_id = cursor.fetchone()[0]   

        success = self.manager.update_student(
            student_id,
            "New Name",
            "new@gmail.com",
            "0922222222",
            21,
            "Software Engineering"
        )

        self.assertTrue(success)

        cursor.execute(
            "SELECT name, email, phone, age, department FROM students WHERE id = ?",
            (student_id,)
        )    
        updated_student = cursor.fetchone()

        self.assertEqual(updated_student[0], "New Name")
        self.assertEqual(updated_student[1], "new@gmail.com")
        self.assertEqual(updated_student[2], "0922222222")
        self.assertEqual(updated_student[3], 21)
        self.assertEqual(updated_student[4], "Software Engineering")

    def test_delete_student(self):
        self.manager.add_student(
            "Student To Delete",
            "delete@gmail.com",
            "0933333333",
            22,
            "Information Technology"
        )

        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT id FROM students WHERE name = ?",
            ("Student To Delete",)
        )
        student_id = cursor.fetchone()[0]

        success = self.manager.delete_student(student_id)
        self.assertTrue(success)

        cursor.execute(
            "SELECT * FROM students WHERE id = ?",
            (student_id,)
        )
        student = cursor.fetchone()

        self.assertIsNone(student)

    def test_validation(self):
        is_valid, err = validate_student_data("Alice", "alice@example.com", "123456", 20, "CS")
        self.assertTrue(is_valid)
        self.assertEqual(err, "")

        is_valid, err = validate_student_data("", "alice@example.com", "123456", 20, "CS")
        self.assertFalse(is_valid)
        self.assertIn("Name cannot be empty", err)

        is_valid, err = validate_student_data("Alice", "invalidemail", "123456", 20, "CS")
        self.assertFalse(is_valid)
        self.assertIn("Invalid email", err)

        is_valid, err = validate_student_data("Alice", "alice@example.com", "abc", 20, "CS")
        self.assertFalse(is_valid)
        self.assertIn("Invalid phone number", err)

        is_valid, err = validate_student_data("Alice", "alice@example.com", "123456", -5, "CS")
        self.assertFalse(is_valid)
        self.assertIn("Age must be greater than 0", err)

if __name__ == "__main__":
    unittest.main()