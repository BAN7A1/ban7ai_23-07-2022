
first_comparison = 3 != 5
print(first_comparison)

################################

equals = 5 == 5
more_equal = 5 >= 5
less_equal = 5 <= 5
and_comparison = 5 and 5
or_comparison = 5 or 5

print(f'{equals=} ; {more_equal=} ; {less_equal=} ; {bool(and_comparison)} ; {bool(or_comparison)}' )

################################

one = 3 < 4 > False
two = 3 < 4 > False
three = 3 != 4 > False
four = 3 or 4 or False
five = 3 != 4 >= False
six = 3 != 4 != False
seven = 3 < 4 != False
eight = 3 <= 4 != False
nine = 3 and 4 or False
ten = 3 or 4 and False

print(f'{one=}; {two=}; {three=}; {bool(four)}; {five=}; {six=}; {seven=}; {eight=}; {bool(nine)}; {bool(ten)}')


###############################

none_one = None and 7
none_two = None or 7
#with no gives a syntax error

print(bool(none_one), bool(none_two))

##############################

line_one = '' and 10 - 1
line_two = '' or (10 - 1)
#with no gives a syntax error

print(bool(line_one), bool(line_two)) 
