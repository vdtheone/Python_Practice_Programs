# Handle collisions in hash tables

class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [None] * self.size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for i, (k, v) in enumerate(self.table[index]):
                if k == key:
                    self.table[index][i] = (key, value)
                    return
            self.table[index].append((key, value))

    def get(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return v
        return None 
    

# Example usage
hash_table = HashTable()
hash_table.insert("name", "Alice")
hash_table.insert("age", 30)
print(hash_table.get("name"))  # Output: Alice
print(hash_table.get("age"))   # Output: 30
hash_table.insert("name", "Bob")
print(hash_table.get("name"))  # Output: Bob
print(hash_table.get("age"))   # Output: 30
print(hash_table.table)  # Output: [[('name', 'Bob')], None,