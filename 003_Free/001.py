
#n = int(input('Введите число: '))
n = 100
s = 0
while n !=  0:
    p = n % 10
    s = s + p
    n = n // 10
    
print('Сумма чисел равна = ',s)

n = 100 

n1 = n // 100

n2 = (n //10) % 10
n4 = (n % 100) //10
n3 = n % 10

print(n1,n2,n4, n3)


x = 123

x1 = x // 100
x2 = x // 10 % 10
x3 = x % 10
print(x1, x2, x3)
    