def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # will be the list of both negatives and positives
    result = []
    # initialize cache 
    cache = {}

    # traverse through input list of numbers
    for num in a:
        # check if number is less than zero
        if num < 0: 
            # store value of num as negative 
            cache[-num] = num

    # traverse numbers again
    for num in a:
         # check if a number is also in the cache (where the negatives are)
        if num in cache:
            # add number to result array
            result.append(num)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
