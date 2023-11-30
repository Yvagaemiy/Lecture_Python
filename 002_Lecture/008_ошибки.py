# Профилирование и отладка
# Мы с вами люди, а людям суждено ошибаться, даже при написании программного кода 
# Давайте разберем с Вами самые частые ошибки в написании кода на Python.
# 🔥Самые распространенные ошибки:


#1) SyntaxError(Синтаксическая ошибка)
# number_first = 5
# number_second = 7
# if number_first > number_second # !!!!! надо поставить ": "
#  print(number_first)



#2) IndentationError(Ошибка отступов)
# number_first = 5
# number_second = 7
# if number_first > number_second:
# print(number_first) # !!!!! надо сделать отступ print
# # Отсутствие отступов


#3) TypeError(Типовая ошибка)
# text = 'Python'
# number = 5
# print(text + number)
# Нельзя складывать строки и числа




#4) ZeroDivisionError(Деление на 0)
# number_first = 5
# number_second = 0
# print(number_first // number_second) 
# Делить на 0 нельзя


#5) KeyError(Ошибка ключа)
# dictionary = {1: 'Monday', 2: 'Tuesday'}
# print(dictionary[3])
# Такого ключа не существует

#6) NameError(Ошибка имени переменной)
# name = 'Ivan'
# print(names)
# Переменной names не существует

#7) ValueError(Ошибка значения)
# text = 'Python'
# print(int(text))
# Нельзя символы перевести в целые значения


