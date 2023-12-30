# x = input("What's x? ")
# y = input("What's y? ") 
# z = int(x) + int(y)
# print(z)

# Nested function 
# x = int(input("What's x? "))
# y = int(input("What's y? ") )
# python print(x + y)

# Float
# x = float(input("What's x? "))
# y = float(input("What's y? ") )
# print(x + y)

# Rounding 
# x = float(input("What's x? "))
# y = float(input("What's y? ") )

# z = round(x + y)
# print(z)
# print(f"{z:,}")

# Division
# x = float(input("What's x? "))
# y = float(input("What's y? ") )
# z = round(x/y, 2)
# print(z)

# Formatted rounding 
# x = float(input("What's x? "))
# y = float(input("What's y? ") )
# z = (x/y)
# print(f"{z:.2f}")

# Integers 
# User defined function (squaring)
# def main():
#    x = int(input("Enter x: "))
#    print("x squared is", square(x) )

# def square(n): 
   # return n*n
#    return n**2

# main()


# Floating points
def main():
    a = float(input("Enter a: "))
    print("a squared is", square(a) )

def square(n): 
    #return n*n
    #return n**2
    return round(pow(n,2))

main()