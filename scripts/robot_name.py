import string
import random
from itertools import product


def get_letters():
    alphabet = list(string.ascii_uppercase)
    alphabet_2 = alphabet.copy()
    pairs = product(alphabet, alphabet_2)    # O(n^2)
    robot_letters = (''.join(pair) for pair in pairs)  # O(n)
    return robot_letters


def name_pool():
    numbers = (str(num).zfill(3) for num in range(1000))
    combinations = product(get_letters(), numbers)
    names = list(''.join(elem) for elem in combinations)
    return names


n = name_pool()


class Robot:
    def __init__(self):
        self.name = self.reset()

    def reset(self):
        if not n:
            raise RuntimeError("No names available")
        random.shuffle(n)
        self.name = n.pop()
        return self.name
