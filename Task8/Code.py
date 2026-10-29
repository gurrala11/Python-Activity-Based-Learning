n = int(input("Number of students: "))

for i in range(n):
    name = input("Name: ")
    fee = int(input("Fee pending: "))
    att = int(input("Attendance: "))
    marks = int(input("Internal marks: "))

    reasons = []
    if fee > 0:
        reasons.append("Fee pending")
    if att < 75:
        reasons.append("Low attendance")
    if marks < 20:
        reasons.append("Low marks")

    print(name, "Eligible" if not reasons else ", ".join(reasons))
