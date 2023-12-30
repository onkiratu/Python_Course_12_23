names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())
        
for name in sorted(names): # use sorted(names, reverse=True): for z-a
    print(f"hello, {name}")