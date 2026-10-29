key = input("Answer key: ").split()
ans = input("Student answers: ").split()

c = w = u = 0
for k, a in zip(key, ans):
    if a == "-":
        u += 1
    elif a == k:
        c += 1
    else:
        w += 1

score = c - w * 0.25
print("Correct:", c, "Wrong:", w, "Unanswered:", u)
print("Final Score:", score)
