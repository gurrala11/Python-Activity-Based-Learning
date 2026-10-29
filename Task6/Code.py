
cap = int(input("Bus capacity: "))
n = int(input("Number of stops: "))
p = 0

for i in range(n):
    b = int(input("Boarding: "))
    a = int(input("Alighting: "))
    p = max(0, p - a) + b
    print("Passengers:", p)
    print("Capacity exceeded" if p > cap else "Within capacity")

