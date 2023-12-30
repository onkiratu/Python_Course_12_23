# with getters and setters 

# improvements on oop_4.py with 
# getters and setters

class Student:
    def __init__(self, name, house):
        self._name = None  # private attribute
        self._house = None  # private attribute
        self.name = name
        self.house = house

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Missing name")
        self._name = value

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, value):
        valid_houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
        if value not in valid_houses:
            raise ValueError("Invalid House")
        self._house = value

    def __str__(self):
        return f"{self.name} from {self.house}"

def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main()
