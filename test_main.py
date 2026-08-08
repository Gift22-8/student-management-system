import unittest
import sqlite3
from unittest.mock import patch
from main import StudentManager

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

    def test_view_students(self):
        self.manager.add_student(
            "Test Student",
            "test@gmail.com",
            "0912345678",
            21,
            "Software Engineering"
        )

        with patch("builtins.print") as mock_print:
            self.manager.view_students()

        mock_print.assert_any_call("ID:", 1)
        mock_print.assert_any_call("Name:", "Test Student")
        mock_print.assert_any_call("Email:", "test@gmail.com")
        mock_print.assert_any_call("Phone Number:", "0912345678")
        mock_print.assert_any_call("Age:", 21)
        mock_print.assert_any_call("Department:", "Software Engineering")

    def test_search_student(self):
        self.manager.add_student(
            "Test Student",
            "test@gmail.com",
            "0912345678",
            21,
            "Software Engineering"
        )

        with patch("builtins.print") as mock_print:
            self.manager.search_student("Test Student")

        mock_print.assert_any_call("ID:", 1)
        mock_print.assert_any_call("Name:", "Test Student")
        mock_print.assert_any_call("Email:", "test@gmail.com")
        mock_print.assert_any_call("Phone Number:", "0912345678")
        mock_print.assert_any_call("Age:", 21)
        mock_print.assert_any_call("Department:", "Software Engineering")

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

        with patch(
            "builtins.input", 
            side_effect=[
                str(student_id),
                "New Name",
                "new@gmail.com",
                "0922222222",
                "21",
                "Software Engineering"
           ]
        ):
            self.manager.update_student()

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

        with patch("builtins.input", return_value=str(student_id)):
            self.manager.delete_student()

        cursor.execute(
            "SELECT * FROM students WHERE id = ?",
            (student_id,)
        )
        student = cursor.fetchone()

        self.assertIsNone(student)

if __name__ == "__main__":
    unittest.main()