# username

def create_username(first, last):
    return f'{first[:4]}{last[:4]}'

first = str(input("First Name:"))
last = str(input("Last:"))

username = create_username(first, last).lower()

print(username)



