

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    num = 5381 # prime
    for char in string:
        num = (num * 33) + ord(char)
    return num % max

# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    index = hash(value, hash_table.capacity)
    # print("Our hashed value", hashed_value)
    pair = LinkedPair(key, value)
    if hash_table.storage[index] != None: 
        hash_table.storage[index].next = pair 
    else:
        hash_table.storage[index] = pair


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    print(hash_table.storage)
    for i in range(hash_table.capacity):
        if hash_table.storage[i] == None:
            pass
        elif hash_table.storage[i].key == key: 
            hash_table.storage[i] = None 
            break 
    print("This item is not in the hash table")


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    for pair in hash_table.storage:
        if pair == None:
            pass
        elif pair.key == key: 
            return pair.value 
    return None 


# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    oldStorage = hash_table.storage

    newHashTable = HashTable(hash_table.capacity * 2)

    for linkedPair in oldStorage:
        if linkedPair.next != None:
            tempLinkPair = linkedPair
            while tempLinkPair.next != None:
                if tempLinkPair.next != None:
                    oldStorage.append(tempLinkPair.next)
                    tempLinkPair = tempLinkPair.next
    
    for linkedPair in oldStorage:
        hash_table_insert(newHashTable, linkedPair.key, linkedPair.value)
    
    return newHashTable



def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
