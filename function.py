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
def date_time():
	pass
##################################################
sum_list = [2, 10, 24, 21, 50, 125]

def sum_for(x):
	return sum(i for i in x)
print(f'The sum of numbers through for is equal to: {sum_for(sum_list)}')

def sum_while(x):
	a = 0
	while a < len(x):
		b = sum(x)
		a += 1
	return b
print(f'The sum of numbers through while is equal to: {sum_while(sum_list)}')

