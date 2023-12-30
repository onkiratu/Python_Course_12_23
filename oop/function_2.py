# using tuples _ immutable_ cannot be changed.
""" In Python, a tuple is a collection data 
type that is ordered and immutable. 
It is used to store an ordered sequence of 
elements. Tuples are similar to lists, 
but with a key difference: once a tuple is 
created, its elements cannot be modified, 
added, or removed. This immutability makes 
tuples suitable for situations where the 
data should remain constant throughout the 
program. """


def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house) 
    # You can use square brackets 
    # instead of a tuple to 
    # make it an editable list


if __name__ == "__main__":
    main()
