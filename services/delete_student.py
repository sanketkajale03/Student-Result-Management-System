from database.database import get_connection


def delete_student():
    print("\n" + "=" * 50)
    print("              DELETE STUDENT")
    print("=" * 50)

    roll_number = input("Enter student roll number: ").strip()

    if not roll_number:
        print("Error: Roll number cannot be empty.")
        return

    connection = None
    cursor = None

    try:
        connection = get_connection()

        if connection is None:
            print("Error: Could not connect to the database.")
            return

        cursor = connection.cursor()

        # Check whether the student exists
        check_query = """
            SELECT student_name
            FROM students
            WHERE roll_number = %s
        """

        cursor.execute(check_query, (roll_number,))
        student = cursor.fetchone()

        if student is None:
            print("\nStudent not found.")
            return

        student_name = student[0]

        # Delete the student
        delete_query = """
            DELETE FROM students
            WHERE roll_number = %s
        """

        cursor.execute(delete_query, (roll_number,))
        connection.commit()

        print("\nStudent deleted successfully.")
        print(f"Name        : {student_name}")
        print(f"Roll Number : {roll_number}")

    except Exception as error:
        if connection:
            connection.rollback()

        print(f"Error: {error}")

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()