# Easy -------------------
# Problem 1: Second largest element in array.
arr_1 = [12, 35, 1, 10, 34, 1]
arr_2 = [10, 5, 10]
arr_3 = [10, 10, 10]

def find_second_largest_element(arr):
    '''
    BRUTEFORCE.
    Input arr: an array of integers.
    Output int or None: The second largest integer if it exists.
    '''

    # Using -np.inf would be ideal.
    first_largest = -99999999
    second_largest = -99999999

    # O(n) time complexity.
    for integer in arr:
        if integer > first_largest:
            second_largest = first_largest
            first_largest = integer
        elif integer > second_largest:
            second_largest = integer

    if (second_largest == -99999999):
        return None
    else:
        return second_largest
    
print(find_second_largest_element)
    

