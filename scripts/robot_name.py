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
    numbers = (str(num).zfill(3) for num in range(1000))
    for int in numbers:
        for char in get_letters():
            names.append(char + int)
    return names
