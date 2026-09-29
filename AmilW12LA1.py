classrecord = {
    "Liza": {
        "StudID": "S001",
        "Grade": [90, 85, 86, 82, 83, 90, 92]
    },
    "Jeremy": {
        "StudID": "S002",
        "Grade": [72, 75, 69, 80, 84, 75, 85]
    },
    "Artemis": {
        "StudID": "S003",
        "Grade": [58, 61, 69, 50, 63, 65, 51]
    }
}

search_name = input("Enter the student name to search: ").strip().title()

if search_name in classrecord:
    print(f"\nStudent '{search_name}' was FOUND!")

    student_id = classrecord[search_name]["StudID"]
    grades = classrecord[search_name]["Grade"]

    average = sum(grades) / len(grades)
    highest_grade = max(grades)
    lowest_grade = min(grades)

    intervention_status = ""
    for grade in grades:
        if grade < 60:
            intervention_status = " -> Candidate for intervention"
            break

    print(f"ID: {student_id}")
    print(f"Grades: {grades}")
    print(f"Average Grade: {average:.2f}{intervention_status}")
    print(f"Highest Grade: {highest_grade}")
    print(f"Lowest Grade: {lowest_grade}")

else:
    print(f"\nStudent '{search_name}' was NOT FOUND.")