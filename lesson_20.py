"""






"""
def short_word(names):
    if names:
        length = len(names[0])
    else:
        return False
    
    for name in names[1:]:
        name_len = len(name)
        if name_len < length:
            length = name_len

    return length

names = ["Bekzod", "John", "Gabriel"]
result = short_word(["Bekzod", "John", "Gabriel"])