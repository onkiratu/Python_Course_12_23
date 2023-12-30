# using match

name = input("What's your name? ")

match name: 
    case "Harry":
        print("Gryffindor!")
    case "Hermione": 
        print("Gryffindor!")
    case "Ron" :
        print("Gryffindor!")
    case "Draco":
        print("Slytherine")
    case _:
        print("Who? ")