#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """

    # insert all tickets into hash table
    for i in tickets:
        hash_table_insert(hashtable, i.source, i.destination)
    
    # set the origin to NONE
    origin = "NONE"

    # starting with key NONE, append each destination (value) in hash table to array
    for i in range(0, len(route)):
        destination = hash_table_retrieve(hashtable, origin)
        route[i] = destination
        origin = destination
    
    # delete last item in array to get rid of the last NONE
    del route[-1]
    
    return route
