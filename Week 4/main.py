"""Entry point: coordinates the Student Marks application.

Responsibility: collect input (INPUT), ask the other modules to validate,
calculate and display, and pass data between them. It contains no
validation rules, formulas, grading rules or output formatting.
"""

from validation import validate_mark, INVALID_MARK_MESSAGE
from calculations import calculate_total, calculate_average, calculate_grade
from display import display_result

NUMBER_OF_SUBJECTS = 3


def read_valid_mark(subject_number):
    """Ask for a mark until validate_mark accepts it, then return it."""
    mark = float(input(f"Enter marks for subject {subject_number}: "))

    while not validate_mark(mark):
        print(INVALID_MARK_MESSAGE)
        mark = float(input(f"Enter marks for subject {subject_number}: "))

    return mark


def main():
    name = input("Enter student name: ")
    marks = []

    for i in range(NUMBER_OF_SUBJECTS):
        marks.append(read_valid_mark(i + 1))

    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = calculate_grade(average)

    display_result(name, total, average, grade)


if __name__ == "__main__":
    main()
