class HashTable(object):
    def __init__(self, capacity=10):
        # Initiate our array with empty values.
        self.map = [None] * capacity
        print(self.map)

    def hash(self, key):
        """Get the index of our array for a specific string key"""
        return int(key) % len(self.map)

    def insert(self, key, value):
        """Add a value to our array by its key"""
        index = self.hash(key)

        print(index)

        if self.map[index] is not None:
            print('in if')
            # This index already contains some values.
            # This means that this add MIGHT be an update
            # to a key that already exists. Instead of just storing the
            # value we have to first look if the key exists.
            for kvp in self.map[index]:
                # If key is found then update,
                # its current value to the new value.
                if kvp[0] == key:
                    kvp[1] = value
                    break
                else:
                    # If no breaks was hit in the for loop, it
                    # means that no existing key was found,
                    # so we can simply just add it to the end.
                    self.map[index].append([key, value])
        else:
            print('in else')
            # This index is empty. We should initiate
            # a list and append our key-value-pair to it.
            self.map[index] = []
            self.map[index].append([key, value])

    def lookup(self, key):
        """Get a value by key"""
        index = self.hash(key)
        if self.map[index] == None:
            raise KeyError()
        else:
            # Loop through all key-value-pairs
            # and find if our key exist. If it does
            # then return its value.
            for kvp in self.map[index]:
                if kvp[0] == key:
                    return kvp[1]

            # If no return was done during loop,
            # it means key didn't exist.
            raise KeyError()
