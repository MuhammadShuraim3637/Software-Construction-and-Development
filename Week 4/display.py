"""Presentation of the student result.

Responsibility: format and show a result. It receives finished values
and never calculates or validates anything.
"""


def display_result(name, total, average, grade):
    """Print the student result to the console."""
    print("\nStudent Result")
    print("----------------")
    print("Name:", name)
    print("Total:", total)
    print("Average:", average)
    print("Grade:", grade)
