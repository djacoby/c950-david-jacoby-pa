# Hash table class: store and lookup objects based of
# off a hashed attribute of the object
class HashTable(object):
    def __init__(self, capacity=40):
        # Initiate our array with empty values.
        self.table = []
        for i in range(capacity):
            self.table.append([])
    
    # Hash key of object
    # Big O = O(1)
    def get_hash(self, key):
        return int(key) % len(self.table)

    # Insert key value pair of object into Hash Table
    # Big O = O(1)
    def insert(self, key, value):
        index = self.get_hash(key)
        kvp = [key, value]
        self.table[index] = list([kvp])

    # Lookup value based off of hashed key
    # Big O = O(n)
    def lookup(self, key):
        index = self.get_hash(key)
        if self.table[index] is not None:
            bucket_list = self.table[index]
            for i, value in bucket_list:
                if int(i) == key:
                    return value
        else:
            print("Not found.")
            return None
