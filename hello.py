# Ask user for their name
# name = input("What's your name? ")

# Remove white space from string 
# name = name.strip()

# Capitalize name
# name = name.capitalize()

# Title case # 
# name = name.title()

#Say hello to user
# print("Hello, ", end="") # Modifying end =
# print(name)

# Comma Separator 
# print("Hello,", name) 

# Concatenation 
# print("Hello, " + name)

# Chain commamnds
# Remove white space from string  and Capitalize
# name = name.strip().title()

# Combine into one string 
# name = input("What's your name? ").strip().title()

# Multiline comment """     """

""""
ddddd
"""

# Escape character \
# print("Hello, \"friend\" ") 

# Using curly bracket around the variable name { }
# Using f-string, format strings 
# print(f"Hello,  {name}")

# Split user's name into first and last name
# first, last = name.split(" ")

# Say hello to user
# print(f"Hello, {first}")
# print(f"Hello, {last}")

# User defined functions
# def hello(): 
  #  print("hello")

# name = input("What's your name?")
# hello() 
# print(name)

# Put parameters in a function 
# def hello(to): 
#     print("hello," , to)

#name = input("What's your name?")
# hello(name) 

# Version 2
# def hello(to="World"): 
#     print("hello," , to)

# hello()
# name = input("What's your name?")
# hello(name) 

# Using main function 
def main():
    name = input("What's your name?")
    hello(name)

def hello(to="World"):
    print("hello,",to)


main()