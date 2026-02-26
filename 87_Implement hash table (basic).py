# Implement hash table (basic)

class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [None] * self.size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index] = value

    def get(self, key):
        index = self.hash_function(key)
        return self.table[index]
    

# Example usage
hash_table = HashTable()
hash_table.insert("name", "Alice")
hash_table.insert("age", 30)
print(hash_table.get("name"))  # Output: Alice
print(hash_table.get("age"))   # Output: 30
hash_table.insert("name", "Bob")
print(hash_table.get("name"))  # Output: Bob
print(hash_table.get("age"))   # Output: 30
print(hash_table.table)  # Output: ['Bob', None, None, None, None, None, None, None, None, None]
hash_table.insert("city", "New York")
print(hash_table.table)
print(hash_table.get("city"))  # Output: New York
print(hash_table.get("country"))  # Output: None