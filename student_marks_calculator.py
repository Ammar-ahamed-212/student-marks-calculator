# Student Marks Calculator with Grades

def get_grade(mark):
    if mark >= 90:
        return "A+"
    elif mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 50:
        return "D"
    else:
        return "F"


num_subjects = int(input("Enter number of subjects: "))

if num_subjects <= 0:
    print("Number of subjects must be greater than 0.")
else:

    subjects = []
    marks = []

    for i in range(num_subjects):
        name = input(f"Enter name of subject {i + 1}: ")
        mark = float(input(f"Enter marks for {name}: "))

        subjects.append(name)
        marks.append(mark)

    total = sum(marks)
    average = total / num_subjects

    highest = max(marks)
    lowest = min(marks)

    highest_subject = subjects[marks.index(highest)]
    lowest_subject = subjects[marks.index(lowest)]

    print("\n----- Subject Grades -----")

    for subject, mark in zip(subjects, marks):
        print(f"{subject:<15} {mark:>6} -> Grade {get_grade(mark)}")

    print("\n----- Result -----")

    print(f"Total Marks   : {total}")
    print(f"Average Marks : {average:.2f}")
    print(f"Overall Grade : {get_grade(average)}")
    print(f"Highest Marks : {highest} in {highest_subject}")
    print(f"Lowest Marks  : {lowest} in {lowest_subject}")