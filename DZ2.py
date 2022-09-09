#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

def multy_par (list_one, list_new, first, last):
    if last-first == 0 or last-first == 1:
        return list_new.append(list_one[first]*list_one[last])
    else:
        list_new.append(list_one[first]*list_one[last])
        multy_par(list_one, list_new, first+1, last-1)
    return list_new

some_list = [int(input('введите элемент списка: ')) for _ in range(int(input('Введите кол-во элементов: ')))]
new_list =[]
index_start = 0
index_end = len(some_list)-1
print(multy_par(some_list, new_list, index_start, index_end))


