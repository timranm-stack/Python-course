# Improved Exam Eligibility Checker with Validation

try:
    total_days = int(input("Enter the total number of working days: "))
    absent_days = int(input("Enter the total number of days absent: "))

    if total_days < 0 or absent_days < 0:
        print("Days cannot be negative.")
    elif absent_days > total_days:
        print("Absent days cannot exceed total working days.")
    else:
        attended_days = total_days - absent_days
        percentage = (attended_days / total_days) * 100

        print(f"\nAttendance Percentage: {percentage:.2f}%")

        if percentage < 75:
            print("You are NOT eligible to sit in the exam.")
        else:
            print("You ARE eligible to sit in the exam.")

except ValueError:
    print("Please enter valid integer values.")
