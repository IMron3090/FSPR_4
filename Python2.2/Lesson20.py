"""


"""
def mult(x,y,z):
    print("args",x,y,z)
    return x * y * z 

numbers = [i for i in range(10)]
numbers_2 = [i for i in range(10,15)]
numbers_3 = [i for i in range(20,30)]
print(list(map(mult,numbers,numbers_2,numbers_3)))

def find_even(x):
    return x % 2 == 0

print(list(filter(lambda x: x %2 == 0,numbers)))

numbers = {i:str(i) for i in range(10)}
numbers_2 = {i:str(i) for i in range(10,15)}
print("answer",list(zip(numbers,numbers_2)))
