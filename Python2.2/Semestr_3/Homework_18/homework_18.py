# Task 1
def accum(s):
    index = 1
    result = []
    for letter in s:
        letter = letter * index
        letter = letter.capitalize()
        index += 1
        result.append(letter)
    return "-".join(result)
# Task 2
def check_concatenated_sum(num, n):
    return n and num % int('1' * n) == 0