import string
import random


def get_letters():
    alphabet = list(string.ascii_uppercase)
    alphabet_2 = alphabet.copy()
    robot_letters = []
    for char in alphabet:
        for elem in alphabet_2:
            robot_letters.append(char + elem)
    return robot_letters


def name_pool():
    names = []
    numbers = (str(num).zfill(3) for num in range(1000))
    for int in numbers:
        for char in get_letters():
            names.append(char + int)
    return names


n = name_pool()


class Robot:
    def __init__(self):
        self.name = self.reset()

    def reset(self):
        random.shuffle(n)
        self.name = n.pop(0)
        return self.name


robot = Robot()
n = name_pool()
random.shuffle(n)
x = n.pop(0)
print(x)
print(len(n))
