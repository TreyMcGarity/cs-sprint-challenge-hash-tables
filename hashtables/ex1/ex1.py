def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # initiaize a cache
    cache = {}
    # will be increment to make representing indexes
    index = 0
    # store weights as keys and indexes as values in cache
    for weight in weights:
        cache[weight] = index
        index += 1

    # traverse and stop at end of input array
    for i in range(length):
        # key to find solution case
        key = limit - weights[i]
        # check if a solution is possible
        if key in cache:
            # return values of solution
            return (cache[key], i)