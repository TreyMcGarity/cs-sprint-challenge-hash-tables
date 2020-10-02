#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # list of destinations along route
    route = []
    # initialize cache
    cache = {}
    
    # store tickets into cache 
    for ticket in tickets:
        # source is key and desitination is value
        cache[ticket.source] = ticket.destination
    
    # add initial cached route None
    route.append(cache["NONE"])

    # traverse and stop at index of last element
    for i in range(length - 1):
        # add cached route at position of loop to result array
        route.append(cache[route[i]])

    return route