# using '.edu' to validate email

import re

email = input("Enter your email address: ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
    
else: 
    print("Invalid")
    