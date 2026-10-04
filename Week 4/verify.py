"""Part G - Verify.

Runs the original monolith and the modular main.py with the same scripted
input and checks that the output is identical. Run: python verify.py
"""

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent

# (description, scripted input lines)
CASES = [
    ("Normal marks: 75, 82, 68", ["Ali", "75", "82", "68"]),
    ("Boundary marks: 50, 60, 70 (avg 60 -> C)", ["Sara", "50", "60", "70"]),
    ("Boundary marks: 80, 80, 80 (avg 80 -> A)", ["Boundary80", "80", "80", "80"]),
    ("Boundary marks: 50, 50, 50 (avg 50 -> D)", ["Boundary50", "50", "50", "50"]),
    ("Boundary marks: 70, 70, 70 (avg 70 -> B)", ["Boundary70", "70", "70", "70"]),
    ("Boundary marks: 60, 60, 60 (avg 60 -> C)", ["Boundary60", "60", "60", "60"]),
    ("Invalid marks -5 and 105, then valid", ["Omar", "-5", "70", "105", "80", "90"]),
    ("Edge marks 0 and 100", ["Edge", "0", "100", "100"]),
    ("Second student, failing result", ["Hina", "30", "45", "20"]),
]


def run(script, lines):
    result = subprocess.run(
        [sys.executable, str(HERE / script)],
        input="\n".join(lines) + "\n",
        capture_output=True,
        text=True,
        cwd=HERE,
    )
    return result.stdout


def main():
    all_ok = True
    for description, lines in CASES:
        original = run("original_monolith.py", lines)
        modular = run("main.py", lines)
        same = original == modular
        all_ok = all_ok and same
        print("=" * 60)
        print(f"CASE: {description}  ->  {'PASS (identical)' if same else 'FAIL'}")
        print("-" * 60)
        print(modular)
    print("=" * 60)
    print("ALL CASES IDENTICAL" if all_ok else "SOME CASES DIFFER")
    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    main()
