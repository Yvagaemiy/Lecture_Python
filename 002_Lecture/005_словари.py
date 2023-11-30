#Словари — неупорядоченные коллекции произвольных объектов с доступом по ключу.
#В списках в качестве ключа используется индекс элемента. В словаре для определения 
#элемента используется значение ключа (строка, число).


#!!!!!! Словари определяет фигурные {} -скобки   !!!!! 
 

d = {}
d = dict() # это тоже является словарем

d['q'] = 'qwerty'
print(d)

d['w'] = 'werty'
print(d)

d['w'] = 'werty'
print(d['q'])

print('___________________________________')

ictionary = {}
dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ← типы ключей могут отличаться
# print(dictionary['up']) # ↑ типы ключей могут отличаться
# dictionary['left'] = '⇐' 
# print(dictionary['left']) # ⇐
# print(dictionary['type']) # KeyError: 'type' 
del dictionary['left'] # удаление элемента
for i in dictionary:
    print(i)
    print(' {} : {}'. format( i , dictionary[i]))
          


#dictionary[564] = 346758 # добовляет ключ и значение по ключу
#print(dictionary)
