#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    # enumerate the weights array and run a loop through it
    for index, weight in enumerate(weights):

        # find the difference in limit and current weight
        difference = limit - weight

        # if the hash table has a key of "difference" retrieve that index
        if hash_table_retrieve(ht, difference) is not None:
            difference_index = hash_table_retrieve(ht, difference)
                        
            # order the indexies accordingly
            if difference_index >= index:
                return [difference_index, index]
            else: 
                return [index, difference_index]

        # otherwise, insert the weight into the hash table with the index as the value
        else:
            hash_table_insert(ht, weight, index)


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
