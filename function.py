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
	print('You ent4ered the wrong value!')
##################################################
intervals = (
	('weeks', 604800),('days', 86400),
	('hours', 3600), ('minutes', 60),
	('seconds', 1),
	)
def data_time(seconds, granularity = 2 ):
	result = []
	for name, count in intervals:
		value = seconds // count
		if value:
			seconds -= value * count
			if value == 1:
				name = name.rstrip('s')
			result.append("{} {}".format(value, name))
	return ': '.join(result[:granularity])
print(f'{data_time(3213213213,3213)}')
##################################################
sum_list = [2, 10, 24, 21, 50, 125]

def sum_for(x):
	null = 0
	for i in sum_list:
		null = null + i
	return null
print(f'The sum of numbers through for is equal to: {sum_for(sum_list)}')

def sum_while(x):
	a = 0
	while a < len(x):
		b = sum(x)
		a += 1
	return b
print(f'The sum of numbers through while is equal to: {sum_while(sum_list)}')

def sum_rek(x):
	if len(x) == 1:
		return x[0]
	else:
		return x[0] + sum_rek(x[1:])
print(f'The sum of numbers through recursion is equal to: {sum_rek(sum_list)}')
################################################
a = int(input('Enter your number: '))
def fibonacci(i):
    if i <= 1:
        return 0
    elif i == 2:
        return 1
    return fibonacci(i - 1) + fibonacci(i - 2)

print(f'Sequence number is: {fibonacci(a)}')
##############################################
def decorator1(func):
	def buter():
		print('помідор')
		func()
		print('хліб')
	return buter
def decorator2(func2):
	def butter():
		func2()
		print('сир')
	return butter

@decorator1
@decorator2

def dsadsa():
	print('м\'ясо')
dsadsa()

#I know that the code is with a curve decorator. 
#I'm still trying to understand this topic ... it's very hard for me
