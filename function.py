def number_sub(start, end):
	if start < end:
		end, start = start, end
		print('We swapped the values for the correct output of the answer!')
	return start - end
try:
	start_input = int(input('Enter the first value: '))
	end_input = int(input('Enter the second value: '))
	print(f'The response of your operation is: {number_sub(start_input, end_input)}')
except ValueError:
	print('You entered the wrong value!')
##################################################
def date_time()
	pass
