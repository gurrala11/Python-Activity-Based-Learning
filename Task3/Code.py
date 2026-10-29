fine = {"Car": 1000, "Bike": 500, "Truck": 2000}

v = input("Vehicle (Car/Bike/Truck): ")
o = input("Offence (Normal/Serious): ")
r = input("Repeat (yes/no): ")

penalty = fine.get(v, 0)
if r == "yes":
    penalty *= 2

print("Penalty: ₹", penalty)
print("Disqualification:", "Yes" if o == "Serious" else "No")
