# with try and except

try:
    x = int(input("Enter x: "))
    print(f"x is {x}")
except ValueError: 
    print("x is not an integer")