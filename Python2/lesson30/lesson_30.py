def random(start,end,step):
    arr = []
    for i in range(start,end,step):
        if i % 2 == 0:
            continue
        arr.append(i)
    return arr     

if __name__ == "__main__":
    random(0,10,2,)
    random(1,100) 

def plus(num = 0):
    try:
        if num:
            return int(num) + 5
        else:
            return "pòease enter a number"
    except ValueError as err:
        return err
    
if __name__ == "main":
    print(plus(5))
    print(plus("5"))
    print(plus("-1"))
    print(plus("a"))

    