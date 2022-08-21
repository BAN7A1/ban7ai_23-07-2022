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

q_set |= w_set
print(q_set)
#------------------------------------------------

e_set = {5, 4, 2, 11}
r_set = {4, 3, 25, 5}

e_set &= r_set
print(e_set)
#------------------------------------------------

t_set = {26, 'hi', 2, 3.4}
y_set = {2, 'hi', 2.5, 2}

t_set -= y_set
print(t_set)
#-----------------------------------------------

z_set = {'hello', 0, 24}
x_set = {0, 'hi', 'hello', 2, 44}

z_set ^= x_set
print(z_set)