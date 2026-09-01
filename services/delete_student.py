from database.database import get_connection


def delete_student():
    """Delete a student by roll number."""

    print("\n" + "=" * 50)
    print("            DELETE STUDENT")
    print("=" * 50)

    roll_number = input("Enter roll number: ").strip()

    if not roll_number:
        print("Roll number cannot be empty.")
        return

    connection = None
    cursor = None

    try:
        connection = get_connection()

        if connection is None:
            print("Database connection failed.")
            return

        cursor = connection.cursor(dictionary=True)

        cursor.execute(
            "SELECT student_name, roll_number, course FROM students WHERE roll_number=%s",
            (roll_number,),
        )

        student = cursor.fetchone()

        if student is None:
            print("\nStudent not found.")
            return

        print("\nStudent Details")
        print("-" * 40)
        print(f"Name        : {student['student_name']}")
        print(f"Roll Number : {student['roll_number']}")
        print(f"Course      : {student['course']}")
        print("-" * 40)

        confirm = input("Delete this student? (y/n): ").strip().lower()

        if confirm != "y":
            print("Deletion cancelled.")
            return

        cursor.execute(
            "DELETE FROM students WHERE roll_number=%s",
            (roll_number,),
        )

        connection.commit()

        print("\nStudent deleted successfully!")

    except Exception as error:
        print(f"Error: {error}")

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()