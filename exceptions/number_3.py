try:
    x = int(input("Enter x: "))
except ValueError: 
    print("x is not an integer")
else: 
    print(f"x is {x}")
