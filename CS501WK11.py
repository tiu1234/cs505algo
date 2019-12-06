class HashTable(object):
    MINIMUM_BUCKETS = 4
    BUCKET_SIZE = 5

    def __init__(self, capacity=MINIMUM_BUCKETS * BUCKET_SIZE):
        self.size = 0
        self.threshold = capacity
        self.buckets = [[] for _ in range(capacity // self.BUCKET_SIZE)]

    def insert(self, key, value):
        bucket = self.hash(key)
        for n, element in enumerate(self.buckets[bucket]):
            if element['key'] == key:
                element['value'] = value
                self.buckets[bucket][n] = element
                return
        else:
            self.buckets[bucket].append({'key': key, 'value': value})
            self.size += 1
            if self.size == self.threshold:
                self.resize()

    def get(self, key):
        bucket = self.hash(key)
        for element in self.buckets[bucket]:
            if element['key'] == key:
                return element['value']
        raise KeyError("No such key '{0}'!".format(key))

    def erase(self, key):
        bucket = self.hash(key)
        for n, element in enumerate(self.buckets[bucket]):
            if element['key'] == key:
                del self.buckets[bucket][n]
                self.size -= 1
                return
        raise KeyError("No such key '{0}'!".format(key))

    def hash(self, key):
        return hash(key) % len(self.buckets)

    def contains(self, key):
        bucket = self.hash(key)
        for element in self.buckets[bucket]:
            if element['key'] == key:
                return True
        return False

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        return self.insert(key, value)

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def resize(self):
        capacity = self.size // self.BUCKET_SIZE * 2
        if capacity >= self.MINIMUM_BUCKETS:
            old = self.buckets
            self.buckets = [[] for _ in range(capacity)]
            for n in range(len(self.buckets)):
                self.buckets[n] = old[n]
            self.rehash()

    def rehash(self):
        for n, bucket in enumerate(self.buckets):
            for m, element in enumerate(bucket):
                new_bucket = self.hash(element['key'])
                self.buckets[new_bucket].append(element)
                del self.buckets[n][m]


arr = [67, 39, 40, 74, 10, 54, 20, 7, 87, 52, 44, 23, 11, 78, 98]
hashtable = HashTable()
for a in arr:
    hashtable.insert(a, a)
print("Separate chaining:")
print(hashtable.get(67))


class HashTable(object):

    def __init__(self):
        self.max_length = 8
        self.max_load_factor = 0.75
        self.length = 0
        self.table = [None] * self.max_length

    def __len__(self):
        return self.length

    def __setitem__(self, key, value):
        self.length += 1
        hashed_key = self._hash(key)
        while self.table[hashed_key] is not None:
            if self.table[hashed_key][0] == key:
                self.length -= 1
                break
            hashed_key = self._increment_key(hashed_key)
        tuple = (key, value)
        self.table[hashed_key] = tuple
        if self.length / float(self.max_length) >= self.max_load_factor:
            self._resize()

    def __getitem__(self, key):
        index = self._find_item(key)
        return self.table[index][1]

    def __delitem__(self, key):
        index = self._find_item(key)
        self.table[index] = None

    def _hash(self, key):
        # TODO more robust
        return hash(key) % self.max_length

    def _increment_key(self, key):
        return (key + 1) % self.max_length

    def _find_item(self, key):
        hashed_key = self._hash(key)
        if self.table[hashed_key] is None:
            raise KeyError
        if self.table[hashed_key][0] != key:
            original_key = hashed_key
            while self.table[hashed_key][0] != key:
                hashed_key = self._increment_key(hashed_key)
                if self.table[hashed_key] is None:
                    raise KeyError
                if hashed_key == original_key:
                    raise KeyError
        return hashed_key

    def _resize(self):
        self.max_length *= 2
        self.length = 0
        old_table = self.table
        self.table = [None] * self.max_length
        for tuple in old_table:
            if tuple is not None:
                self[tuple[0]] = tuple[1]


hashtable = HashTable()
for a in arr:
    hashtable.__setitem__(a, a)
print("Linear probing:")
print(hashtable.__getitem__(67))