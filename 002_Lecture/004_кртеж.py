# Картеж не изменяемый массив( для поролей , логинов и т.д)
#!!!!!! картеж определяет ()-скобками   !!!!! 

t = ()# это пустой кaртеж
print(type(t))

t = (1, 4, 6, 8, ) # В конце картежа нужно оставить запятую
print(type(t))

v = [2, 5, 6 ,98] # в квадратных скобках СПИСКИ
print(v)
print(type(v))

v = tuple(v) # метод перевел лист в картеж
print(v)
print(type(v))

# Присваивание 
# a = 1
# d = 2
# можно так a , d = 1 , 2
# a = 1
# d = 1
# можно так a = d = 1 

a, b, c, s = v #  переменных должно быть столько сколько аргументов у v
print(a, b, c , s)

print('_________________________________')


t_2 = (1,5,8,98)
print(t_2[3])
print('_________________________________')

for i in t_2:
    print(i, end=' ')
    
print('_________________________________') 

for i in range(len(t_2)):
    print(t_2[i], end=' ')

print('_________________________________') 

#t_3 = (1,5,8,98) список так не заменить элемент меняем скобки и все запустится

t_3 = [3,56,34,9]
t_3[0] = 1234
print(t_3)
