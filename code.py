students = []
while True:
    student_count = input("Enter student count: ")
    if student_count.isdigit():
        student_count = int(student_count)
        break
    else:
        print("Please enter numbers")
for i in range(student_count):
    student_name = input("Enter student name: ")
    while True:
        student_score = input(f"Enter {student_name} score: ")
        if student_score.isdigit():
            student_score = int(student_score)
            break
        else:
            print("Please enter numbers")
    students.append({"student_name": student_name, "student_score": student_score})

high_student_score = max(student["student_score"] for student in students)
low_student_score = min(student["student_score"] for student in students)
average_student_score = sum(student["student_score"] for student in students) / student_count


high_student_name = [student["student_name"] for student in students if student["student_score"] == high_student_score]
low_student_name = [student["student_name"] for student in students if student["student_score"] == low_student_score]

print("Highest score: ", high_student_score, ", ".join(high_student_name))
print("Lowest score: ", low_student_score, ", ".join(low_student_name))
print(f"Average score: {average_student_score:.2f}")
