# looping through a dictionary
# {keys, left: values, right}
# dictionaries use strings to index
students = {
    "Hermione" : "Gryffindor",
    "Harry" : "Gyffindor",
    "Ron" : "Gryffindor",
    "Draco" : "Slytherin",
}

for student in students: #iterate throufgh keys
    print(student,students[student], sep=": ")