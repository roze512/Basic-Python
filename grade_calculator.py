def calculate_grade(marks):
    if marks > 90:
        return "A"
    elif marks > 80:
        return "B"
    else:
        return "C"

print(calculate_grade(95))
print(calculate_grade(85))
print(calculate_grade(60))
