def calculate_total(marks):
    """Calculate the total marks for all subjects."""
    return sum(marks)


def calculate_percentage(total, number_of_subjects=5):
    """Calculate percentage from total marks."""
    if number_of_subjects <= 0:
        raise ValueError("Number of subjects must be greater than zero.")

    return total / number_of_subjects


def calculate_grade(percentage):
    """Determine the grade from the percentage."""
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def calculate_result(marks):
    """Determine whether the student passed or failed."""
    return "PASS" if all(mark >= 40 for mark in marks) else "FAIL"


def calculate_result_details(marks):
    """Calculate complete result details."""
    total = calculate_total(marks)
    percentage = calculate_percentage(total)
    grade = calculate_grade(percentage)
    result = calculate_result(marks)

    return {
        "total": total,
        "percentage": percentage,
        "grade": grade,
        "result": result,
    }