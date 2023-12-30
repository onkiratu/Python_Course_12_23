import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def is_valid_url(url):
    pattern = r'^(https?|ftp):\/\/[^\s/$.?#].[^\s]*$'
    return bool(re.match(pattern, url))

def is_valid_ip(ip):
    pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    return bool(re.match(pattern, ip))

def is_valid_date(date):
    pattern = r'^(0[1-9]|1[0-2])\/(0[1-9]|[12][0-9]|3[01])\/\d{4}$'
    return bool(re.match(pattern, date))

def is_valid_time(time):
    pattern = r'^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$'
    return bool(re.match(pattern, time))

def is_valid_username(username):
    pattern = r'^[a-zA-Z0-9_]{3,16}$'
    return bool(re.match(pattern, username))

def is_valid_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    return bool(re.match(pattern, password))

def is_valid_html(html):
    pattern = r'<([a-z]+) *[^/]*?>.*?<\/\1>'
    return bool(re.search(pattern, html))

def is_valid_credit_card(card_number):
    pattern = r'^\d{4}-?\d{4}-?\d{4}-?\d{4}$'
    return bool(re.match(pattern, card_number))

def is_valid_zip_code(zip_code):
    pattern = r'^\d{5}(-\d{4})?$'
    return bool(re.match(pattern, zip_code))

# Example usage:
email = "example@email.com"
print(f"Is valid email? {is_valid_email(email)}")

url = "https://www.example.com"
print(f"Is valid URL? {is_valid_url(url)}")

ip = "192.168.1.1"
print(f"Is valid IP address? {is_valid_ip(ip)}")

date = "12/31/2023"
print(f"Is valid date? {is_valid_date(date)}")

time = "15:30:00"
print(f"Is valid time? {is_valid_time(time)}")

username = "user_name123"
print(f"Is valid username? {is_valid_username(username)}")

password = "StrongPwd@123"
print(f"Is valid password? {is_valid_password(password)}")

html = "<div>Hello, World!</div>"
print(f"Contains valid HTML? {is_valid_html(html)}")

credit_card = "1234-5678-9012-3456"
print(f"Is valid credit card number? {is_valid_credit_card(credit_card)}")

zip_code = "12345-6789"
print(f"Is valid ZIP code? {is_valid_zip_code(zip_code)}")
