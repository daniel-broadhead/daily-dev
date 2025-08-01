#The following is my first attempt at implementing a hashmap structure from scratch. Func includes putting key, value pairs into buckets,
#converting keys into hashes, getting key, value pairs, and deleting key, value pairs. More to come(probably)

class HashMap:
    def __init__(self, capacity = 8):
        self.capacity = capacity #Number of buckets
        self.size = 0 #Number of key-value pairs currently in map
        self.buckets = [[] for _ in range(capacity)] #A list of lists to handle collisions
    
    def _hash(self, key):
        return hash(key) % self.capacity
    
    def put(self, key, value): #Insert or update contents of bucket
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket [i] = (key, value)
                return
        bucket.append((key, value))
        self.size += 1
    
    def get(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return v
        return None
    
    def remove(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        pairs = []
        for bucket in self.buckets:
            for k, v in bucket:
                pairs.append(f"{k}: {v}")
        return "{" + ", ".join(pairs) + "}"

            

hm = HashMap()
hm.put("a", 4)
hm.put("b", 24)
hm.put("c", 3)
hm.put(5, 5)
print(len(hm))
print(hm)

            
