#!!!!! Список определяется квадратными []- скобками!!!!!!!


list_1 = []
list_1 = list()
list_1 = [1,2,3,4]
print(list_1)
print(*list_1)  # * -говорит что мы хотим увидить только числа( без запятых без скобок и тд)

list_1 = [1,2,3,4]
for i in list_1:
        print(i,end=' ')
list_1 = [1,2,3,6,87]
print(len(list_1)) # len определяет количество элементов в списке
print(list_1[2]) # Можем оброщаться к элементу по индексу
print(list_1[-1]) # !!!! индексация выводиться с конца

list_1 = [1,6]
print(list_1)
list_1.append(45) # append позволяет внести при печатань дополнительное значение (45- только одно)
print(list_1)
list_1.append(321) # если код писать друг за другом то можно приплюсовать еще несколько значений
print(list_1)

list_1 = []
for i in range(5):
    list_1.append(i)
    print(list_1)# при таком выведении принта (отступ на уровне list_1)он будет показывать каждое добовление индекса!!!!!!
    