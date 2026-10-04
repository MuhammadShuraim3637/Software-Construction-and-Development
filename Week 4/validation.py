"""Validation rules for student marks.

Responsibility: decide whether a mark is acceptable and own the message
shown when it is not. Nothing here reads input, calculates, or prints.
"""

MIN_MARK = 0
MAX_MARK = 100
INVALID_MARK_MESSAGE = "Invalid marks. Enter 0-100."


def validate_mark(mark):
    """Return True if mark is within MIN_MARK..MAX_MARK (inclusive)."""
    return MIN_MARK <= mark <= MAX_MARK
