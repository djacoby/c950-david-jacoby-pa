class HashTable(object):
    def __init__(self, capacity=40):
        # Initiate our array with empty values.
        self.table = []
        for i in range(capacity):
            self.table.append([])

    def get_hash(self, key):
        """Get the index of our array for a specific string key"""
        return int(key) % len(self.table)

    def insert(self, key, value):
        index = self.get_hash(key)
        kvp = [key, value]
        self.table[index] = list([kvp])

    def lookup(self, key):
        """Get a value by key"""
        index = self.get_hash(key)
        if self.table[index] is not None:
            bucket_list = self.table[index]
            for i, value in bucket_list:
                if int(i) == key:
                    return value
        else:
            print("Not found.")
            return None
