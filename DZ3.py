#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов
#Пример:
#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

some_list = [float(input('введите элемент списка: ')) for _ in range(int(input('Введите кол-во элементов: ')))]
#mx = max([round(i%1, 3) for i in some_list])
#mn =  min([round(i%1, 3) for i in some_list if round(i%1, 3) != 0])
#print(mx, mn)
print(f' Разница между max и min дробной части = \
    {round(max([round(i%1, 3) for i in some_list]) - min([round(i%1, 3) for i in some_list if round(i%1, 3) != 0]), 3)}')

