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
a_set = {1, 52, 224, 12, 9}
b_set = {'hi', 52, 7, 2, 1}
c_set = {2, 45, 'hello'}

a_set.update(b_set, c_set)
print(a_set)
############################################
q_set = {1, 56, 2, 14}
w_set = {43, 4, 1, 12, 2}
e_set = {5, 15, 2, 9, 56}

q_set |= w_set |= e_set
print(q_set)
