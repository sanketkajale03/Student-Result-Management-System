def display_menu():
    """Display the main application menu."""
    print("\n" + "=" * 50)
    print("       STUDENT RESULT MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display All Students")
    print("6. Exit")
    print("=" * 50)


def get_menu_choice():
    """Get and validate the user's menu choice."""
    while True:
        choice = input("Enter your choice (1-6): ").strip()

        if choice in {"1", "2", "3", "4", "5", "6"}:
            return int(choice)

        print("Error: Please enter a number between 1 and 6.")