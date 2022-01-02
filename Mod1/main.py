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

    """
    here they created a for loop that returns the traversal of an array from 
    start to finish and peforms the square on each index
    """
    for i in range(len(array)):
        initial_value = array[i]
        sorted_squares[i] = initial_value * initial_value

    # they sort the new array of squared values
    sorted_squares.sort()

    # need to include the return call for the code to show values
    return sorted_squares


# need to call print to display the values in the terminal
print(sorted_square_array([0, 1, 2, 3]))
