import string
import random
from itertools import product


def get_letters():
    alphabet = list(string.ascii_uppercase)
    alphabet_2 = alphabet.copy()
    robot_letters = (''.join(p) for p in product(alphabet, alphabet_2))
    # for char in alphabet:
    #    for elem in alphabet_2:
    #        robot_letters.append(char.join(elem))
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
        self.name = n.pop()
        return self.name


r = Robot()
print(r.name)
print(type(get_letters()))
