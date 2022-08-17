first_input = input('Enter first text: ')
second_input = input('Enter second text: ')

first_set = {i for i in first_input if i.isalpha()}
second_set = {i for i in second_input if i.isalpha()}

print(f'In the text there are such letters: {first_set & second_set}')
#############################################

first_set_1 = {i for i in first_input if i.isdigit()}
first_set_2 = {i for i in second_input if i.isdigit()}

len_number_1 = first_set_1 - first_set_2
len_number_2 = first_set_2 - first_set_1

print(f'In your entered text such numbers: {len_number_1 - len_number_2}')
############################################
