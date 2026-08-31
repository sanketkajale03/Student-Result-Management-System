import os

import mysql.connector
from dotenv import load_dotenv
from mysql.connector import Error


load_dotenv()


def test_connection():
    """Test the connection to the MySQL server."""
    connection = None
    cursor = None

    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT", "3306")),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
        )

        if connection.is_connected():
            print("MySQL connection successful!")

            cursor = connection.cursor()
            cursor.execute("SELECT VERSION()")

            version = cursor.fetchone()

            print(f"MySQL Server Version: {version[0]}")

    except Error as error:
        print(f"MySQL connection failed: {error}")

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")


if __name__ == "__main__":
    test_connection()