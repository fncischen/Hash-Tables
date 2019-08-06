

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = [None] * capacity


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, max):

    hash = 5381
    for c in string:
        hash = (hash * max) + ord(c)
    return hash


# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    hashed_value = hash(value, 33)
    newPair = Pair(key, hashed_value)
    if newPair in hash_table.arr: 
        print("This item is in the hash table")
    else:
        for i in range(hash_table.capacity):
            if hash_table.arr[i] == None:
                hash_table.arr[i] = newPair
                break 


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    print(hash_table.arr)
    for i in range(hash_table.capacity):
        if hash_table.arr[i].key == key: 
            hash_table.arr[i] = None 
            break 
    print("This item is not in the hash table")
# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    for pair in hash_table.arr:
        if pair == None:
            pass
        elif pair.key == key: 
            return pair 
    return None 


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
