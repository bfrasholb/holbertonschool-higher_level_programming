#!/usr/bin/python3


students = [
    ("Sam", 24),
    ("Zac", 24),
    ("Sean", 23),
    ("Venghour", 28),
    ("Lachlan", 28),
]
res = []
res = tuple(sorted([element[0] for element in students if element[1] >= 25]))
# old = list(filter(lambda student: student[1] >= 25, students))
# old.sort(key=lambda s: s[0])
# print(tuple((student[0] for student in old)))

# res = []
# for element in range(len(students)):
#    if students[element][1] >= 25:
#        res.append(students[element][0])
print(res)
#    print(tuple(sorted(students)))
