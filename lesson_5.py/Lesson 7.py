"""



"""
# Интерируемые - iterable. Исчисляемый. Это те перемменные,которые хранят больше одного значения 
# ИНдексы
#    0 1 2 3 
names = [1,3,4,5] # 3
print(type(names),names[3] )
names = ()
print(type(names) )
# Dictionary - Словарь
# ключом словаря могут быть только не изменяемые типы переменных
user_data = {
"ключ": "Значение",
1:None,
2:21,
3:6.7,
4: [2,3,4],
5: (1,2,3),
6: {"key":"Другой Словарь "}
# [1]: 23, # error
# (2,3,[2,3]):"Error,# кортеж можно использовать как ключ, но не рекомендуется"
}
# 40-50 vncaol2wnmcm,vlea,pxw
print(type(user_data),user_data,user_data["ключ"],sep="\n" )
print(type(user_data),user_data,user_data["ключ"],sep="\21" )
print(type(user_data),user_data,user_data["ключ"],sep="\6.7" )
print(type(user_data),user_data,user_data["ключ"],sep="\[2,3,4]" )
print(type(user_data),user_data,user_data["ключ"],sep="\(1,2,3)" )

user_data = {
"username":"Gobby",
"password" : "2rtr123r",
"age" : 18,
"age" : 22,
}
print(user_data["age"])

user_data =[
    {
"username":"Gobby",
"password" : "2rtr123r",
"age" : 18,
    },

{
"username":"Apo",
"password" : "2rtr123r",
"age" : 14,


},
{
"username":"Apo",
"password" : "2rtr123r",
"age" : 14,
},
    ]
print(user_data[0]["username"],user_data[0]["age"])

user_data["username"] = "Alabasta"
print(user_data.keys(),user_data.values(),user_data.items,()sep="\n")
user_list = list(user_data.values())#


print("get",user_data.get("age"),user_data.get("unexisting"))

numbers = {2,3,4,"hello", 2, 4}
print(numbers)
numbers = {}









































