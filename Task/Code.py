
n = int(input("Number of students: "))
students = []

for i in range(n):
    name = input("Name: ")
    marks = float(input("Aggregate marks: "))
    subject = float(input("Minimum subject score: "))
    attendance = float(input("Attendance %: "))
    income = float(input("Family income: "))

    if marks >= 75 and subject >= 40 and attendance >= 75 and income <= 200000:
        students.append((name, marks, attendance))

students.sort(key=lambda x: (-x[1], -x[2]))

print("\nScholarship Ranking:")
for rank, s in enumerate(students, 1):
    print(rank, s[0], "Marks:", s[1], "Attendance:", s[2])

if not students:
    print("No eligible students.")

