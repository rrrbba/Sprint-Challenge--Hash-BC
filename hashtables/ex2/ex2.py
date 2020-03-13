#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * (length - 1) #gets rid of extra element at end the(NONE)

    """
    Objective: reconstruct trip from the tickets
    Source string is starting point 
    Destination string is next airport along trip
    Ticket for first & final flight has destination with source = None 
    The function should output an array of strings with entire route of trip
    Can assume that function will always be handed a valid ticket as input
    """
    #Based off the second hint, hash each ticket so that the starting location is the key and the destination is the value.

    #loop through the length
    for i in range(length):
        #insert the source and destination into hashtable
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)
    #Then when constructing the entire route, ith location in the route can be found by checking the hash table for the i-1th destination

    #start the first ticket source key in route to none
    route[0] = "NONE"
    #use a variable instead of route[0] in retrieve, location
    location = route[0]

    #loop through length - 1 so it can be within range
    for i in range(length-1):
        #set route at current position since the tickets source and desitnation are in hashtable 
        route[i] = hash_table_retrieve(hashtable, location)
        #update as you move through 
        location = route[i]
        
    return route

