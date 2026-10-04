"""Calculations and business rules for student marks.

Responsibility: turn raw marks into total, average and grade.
Pure functions only: no input(), no print(), no validation.
"""


def calculate_total(marks):
    """Return the sum of all marks."""
    return sum(marks)


def calculate_average(marks):
    """Return the average of the marks."""
    return calculate_total(marks) / len(marks)


def calculate_grade(average):
    """Return the letter grade for an average (grading business rule)."""
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"
