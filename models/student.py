from services.calculate_result import calculate_result_details


class Student:
    """Represent a student and their academic result."""

    def __init__(
        self,
        student_name,
        roll_number,
        course,
        physics,
        chemistry,
        mathematics,
        english,
        computer,
        student_id=None,
        total=0.0,
        percentage=0.0,
        grade="",
        result="",
    ):
        self.student_id = student_id
        self.student_name = student_name
        self.roll_number = roll_number
        self.course = course

        self.physics = float(physics)
        self.chemistry = float(chemistry)
        self.mathematics = float(mathematics)
        self.english = float(english)
        self.computer = float(computer)

        self.total = float(total)
        self.percentage = float(percentage)
        self.grade = grade
        self.result = result

    def get_marks(self):
        """Return all subject marks as a list."""
        return [
            self.physics,
            self.chemistry,
            self.mathematics,
            self.english,
            self.computer,
        ]

    def calculate_result_details(self):
        """Calculate and update the student's result details."""
        details = calculate_result_details(self.get_marks())

        self.total = details["total"]
        self.percentage = details["percentage"]
        self.grade = details["grade"]
        self.result = details["result"]

        return details

    def to_dict(self):
        """Convert the student object into a dictionary."""
        return {
            "id": self.student_id,
            "student_name": self.student_name,
            "roll_number": self.roll_number,
            "course": self.course,
            "physics": self.physics,
            "chemistry": self.chemistry,
            "mathematics": self.mathematics,
            "english": self.english,
            "computer": self.computer,
            "total": self.total,
            "percentage": self.percentage,
            "grade": self.grade,
            "result": self.result,
        }

    def __str__(self):
        """Return a readable representation of the student."""
        return (
            f"Student("
            f"id={self.student_id}, "
            f"name='{self.student_name}', "
            f"roll_number='{self.roll_number}', "
            f"course='{self.course}', "
            f"total={self.total:.2f}, "
            f"percentage={self.percentage:.2f}, "
            f"grade='{self.grade}', "
            f"result='{self.result}'"
            f")"
        )