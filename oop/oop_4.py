# improvements on oop_3.py with 
# robust classes


class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherine"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house

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
