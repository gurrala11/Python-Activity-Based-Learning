rooms = [["Ram", "Reserved", None],
         ["Sita", "Ram", None]]

students = [s for room in rooms for s in room
            if s not in (None, "Reserved")]

print("Duplicate:", len(students) != len(set(students)))
print("Vacant seats:", sum(s is None for r in rooms for s in r))
