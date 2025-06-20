# rough practice 2:-

# Students=["Harry", "Ron", "Hermione"]
'''
for _ in Students:
    print(_)
'''

# len() function
'''
for i in range(len(Students)):
    print(i+1, Students[i])
'''

# DICT:
'''
students={
    "Harry":"Gryffindor",
    "Hermione":"Gryffindor",
    "Ron":"Gryffindor",
    "Draco":"Slytherin",
}
print(students)
for i in students:
    print(i, students[i], sep=(" - "))
'''

# List of dictionaries:
# None keyword

Students=[
    {"name":"Hermione", "house":"Gryffindor", "patronus":"Otter"},
    {"name":"Harry", "house":"Gryffindor", "patronus":"Stag"},
    {"name":"Ron", "house":"Gryffindor", "patronus":"Jack Russel terrier"},
    {"name":"Draco", "house":"Slytherin", "patronus":None}
]
for i in Students:
    print(i["name"], i["house"], i["patronus"], sep=", ")