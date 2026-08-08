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
            name TEXT
            )
        """)
        self.connection.commit()

        self.manager = StudentManager(self.connection)

    def tearDown(self):
        self.connection.close()    

    def test_add_student(self):
        self.manager.add_student("Test Student")

        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM students")
        student = cursor.fetchone()

        self.assertEqual(student[1], "Test Student")

    def test_view_students(self):
        self.manager.add_student("Test Student")

        with patch("builtins.print") as mock_print:
            self.manager.view_students()

        mock_print.assert_any_call(1, "Test Student")

    def test_search_student(self):
        self.manager.add_student("Test Student")

        with patch("builtins.print") as mock_print:
            self.manager.search_student("Test Student")

        mock_print.assert_any_call(1, "Test Student")

    def test_update_student(self):
        self.manager.add_student("Old Name")  

        cursor = self.connection.cursor()
        cursor.execute("SELECT id FROM students WHERE name = ?", ("Old Name",))
        student_id = cursor.fetchone()[0]   

        with patch("builtins.input", side_effect=[str(student_id), "New Name"]):
            self.manager.update_student()

        cursor.execute(
            "SELECT name FROM students WHERE id = ?",
            (student_id,)
        )    
        updated_student = cursor.fetchone()

        self.assertEqual(updated_student[0], "New Name")

    def test_delete_student(self):
        self.manager.add_student("Student To Delete")

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