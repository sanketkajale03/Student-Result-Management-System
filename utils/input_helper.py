from utils.validation import (
    validate_name,
    validate_roll_number,
    validate_course,
    validate_marks,
)


def get_student_name():
    """Get a valid student name from the user."""
    while True:
        name = input("Enter student name: ")

        is_valid, result = validate_name(name)

        if is_valid:
            return result

        print(f"Error: {result}")


def get_roll_number():
    """Get a valid roll number from the user."""
    while True:
        roll_number = input("Enter roll number: ")

        is_valid, result = validate_roll_number(roll_number)

        if is_valid:
            return result

        print(f"Error: {result}")


def get_course():
    """Get a valid course name from the user."""
    while True:
        course = input("Enter course: ")

        is_valid, result = validate_course(course)

        if is_valid:
            return result

        print(f"Error: {result}")


def get_marks(subject_name):
    """Get valid marks for a subject."""
    while True:
        marks = input(f"Enter {subject_name} marks (0-100): ")

        is_valid, result = validate_marks(marks)

        if is_valid:
            return result

        print(f"Error: {result}")


def get_student_marks():
    """Get marks for all five subjects."""
    return {
        "physics": get_marks("Physics"),
        "chemistry": get_marks("Chemistry"),
        "mathematics": get_marks("Mathematics"),
        "english": get_marks("English"),
        "computer": get_marks("Computer"),
    }
