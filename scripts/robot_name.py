import string
import random
from itertools import product


def get_letters():
    alphabet = list(string.ascii_uppercase)  # O(n)
    alphabet_2 = alphabet.copy()  # O(n)
    pairs = product(alphabet, alphabet_2)    # O(n^2)
    robot_letters = (''.join(pair) for pair in pairs)  # O(n)
    return robot_letters


def name_pool():
    numbers = (str(num).zfill(3) for num in range(1000))  # O(n) + O(n)
    combinations = product(get_letters(), numbers)  # O(n^2) + O(n^2)
    names = list(''.join(elem) for elem in combinations)  # O(n^2) + O(n)
    return names


n = name_pool()  # O(n^2)


class Robot:
    def __init__(self):
        self.name = self.reset()

    def reset(self):
        if not n:  # O(n)
            raise RuntimeError("No names available")  # O(1)
        random.shuffle(n)  # O(n)
        self.name = n.pop()  # O(1)
        return self.name
