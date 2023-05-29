"""

"""
# PIP и его команды
# Пробежимся по основным командам pip: 
# pip help - помощь по доступным командам. 
# pip install package_name - установка пакета(ов). 
# pip uninstall package_name - удаление пакета(ов).
# py -m pip list - Список установленных пакетов, включая редактируемые.
# py -m pip show - Показывает информацию об одном или нескольких установленных пакетах. 
# py -m pip freeze - Вывод установленных пакетов в формате требований.
# py -m pip check - Убедитесь, что установленные пакеты имеют совместимые зависимости. 

def factorial(n): 
    if n == 0 or n == 1: 
        return 1
    else: 
        return n * factorial(n - 1) 

number = 5
print ("Factorial для", number ,"равнo", factorial(number))

def fibonacci(n):
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))

