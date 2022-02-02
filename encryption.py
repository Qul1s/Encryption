import language
from array import *
import random

def encryption(text):
    random_number = random.randrange(1, 9)
    random_direction = random.randrange(0, 1)
    print(random_direction)
    if random_direction == 0:
        direction = 'L'
    else:
        direction = 'R'
    encryption_code = str(random_number) + '.' + direction
    new_text=''
    print(encryption_code)
    for i in range(len(text)):
        if language.is_English(text[i]) == True:
            alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
            alphabet_high = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        elif language.is_Russian(text[i]) == True:
            alphabet_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
            alphabet_high = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        else:
            new_text = new_text + text[i]
            continue
        if text[i].isupper() == True:
            alphabet = alphabet_high
        else:
            alphabet = alphabet_lower

        position = alphabet.find(text[i])

        if random_direction == 0:
            if random_number > position:
                position = len(alphabet) - (random_number - position)
            else:
                position = position - random_number
        else:
            if position + random_number > len(alphabet)-1:
                position = position + random_number - len(alphabet)
            else:
                position = position + random_number

        new_text = new_text + alphabet[position]
    return new_text

def deencryption(text, code):
    random_number = int(code[0])
    direction = code[2]
    if direction == 'L':
        random_direction = 1
    else:
        random_direction = 0

    new_text =''
    for i in range(len(text)):
        if language.is_English(text[i]) == True:
            alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
            alphabet_high = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        elif language.is_Russian(text[i]) == True:
            alphabet_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
            alphabet_high = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        else:
            new_text = new_text + text[i]
            continue
        if text[i].isupper() == True:
            alphabet = alphabet_high
        else:
            alphabet = alphabet_lower

        position = alphabet.find(text[i])

        if random_direction == 0:
            if random_number > position:
                position = len(alphabet) - (random_number - position)
            else:
                position = position - random_number
        else:
            if position + random_number > len(alphabet)-1:
                position = position + random_number - len(alphabet)
            else:
                position = position + random_number
        new_text = new_text + alphabet[position]
    return new_text


print("Введите что-нибудь, чтобы проверить шифр: ")
text = input()
text = encryption(text)
print(text)
print("Введите шифр: ")
code = input()
text = deencryption(text, code)
print(text)