# Напишите программу, которая принимает на вход число N
# и выдает последовательность из N членов

# Пример:
# Для N = 5: 1, -3, 9, -27, 81

# Вариант 1: каждый следующий элемент - это предыдущий, умноженный на -3

def create_seq(numb_members: int):
    seq = [1]
    i = 0
    while i<=numb_members-1:
        seq.append(seq[i]*-3)
        i += 1
    return seq

n = int(input('Enter your number of members in the sequence: '))
print(create_seq(n))

# Вариант 2: каждый элемент - это -3 в степени, соответствующей его индексу

def create_seq(numb_members: int):
    seq = []
    for element in range(0, numb_members):
        seq.append((-3)**element)
    return seq

n = int(input('Enter your number of members in the sequence: '))
print(create_seq(n))