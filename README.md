# Student Management System

This is a Student Management System I built using Python. It lets the user add, view, search, update, and delete student information.

The project uses SQLite to store the student data so that the information is not lost when the program is closed. I also used classes and object-oriented programming to organize the project.

Each student can have a name, email, phone number, age, and department.

## Features

- Add a new student
- View all students
- Search for a student by name
- Update student information
- Delete a student
- Store student information using SQLite
- Validate user input
- Handle invalid input and errors
- Use object-oriented programming
- Run unit tests

## Technologies Used

- Python
- SQLite
- unittest
- Git and GitHub

## How to Run

1. Clone the repository.
2. Open the project folder in your terminal.
3. Run the program with:

```bash
python main.py
```
The students.db file is not included in the GitHub repository because it contains local student data. The database is created automatically when the program runs.

## Testing

The project includes unit tests for the main student management functions.

To run the tests, use:

```bash
python -m unittest