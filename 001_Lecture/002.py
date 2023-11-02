#num = input('Введите число: ')
# res = 0
# if len(num)==3:
#         for i in num: 
#             res = res + int(i)
#         print('Сумма чисел =',res)
# else:
#         print('Это не трехзначное число!')




# num = 123
# res = 0
# #if len(num)==3:
# for i in num:
#     res = res + int(i)
# print(res)



# num = 123
# res = 0
# for i in num:
#     res = res + int(i)
# print(res)

# num = input('Введите число: ')
# a = int(num[0])
# b = int(num[1])
# c = int(num[2])
# print('сымма равна =', a + b + c)


# num = 123
# res = 0
# for i in num: 
#     res = res + int(i)
# print('Сумма чисел =',res)



# num = input()
# print(int(num[0]) + int(num[1]) + int(num[2]))

# num = 265
# print(type(num))
# res = 0
# for i in num:
#     res = res + i
# print(res)

# a = 'qwer'
# print(type)
# print(a[0])


# n = int(input('Введите число: '))
# print(type(n))
# su = 0 
# for i in range (0,n ):
#     su = su +int[i]
#     print(su)

# n = int(input('Введите число: '))
# print(type(n))
# counter = 0
# res = 0
# while n > 0:
#     for i in range(n):
#         res = res / 10
#         counter = res+1
#         print(counter)


n = int(input("Введите число: "))
res = 0
while  n != 0:
    p = n % 10 
    res = res + p
    n = n //10
print("Сумма цыфр в числе = ",res)

print('__________________________') 
n = 222
n1 = n // 100 # Нахождение первой цифры числа
n2 = (n % 100) // 10 # Нахождение второй цифры числа
n3 = n % 10 # Нахождение третьей цифры числа
res1 = n1 + n2 + n3
print("Сумма цыфр в числе = ",res1)

print('__________________________')

i = 0 
massif = [1, 8 , 4, 34,56, 82]
while (i < 6):
    print("massif[",i,"]:", massif[i])
    i = i + 1
print('__________________________') 

f = 0
while (f < 10):
    f = f + 6
    print(f)        
print('__________________________') 

a = [4,67,3,-9,-13,56,34,-7]
for i in a:
        if i == 99:
            print('Ура нашол 99')
            break
else:
    print('Не нашол 99!')
    
print('__________________________') 
  
def monety_i_ves (monety, ves, number):
    print("Пример № %s"%(number))
    print("Всего вес манет: %s"% (monety*ves))
    
monety_i_ves(110,2,1)     
   


  
print('__________________________') 


def primer (a,b):
    print("a = ",a,"b = ",b)
primer(4,55)

monety_i_ves(55,5,2)  

print('__________________________') 

def summa(a, b, c = 100):# фунлция по умолчанию с = 100
    return a + b + c
ab = summa (2,30,1000 ) # Если не ввести сюда 1000 то  по умалчанию будет использоваться аргумент с =100
print(ab)

print('__________________________') 
 
def Plochad (a,b):
    return a* b

a1 = 14
b1 = 2
print("Площадь прямоугольника %s на %s равна %s"% (a1,b1,Plochad (a1,b1)))

print('__________________________')

for i in range(0,1):
    a = int(input("Введите а: "))
    b = int(input("Введите b: "))
    print("Площадь прямоугольника %s на %s равна %s"% (a,b,Plochad (a,b))) 
    
print('__________________________')
       

p =100 # это лакальня переменная видна и снаружи и в этой функции
def pue():
    u = 3
    e = 56
    print(p,u,e)# в это функции видны только внутренние аргументы снаружион не видны
pue() 
