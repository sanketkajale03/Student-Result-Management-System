from database.database import get_connection


def search_student():
    """Search for a student by roll number."""

    print("\n" + "=" * 50)
    print("             SEARCH STUDENT")
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

        cursor = connection.cursor(dictionary=True)

        query = """
            SELECT
                id,
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
                result,
                created_at,
                updated_at
            FROM students
            WHERE roll_number = %s
        """

        cursor.execute(query, (roll_number,))
        student = cursor.fetchone()

        if student is None:
            print("\nStudent not found.")
            return

        print("\nStudent Found!")
        print("-" * 50)
        print(f"Student ID  : {student['id']}")
        print(f"Name        : {student['student_name']}")
        print(f"Roll Number : {student['roll_number']}")
        print(f"Course      : {student['course']}")
        print("-" * 50)
        print(f"Physics     : {student['physics']}")
        print(f"Chemistry   : {student['chemistry']}")
        print(f"Mathematics : {student['mathematics']}")
        print(f"English     : {student['english']}")
        print(f"Computer    : {student['computer']}")
        print("-" * 50)
        print(f"Total       : {student['total']}")
        print(f"Percentage  : {student['percentage']}%")
        print(f"Grade       : {student['grade']}")
        print(f"Result      : {student['result']}")
        print("-" * 50)

    except Exception as error:
        print(f"Error while searching for student: {error}")

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()