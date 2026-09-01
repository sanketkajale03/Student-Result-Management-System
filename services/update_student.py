from database.database import get_connection
from models.student import Student
from utils.input_helper import (
    get_student_name,
    get_course,
    get_student_marks,
)


def update_student():
    """Update an existing student's information."""

    print("\n" + "=" * 50)
    print("            UPDATE STUDENT")
    print("=" * 50)

    roll_number = input("Enter roll number: ").strip()

    connection = None
    cursor = None

    try:
        connection = get_connection()

        if connection is None:
            print("Database connection failed.")
            return

        cursor = connection.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM students WHERE roll_number=%s",
            (roll_number,),
        )

        student = cursor.fetchone()

        if student is None:
            print("Student not found.")
            return

        print("\nCurrent Details")
        print("-" * 50)
        print(f"Name   : {student['student_name']}")
        print(f"Course : {student['course']}")
        print("-" * 50)

        student_name = get_student_name()
        course = get_course()
        marks = get_student_marks()

        obj = Student(
            student_name=student_name,
            roll_number=roll_number,
            course=course,
            physics=marks["physics"],
            chemistry=marks["chemistry"],
            mathematics=marks["mathematics"],
            english=marks["english"],
            computer=marks["computer"],
        )

        result = obj.calculate_result_details()

        update_query = """
        UPDATE students
        SET
            student_name=%s,
            course=%s,
            physics=%s,
            chemistry=%s,
            mathematics=%s,
            english=%s,
            computer=%s,
            total=%s,
            percentage=%s,
            grade=%s,
            result=%s
        WHERE roll_number=%s
        """

        values = (
            obj.student_name,
            obj.course,
            obj.physics,
            obj.chemistry,
            obj.mathematics,
            obj.english,
            obj.computer,
            result["total"],
            result["percentage"],
            result["grade"],
            result["result"],
            roll_number,
        )

        cursor.execute(update_query, values)
        connection.commit()

        print("\nStudent updated successfully!")

    except Exception as error:
        print(f"Error: {error}")

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()