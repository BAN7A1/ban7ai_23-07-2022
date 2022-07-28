name_user = input("Enter your name: ")

print(f'Hello i removed all the spaces in your typing {name_user.strip()}')

print(f'Hello now the first letter in your name is capitalized {name_user.capitalize()}')

print(f'{name_user.capitalize()} in your name {len(name_user)} letters')

print(f'Your inventory name will be {name_user[::-1]}')
