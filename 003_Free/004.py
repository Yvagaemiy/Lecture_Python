#Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

n = 3
m = 2
k = 1

if k <= n * m and (k % n == 0 or k % m ==0):
    print('yes')
else:
    print('no')