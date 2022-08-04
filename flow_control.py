while True:
    try:
        sign = input('Enter sign (**,*,/,+,-): ')
        if sign not in ('**', '*', '/', '+', '-'):
            print('You entered an invalid character')
            break

        first_number = input('Enter the number: ')
        if first_number.find('.') == 1:
            first_number = float(first_number)
        elif first_number.isnumeric():
            first_number = int(first_number)
        else:
            print('You entered an invalid character')
            break 

        second_number = input('Enter the number: ')
        if second_number.find('.') == 1:
            second_number = float(second_number)
        elif second_number.isnumeric():
            second_number = int(second_number)
        else:
            print('You entered an invalid character')
            break

        if sign == '**':
            print(f'Answer = {first_number ** second_number} ')
        elif sign == '*':
            print(f'Answer = {first_number * second_number}')
        elif sign == '/':
            print(f'Answer = {first_number / second_number}')
        elif sign == '+':
            print(f'Answer = {first_number + second_number}')
        elif sign == '-':
            print(f'Answer = {first_number - second_number}')
        else:
            print('You entered an invalid character')
            break
    except (TypeError, ValueError):
        print('You entered an invalid character')
    except ZeroDivisionError:
        print(f'Can\'t divice by zero') 
    break
