#1.Створи послідовність інструкцій,d яка отримує рядок від користувача та 
#друкує кожне третє слово з цього рядка. Цикли не використовувати

user_input = input('Enter offer here: ')
print(f'{user_input[2::3]}')


#2.Створи генератор списка
li = [1, 2.1, 'f', '2', 3,'1', 18, 'df']
print(li)

li2 = [i if type(i) == float else i
       if (type(i) == int and i % 2 == 0) else i ** 2
       if (type(i) == int and i % 2 != 2) else (str(int(i) * 3))
       if (type(i) == str and i.isdigit()) else -1
       for i in li]
print(li2)
#Вихідний список [1, 2.1, -1, '6', 9, '3', 18, -1]

#Як та які елементи потрапляють з вхідного до вихідного списка:

#-Елемент типу float
#-Елемент типу int та є парним
#-Елемент типу int та є непарним. Додатково звести у 2 ступінь.
#Приклад, елемент 3 -> 9
#-Елемент типу str у якому лише цифри. Додатково помножити на 3.
#Приклад, елемент "2" -> "6"
#-В інших випадках замість елемента підстав число -1
