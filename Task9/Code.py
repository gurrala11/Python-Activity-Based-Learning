seats = [[None, None], [None, None]]
registered = ["A1", "A2", "A3"]
entered = []

for ticket in ["A1", "A2", "A1", "X1"]:
    if ticket not in registered:
        print(ticket, "Invalid")
    elif ticket in entered:
        print(ticket, "Duplicate")
    else:
        entered.append(ticket)
        for row in seats:
            if None in row:
                row[row.index(None)] = ticket
                print(ticket, "Seat assigned")
                break

print("Available seats:", sum(r.count(None) for r in seats))
