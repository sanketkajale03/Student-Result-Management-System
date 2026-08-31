def validate_name(name):
    """Validate a student's name."""
    name = name.strip()

    if not name:
        return False, "Student name cannot be empty."

    if len(name) < 2:
        return False, "Student name must contain at least 2 characters."

    if not all(char.isalpha() or char.isspace() for char in name):
        return False, "Student name can contain only letters and spaces."

    return True, name


def validate_roll_number(roll_number):
    """Validate a student's roll number."""
    roll_number = roll_number.strip()

    if not roll_number:
        return False, "Roll number cannot be empty."

    if len(roll_number) > 20:
        return False, "Roll number cannot exceed 20 characters."

    return True, roll_number


def validate_course(course):
    """Validate the course name."""
    course = course.strip()

    if not course:
        return False, "Course cannot be empty."

    if len(course) < 2:
        return False, "Course must contain at least 2 characters."

    return True, course


def validate_marks(marks):
    """Validate marks for a subject."""
    try:
        marks = float(marks)
    except ValueError:
        return False, "Marks must be a valid number."

    if marks < 0 or marks > 100:
        return False, "Marks must be between 0 and 100."

    return True, marks