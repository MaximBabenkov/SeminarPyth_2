# Напишите программу, в которой пользователь будет задавать две строки,
# а программа определять количество вхождений одной строки в другую

def amount_substr(text_1: str, text_2: str):
    count = 0
    for i in range(len(text_1) - len(text_2) + 1):
        if text_1[i:i+len(text_2)] == text_2:
            count += 1
    return count

str_1 = str(input('Enter your text: '))
str_2 = str(input('Enter your item to find in text: '))
print(amount_substr(str_1, str_2))

