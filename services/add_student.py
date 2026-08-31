from database.database import get_connection
from models.student import Student
from utils.input_helper import (
    get_student_name,
    get_roll_number,
    get_course,
    get_student_marks,
)


def add_student():
    """Collect student information and save it to the database."""

    print("\n" + "=" * 50)
    print("              ADD STUDENT")
    print("=" * 50)

    student_name = get_student_name()
    roll_number = get_roll_number()
    course = get_course()
    marks = get_student_marks()

    student = Student(
        student_name=student_name,
        roll_number=roll_number,
        course=course,
        physics=marks["physics"],
        chemistry=marks["chemistry"],
        mathematics=marks["mathematics"],
        english=marks["english"],
        computer=marks["computer"],
    )

    result_details = student.calculate_result_details()

    connection = None
    cursor = None

    try:
        connection = get_connection()

        if connection is None:
            print("Error: Could not connect to the database.")
            return

        cursor = connection.cursor()

        query = """
            INSERT INTO students (
                student_name,
                roll_number,
                course,
                physics,
                chemistry,
                mathematics,
                english,
                computer,
                total,
                percentage,
                grade,
                result
            )
            VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            )
        """

        values = (
            student.student_name,
            student.roll_number,
            student.course,
            student.physics,
            student.chemistry,
            student.mathematics,
            student.english,
            student.computer,
            result_details["total"],
            result_details["percentage"],
            result_details["grade"],
            result_details["result"],
        )

        cursor.execute(query, values)
        connection.commit()

        student.student_id = cursor.lastrowid

        print("\nStudent added successfully!")
        print("-" * 50)
        print(f"Student ID : {student.student_id}")
        print(f"Name       : {student.student_name}")
        print(f"Roll Number: {student.roll_number}")
        print(f"Course     : {student.course}")
        print(f"Total      : {student.total:.2f}")
        print(f"Percentage : {student.percentage:.2f}%")
        print(f"Grade      : {student.grade}")
        print(f"Result     : {student.result}")
        print("-" * 50)

    except Exception as error:
        if connection:
            connection.rollback()

        if "Duplicate entry" in str(error):
            print("Error: This roll number already exists.")
        else:
            print(f"Error while adding student: {error}")

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()