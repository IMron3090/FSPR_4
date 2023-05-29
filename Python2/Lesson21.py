def hello():
    print("Greetings")
          
def my_dec(func):
    def wrapper():
        print('расширяем функционал')
        func()
        print('расширяем функционал')
        return wrapper
    
answer = my_dec(hello) #wrapper
print(answer)
print(answer)

