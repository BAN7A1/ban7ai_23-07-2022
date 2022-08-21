2#new_dict = {element: chr(element) for element in range(5)}
#print(new_dict)
##############################
one_input = input('Enter your message text: ')
password_input = int(input('Enter an integer from 1 to 26: '))
eng_dict = {'a': 1, 'b': 2, 'c': 3, }
a = {i: ascii(i) for i in one_input}
print(a)
