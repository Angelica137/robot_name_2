import string


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
    for num in range(100, 1000):
        for char in get_letters():
            names.append(char + str(num))
    return names


print(len(name_pool()))
print(len(range(100, 1000)))
print(676*900)
