#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    Finds two items whose sum of weights equals the weight limit.
    Answer looks like -> (zero, one)
    Each element represents the item weights (index position) of the two packages
    HIGHER_NUM[0],SMALLER_NUM[1]
    If pair doesn't exist for the given inputs return None
    !Note!: If the key doesn't exist in the ht, ht_retrieve returns None
    """
    #Based off of last hint, loop through weights and store each weight's list index as its value

    #loop through weights
    for i in range(len(weights)):
        #run insert to add: it takes ht, key and value
        hash_table_insert(ht, weights[i], i)
    #loop through weights again 
    for i in range(len(weights)):
        #check to see if entry for limit-weight
        entry = hash_table_retrieve(ht, limit-weights[i])
        #if there is
        if entry:
            #return it, entry is larger..i is smaller
            return (entry, i)
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
