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

        self.physics = physics
        self.chemistry = chemistry
        self.mathematics = mathematics
        self.english = english
        self.computer = computer

        self.total = total
        self.percentage = percentage
        self.grade = grade
        self.result = result

    def calculate_total(self):
        """Calculate the total marks."""
        self.total = (
            self.physics
            + self.chemistry
            + self.mathematics
            + self.english
            + self.computer
        )

        return self.total

    def calculate_percentage(self):
        """Calculate the percentage based on five subjects."""
        self.percentage = self.calculate_total() / 5

        return self.percentage

    def calculate_grade(self):
        """Calculate the grade based on the percentage."""
        percentage = self.calculate_percentage()

        if percentage >= 90:
            self.grade = "A+"
        elif percentage >= 80:
            self.grade = "A"
        elif percentage >= 70:
            self.grade = "B"
        elif percentage >= 60:
            self.grade = "C"
        elif percentage >= 50:
            self.grade = "D"
        else:
            self.grade = "F"

        return self.grade

    def calculate_result(self):
        """Determine whether the student passed or failed."""
        subjects = [
            self.physics,
            self.chemistry,
            self.mathematics,
            self.english,
            self.computer,
        ]

        if all(mark >= 40 for mark in subjects):
            self.result = "PASS"
        else:
            self.result = "FAIL"

        return self.result

    def calculate_result_details(self):
        """Calculate total, percentage, grade, and result."""
        self.calculate_total()
        self.calculate_percentage()
        self.calculate_grade()
        self.calculate_result()

        return {
            "total": self.total,
            "percentage": self.percentage,
            "grade": self.grade,
            "result": self.result,
        }

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
            f"total={self.total}, "
            f"percentage={self.percentage:.2f}, "
            f"grade='{self.grade}', "
            f"result='{self.result}'"
            f")"
        )