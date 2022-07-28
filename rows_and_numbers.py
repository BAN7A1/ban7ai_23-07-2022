#1
name_user = input('What is your name? ')
print(f'Hi {name_user}. What is your name!')

#2
number_input = float(input('Enter a fractional number: '))
print(f'You entered this number: int({number_input})')
print(f'Integer from user: {int(number_input)}')
print(f'ТHere is the output of the 4th power of the integer entered by the user: {int(number_input) ** 4}')
print(f'Outputting the square root of the entered integer: {int(number_input) ** 0.5}')
print(f'Output of the remainder from the division of the entered number: {int(number_input) // 2}')

#3
def mult_two(a: int, b: int) -> int:
    first_input = int(input('Enter the first number: '))
    second_input = int(input('Enter the second number: '))
    multiplication_of_numbers = first_input * second_input
    return multiplication_of_numbers

print('Example')
print(f'The product of two numbers is: {mult_two(1, 2)}')
