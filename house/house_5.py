# using | instead or or

# using match with | 

name = input("What's your name? ")

match name: 
    case "Harry" | "Hermione" |  "Ron" : 
        print("Gryffindor!")
    case "Draco":
        print("Slytherine")
    case _:
        print("Who? ")