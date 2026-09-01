from database.database import get_connection


def display_students():
    """Display all students from the database."""

    print("\n" + "=" * 100)
    print(" " * 35 + "ALL STUDENTS")
    print("=" * 100)

    connection = None
    cursor = None

    try:
        connection = get_connection()

        if connection is None:
            print("Database connection failed.")
            return

        cursor = connection.cursor(dictionary=True)

        query = """
        SELECT
            id,
            student_name,
            roll_number,
            course,
            total,
            percentage,
            grade,
            result
        FROM students
        ORDER BY id;
        """

        cursor.execute(query)
        students = cursor.fetchall()

        if not students:
            print("\nNo student records found.")
            return

        print(
            f"{'ID':<5}"
            f"{'Name':<25}"
            f"{'Roll No':<15}"
            f"{'Course':<25}"
            f"{'Total':<10}"
            f"{'%':<10}"
            f"{'Grade':<8}"
            f"{'Result':<10}"
        )

        print("-" * 100)

        for student in students:
            print(
                f"{student['id']:<5}"
                f"{student['student_name']:<25}"
                f"{student['roll_number']:<15}"
                f"{student['course']:<25}"
                f"{student['total']:<10}"
                f"{student['percentage']:<10}"
                f"{student['grade']:<8}"
                f"{student['result']:<10}"
            )

        print("=" * 100)

    except Exception as error:
        print(f"Error: {error}")

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()