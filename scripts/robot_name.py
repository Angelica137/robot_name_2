import string
import random
from itertools import product


def name_pool():
    alphabet = list(string.ascii_uppercase)  # O(n)
    letters = (''.join(pair)
               for pair in product(alphabet, alphabet))  # O(n) + O(n^2)
    numbers = (str(num).zfill(3) for num in range(1000))  # O(n)
    names = list(''.join(elem)
                 for elem in product(letters, numbers))  # O(n) + O(n^2)
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
