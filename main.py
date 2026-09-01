from services.add_student import add_student
from services.search_student import search_student
from services.update_student import update_student
from services.delete_student import delete_student
from services.display_students import display_students


def display_menu():
    print("\n" + "=" * 60)
    print("        STUDENT RESULT MANAGEMENT SYSTEM")
    print("=" * 60)
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display All Students")
    print("6. Exit")
    print("=" * 60)


def main():
    while True:
        display_menu()

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            search_student()

        elif choice == "3":
            update_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            display_students()

        elif choice == "6":
            print("\nThank you for using Student Result Management System.")
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()