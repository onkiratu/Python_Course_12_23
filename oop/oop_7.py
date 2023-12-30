class Customer:
    def __init__(self, name, membership_type):
        self.name = name 
        self.membership_type = membership_type

customers = [Customer("Caleb", "Gold"),
             Customer("Brad", "Bronze") ]

print(customers[0].name)