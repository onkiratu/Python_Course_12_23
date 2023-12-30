name = input("What's your name? ").strip().lower()

if name == "harry".lower():
    print(f"{name.title()} is in Gryffindor!")
elif name == "hermione".lower():
    print(f"{name.title()} is in Gryffindor!")
elif name == "ron".lower():
    print(f"{name.title()} is in Gryffindor!")
elif name == "draco".lower():
    print(f"{name.title()} is in Slytherine")
else:
    print(f"Who is {name.title()}?")
