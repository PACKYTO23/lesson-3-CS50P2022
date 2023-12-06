# # # Lists

# students = ["Hermoine", "Harry", "Ron"]

# for student in students:
#     print(student)

# for i in range(len(students)):
#     print(i + 1, students[i])

# # # Dictionaries

# students = ["Hermoine", "Harry", "Ron", "Draco"]
# houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

# students = {
#     "Hermoine": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin",
# }

# print(students["Hermoine"])
# print(students["Harry"])
# print(students["Ron"])
# print(students["Draco"])

# for student in students:
#     print(student, students[student], sep=", ")

# # # Dictionaries nested List

students = [
    {"name": "Hermoine", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
