class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.deleted = False

class HashTable:
    def __init__(self, initial_size=16):
        self.size = initial_size
        self.table = [None] * self.size
        self.used_slots = 0
        self.deleted_slots = 0
        self.load_factor = 0.5
        self._resize_threshold = int(self.size * self.load_factor)

    def _hash_function(self, key):
        return hash(key) % self.size

    def _double_hash(self, key, attempt):
        return (self._hash_function(key) + attempt * (1 + hash(key) % (self.size - 1))) % self.size

    def _resize_table(self):
        self.size *= 2
        new_table = [None] * self.size

        for node in filter(None, self.table):
            index = self._find_empty_slot(new_table, node.key)
            new_table[index] = node

        self.table = new_table
        self._resize_threshold = int(self.size * self.load_factor)

    def _find_empty_slot(self, table, key):
        attempt = 0
        index = self._double_hash(key, attempt)
        while table[index] is not None and not table[index].deleted:
            print(f"Collision at index {index} for key {key}. Trying next index.")
            attempt += 1
            index = self._double_hash(key, attempt)
        return index

    def insert(self, key, value):
        if self.used_slots + self.deleted_slots >= self._resize_threshold:
            print(f"Resizing table (current size: {self.size}).")
            self._resize_table()

        attempt = 0
        index = self._find_empty_slot(self.table, key)

        if self.table[index] is None or self.table[index].deleted:
            print(f"Inserting key {key} at index {index}.")
            self.table[index] = HashNode(key, value)
            self.used_slots += 1
        else:
            print(f"Updating value for key {key} at index {index}.")
            self.table[index].value = value

    def search(self, key):
        attempt = 0
        index = self._double_hash(key, attempt)

        while self.table[index] is not None:
            if not self.table[index].deleted and self.table[index].key == key:
                print(f"Key {key} found at index {index}.")
                return self.table[index].value
            attempt += 1
            index = self._double_hash(key, attempt)

        raise KeyError(f"Key not found: {key}")

    def delete(self, key):
        attempt = 0
        index = self._double_hash(key, attempt)

        while self.table[index] is not None:
            if not self.table[index].deleted and self.table[index].key == key:
                print(f"Deleting key {key} at index {index}.")
                self.table[index].deleted = True
                self.deleted_slots += 1
                self.used_slots -= 1
                return
            attempt += 1
            index = self._double_hash(key, attempt)

        raise KeyError(f"Key not found: {key}")

# Ejemplo de uso
hash_table = HashTable()
for i in range(1000):
    hash_table.insert(f"key_{i}", f"value_{i}")

print(hash_table.search("key_42"))

hash_table.delete("key_42")
try:
    print(hash_table.search("key_42"))
except KeyError as e:
    print(e)
