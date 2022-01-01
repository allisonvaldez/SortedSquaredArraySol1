"""
time: O(n log(n)) since we use a sort algorithm | space: O(n) the length of
the array
"""


def sorted_square_array(array):
    """
    here they are creating an array with 0 as the initialized value via a
    for-loop within an array
    """
    sorted_squares = [0 for i in array]

    for i in range(len(array)):
        initial_value = array[i]
        sorted_squares[i] = initial_value * initial_value

    sorted_squares.sort()
    return sorted_squares


print(sorted_square_array([0, 1, 2, 3]))
