
# Пробелы между словами

a = 'Pyhton'
b = 'Hello'
c = 'Вася'
d = 'Ура\n это\n же\n вася\n'
my_sep = '$$$$$$$$$$'
print(a,b,c)
print(a,b,c, sep= '--------', end='\n')# end = '\ n' перенос на новую строку 
print(a,b,c, sep = my_sep, end='\n')
print(a,end='\n')
print(b,end='=======')
print(c,end='#####')
print(*a)
print(*a, sep='     ')
print(*a, sep='******')
print(d)