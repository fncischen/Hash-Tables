

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
    index = hash(key, hash_table.capacity)
    # print("Our hashed value", hashed_value)
    pair = LinkedPair(key, value)
    if hash_table.storage[index] == None: 
        hash_table.storage[index] = pair 
    else:
        if hash_table.storage[index].key == key:
            hash_table.storage[index] = pair
        else:
            tempLinkedPair = hash_table.storage[index]
            while tempLinkedPair != None:
                if tempLinkedPair.next == None:
                    tempLinkedPair.next = pair
                    break 
                else:
                    tempLinkedPair = tempLinkedPair.next 


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    index = hash(key, hash_table.capacity)
    if hash_table.storage[index] == None:
        return None 
    elif hash_table.storage[index].key == key:
        if hash_table.storage[index].next == None:
            hash_table.storage[index] == None
        else:
            hash_table.storage[index] = hash_table.storage[index].next
    else:  
        tempLinkedPair = hash_table.storage[index]
        while tempLinkedPair.next != None:
            if tempLinkedPair.next.key == key:

                ## refactor linked list through hash

                ## 
                tempLinkedPair.next = tempLinkedPair.next.next; 
                break 
            else:
                tempLinkedPair = tempLinkedPair.next 


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, hash_table.capacity)
    if hash_table.storage[index] == None:
        return None 
    elif hash_table.storage[index].key == key:
        return hash_table.storage[index].value
    else:  
        # print(hash_table.storage)
        tempLinkedPair = hash_table.storage[index]
        while tempLinkedPair.next != None:
            if tempLinkedPair.next.key == key:
                return tempLinkedPair.next.value
            else:
                tempLinkedPair = tempLinkedPair.next 
        return None 

# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    oldStorage = hash_table.storage

    newHashTable = HashTable(hash_table.capacity * 2)

    for linkedPair in oldStorage:
        if linkedPair == None:
            pass
        else:
            tempLinkPair = linkedPair
            hash_table_insert(newHashTable, tempLinkPair.key, tempLinkPair.value)
            if linkedPair.next != None:
                while tempLinkPair.next != None:
                    print("check!")
                    hash_table_insert(newHashTable, tempLinkPair.next.key, tempLinkPair.next.value)
                    tempLinkPair = tempLinkPair.next

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
