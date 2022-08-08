user_input = input()
#####################
print(f'{user_input.upper()}')
####################
space = ' '

for index, letter in enumerate(user_input):
    if letter == space:
        print(f'space is under {index} index')
####################
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
total = 0
for i in user_input:
    if i in vowels:
        print(i)
####################
num = ""

for i in user_input:
    if i.isdigit():
        num = num + i
    if len(num) >= 3:
        print('Script terminated')
        break
else:
    print('The script worked correctly')
####################
for i in range(3):
    print(user_input)
