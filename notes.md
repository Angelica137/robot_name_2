def get_letters():
    initialise list of letters -> O(n)
    copy list of letters -> O(n)
    initialise empty list -> O(1)
    for char in list 1: -> O(n)
        for elem in list 2: -> O(n)
            concatenate the letters -> O(n^2)
						and add them to the empty list -> O(1)
    return the new list -> O(1)

TOTAL: O(n) + O(n) + O(n) * O(n) + O(n^2) + O(1) +O(1)
       O(n^2) + O(n^2)
       O(n^2)


def name_pool():
    initilaise empty list -> O(1)
    create a range from 0 to 1000 -> O(1)
		adding zeros as needed -> O(n)
    for int in numbers range -> O(n)
        for char in get_letters list: -> O(n^2)
            concatenate the elments  -> O(n^2)
						and append to empty list -> O(1)
    return new list -> O(1)
TOTAL: O(n^2) + O(n^2) + O(n^2)
       O(n^2)


def reset():
    shuffle the name pool -> O(n) + O(n^2)
    pop the first element in the shuffled list -> O(n)
    return the popped element -> O(1)
TOTAL: O(n^2)
