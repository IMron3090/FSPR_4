# 
# 1. Что такое генератор и какие виды генератора существуют? Приведите примеры
    # 2.yield
    # 3.next() 
# 2
# Работа протокола итератора представляет собой следующий цикл:

# Создание итератора: для коллекции создается объект-итератор, который будет использо
# ваться для обхода элементов коллекции.
# Первый вызов метода итерации: итератор вызывает метод "next()" для получения 
# первого элемента коллекции.
# Возвращение первого элемента: метод "next()" возвращает первый элемент коллекции, итератор запоминает
# его и готовится к возвращению следующего элемента.
# Повторение до конца коллекции: процесс повторяется до тех пор, пока в коллекции не закончатся
# элементы. Каждый вызов метода "next()" возвращает следующий элемент коллекции, пока не будет достигнут
# конец коллекции.
# Завершение прохода: когда все элементы коллекции были обработаны, итератор завершает свою работу и
# больше не возвращает элементы при вызовах метода "next()".
# Протокол итератора позволяет работать с коллекциями любого размера и типа, предоставляя единую итерфейс
# для их обхода. Он также может быть использован для реализации других 
# алгоритмов, которые требуют доступа к элементам коллекции в определенном порядке.

# 3
# Да, можно создать итератор из итератора. Для этого нам нужно использовать Python 
# itertools Module.
# К примеру, вам нужно создать итератор из двух итераторов, 
# вы можете это сделать с помощью функции chain:


# from itertools import chain

# iterator_1 = range(10)
# iterator_2 = range(20)
# iterators = chain(iterator_1, iterator_2)

# for x in iterators:

# 4
# добавлен к shield

# 5
# Файл PYC представляет собой скомпилированный выходной файл, созданный из исходного кода, 
# написанного на языке программирования Python. Когда файл PY запускается с использованием интерпретатора
# Python, он преобразуется в байт-код для выполнения.
#  В то же время скомпилированный байт-код также сохраняется в виде файла 

 

# Задачи
# Задача 1
from PIL import Image
import csv

class Staff:
    def init(self, name, last_name, photo_path, position, salary, age, department):
        self.name = "Anne"
        self.last_name = "Gray"
        self.photo = Image.open(photo_path)
        self.position = "povar"
        self.salary = "100"
        self.age = "21"
        self.department = "Kitchen"

def create_staff_member(name, last_name, photo_path, position, salary, age, department):
    staff_member = Staff(name, last_name, photo_path, position, salary, age, department)
    with open('staff.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([staff_member.name, 
                         staff_member.last_name, 
                         photo_path, 
                         staff_member.position, 
                         staff_member.salary, 
                         staff_member.age, 
                         staff_member.department])

def read_staff_list():
    with open('staff.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def filter_staff_by_last_name_department(last_name, department):
    staff_list = []
    with open('staff.csv', mode='w') as file:
        writer = csv.writer(file)
        for row in writer:
            if row[1] == last_name and row[6] == department:
                staff_list.append(row)
    return staff_list
filtered_staff_list = filter_staff_by_last_name_department('Gray', 'Kitchen')
print(filtered_staff_list)
# Задача 2
# ?????
# Задача 3 
def rewrite(numbers_1, numbers_2):
    a = set(numbers_1)
    b = set(numbers_2)
    result = (x for x in (a | b, a & b, a - b, a ^ b))

    for item in result:
        yield item

# Задача 4
import time
from functools import wraps

def slow_down(slow_rate):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            time.sleep(slow_rate)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@slow_down(2)
def hi():
    print("Hi Imran")

hi()

# Задача 5
# ???????