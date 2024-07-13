def calculate_cgpa(grades, credits):
    total_points = 0
    total_credits = 0

    for grade, credit in zip(grades, credits):
        total_points += grade * credit
        total_credits += credit

    if total_credits == 0:
        return 0

    cgpa = total_points / total_credits
    return cgpa


def main():
    num_subjects = int(input("Enter the number of subjects: "))

    grades = []
    credits = []

    for i in range(num_subjects):
        grade = float(input(f"Enter the grade for subject {i + 1}: "))
        credit = float(input(f"Enter the credit for subject {i + 1}: "))
        grades.append(grade)
        credits.append(credit)

    cgpa = calculate_cgpa(grades, credits)
    print(f"Your CGPA is: {cgpa:.2f}")


if __name__ == "__main__":
    main()
