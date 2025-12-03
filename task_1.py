class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.table[key_hash].append(key_value)
            return True
    
    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None
    
    def delete(self, key) -> bool:
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for i in range(0, len(self.table[key_hash])):
                if self.table[key_hash][i][0] == key:
                    self.table[key_hash].pop(i)
                    return True
        return False
    

# Тестуємо нашу хеш-таблицю:
Ht = HashTable(5)
Ht.insert("apple", 10)
Ht.insert("orange", 20)
Ht.insert("banana", 30)

print(Ht.get("apple"))   # Виведе: 10
print(Ht.get("orange"))  # Виведе: 20
print(Ht.get("banana"))  # Виведе: 30

# Додаємо тести для видалення:
print(Ht.delete("apple"))   # Виведе: True
print(Ht.get("apple"))      # Виведе: None, бо "apple" було видалено
print(Ht.get("orange"))  # Виведе: 20
print(Ht.delete("orange"))  # Виведе: True
print(Ht.get("orange"))     # Виведе: None, бо "orange" було видалено

# Спробуємо видалити ключ, якого немає в таблиці
print(Ht.delete("grape"))   # Виведе: False, бо "grape" немає в таблиці
print(Ht.get("banana"))  # Виведе: 30, бо не вилаляли це значення