"""

"""
# Map
def my_map(func, iterable):
    result = []
    for i in iterable:
        result.append(func(i))
    return result

# Filter
def my_filter(func, iterable):
    result = []
    for i in iterable:
        if func(i):
            result.append(i)
    return result

#  список чисел
numbers = [1, 2, 4, 5, 7, 8, 10, 11]

#  функция, которая проверяет числа
def filter_odd_num(in_num):
    if(in_num % 2) == 0:
        return True
    else:
        return False

#  Применение filter() для удаления нечетных чисел
out_filter = filter(filter_odd_num, numbers)

# Используя функцию filter, получить список, который записывает имена с длиной в 3 или более символа в новый список.
print("Тип объекта out_filter: ", type(out_filter))
print("Отфильтрованный список: ", list(out_filter))


names = ["John", "Bob", "Alice", "Tim", "Sam"]
filtered_names = list(filter(lambda x: len(x) >= 3, names))
print(filtered_names)

# Функция filter() в Python применяет другую функцию к заданному итерируемому объекту
# (список, строка, словарь и так далее),
# проверяя, нужно ли сохранить конкретный элемент или нет.
# Простыми словами, она отфильтровывает то,
# что не проходит и возвращает все остальное.