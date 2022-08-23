new_dict = {element: chr(element) for element in range(6)}
print(new_dict)
##############################
try:
	user_input = input('Enter your message text: ')
	while user_input.isalpha():
		break
	else:
		print('This version does not include numbers!')
		sys.exit()
	password_input = int(input('Enter an integer from 1 to 26: '))
	new_list = []
	eng_dict = {
    	'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,
    	'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
    	'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
    	'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
    	'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
    	'z': 26
	}
	for x in user_input:
		if x in eng_dict:
			new_index = eng_dict[x] + password_input
			new_list.append(list(eng_dict.keys())[list(eng_dict.values()).index(new_index)])
	print(''.join(new_list))
except (ValueError, NameError):
	print('You entered an invalid character.Check if the set is correct!')
