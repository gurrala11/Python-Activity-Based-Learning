marks = list(map(int, input("Enter 3 marks: ").split()))

for i in range(3):
    if marks[i] == 34:
        marks[i] = min(35, marks[i] + 1)

total = sum(marks)

if min(marks) < 35:
    result = "Fail"
elif total >= 240:
    result = "Distinction"
elif total >= 180:
    result = "First Class"
else:
    result = "Pass"

print("Marks:", marks)
print("Total:", total, "/ 300")
print("Result:", result)
