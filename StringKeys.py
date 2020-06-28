class HashTable(object):
    def __init__(self):
        self.table = [None]*10000
    
    def calculate_hash_value(self, string):
        hash_value = ord(string[0]) * 100 + ord(string[1])
        return hash_value

    def store(self, string):
        value = self.calculate_hash_value(string)
        if self.table[value] is None:
            self.table[value] = [string]
        else:
            self.table[value].append(string)

    def lookup(self, string):
        value = self.calculate_hash_value(string)
        if self.table[value] is not None:
            if string in self.table[value]:
                return value
        return -1
