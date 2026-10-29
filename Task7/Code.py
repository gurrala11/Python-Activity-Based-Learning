
seats = [[101, 102], [103, 101]]
reserved = [(0, 1)]
seen = []

for i, row in enumerate(seats):
    for j, s in enumerate(row):
        if (i, j) in reserved:
            print(s, "Reserved seat occupied")
        elif s == 0:
            print("Empty seat")
        elif s < 0:
            print("Invalid allocation")
        elif s in seen:
            print(s, "Duplicate roll number")
        else:
            seen.append(s)
            print(s, "Valid")

