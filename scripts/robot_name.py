import string
from typing import AsyncIterable


def get_letters():
    alphabet = list(string.ascii_uppercase)
    alphabet_2 = alphabet.copy()
    robot_letters = []
    for char in alphabet:
        for elem in alphabet_2:
            robot_letters.append(char + elem)
    return robot_letters


print(get_letters())
