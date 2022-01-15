def name_pool():
    initialise a list containing the letters -> O(n)
    calcualte a cartesian product of the letter list with itself -> O(n^2)
    join the resulting paris -> O(n)
    create a range from 0 to 1000 -> O(1)
		adding zeros as needed -> O(n)
    calculate a cartesian product fo the letters and the numbers -> O(n^2)
    join the resulting tupples -> O(n)
    return new list -> O(1)
TOTAL: O(n) + O(n^2) + O(n) + O(1) + + O(n) + O(n^2) + O(n) + O(1)
       O(n^2)


def reset():
		calculate n -> O(n^2)
    check if n is empty -> O(n)
    shuffle the name pool -> O(n)
    pop the last element in the shuffled list -> O(1)
    return the popped element -> O(1)
TOTAL: O(n^2)
