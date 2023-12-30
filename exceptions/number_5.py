def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return  int(input("Enter x: "))
        except ValueError: 
            pass

main()