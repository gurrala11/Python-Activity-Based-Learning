records = input("Enter records: ").split(";")
seen = set()

for r in records:
    f = r.split(",")
    if len(f) != 3 or len(f[0]) != 4 or not f[1].isalpha():
        print(r, "- Invalid format")
    elif f[0] in seen:
        print(r, "- Duplicate ID")
    else:
        seen.add(f[0])
        print("Valid:", f[0], f[1], f[2])
