def create_username(first: str, last: str) -> str:
    return f'{first[:4]}{last[:4]}'

username = create_username(last='hart', first='gareth')

print(username)