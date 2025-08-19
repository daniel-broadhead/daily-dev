#The following is my first attempt at implementing a hashmap structure from scratch. Func includes putting key, value pairs into buckets,
#converting keys into hashes, getting key, value pairs, deleting values resizing the hashmap, accessing key, value, and item generators,
# and accessibility using brackets. 

class HashMap:
    def __init__(self, capacity = 8):
        self.capacity = capacity #Number of buckets
        self.size = 0 #Number of key-value pairs currently in map
        self.buckets = [[] for _ in range(capacity)] #A list of lists to handle collisions(chaining)
    
    def _hash(self, key): #Hash is built in to python. Returns a large integer, which then after modulo-ing, makes it a valid index for the bucket
        return hash(key) % self.capacity
    
    def put(self, key, value): #Insert or update contents of map
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self.size += 1

        if self.size / self.capacity > 0.75: #Automatic resizing when load factor unfavorable
            self._resize()
    
    def _resize(self): #internal method to resize when critical load factor reached
        old_buckets = self.buckets #Store current buckets in var old_buckets
        self.capacity *= 2 #Double current capacity
        self.buckets = [[] for _ in range(self.capacity)] #Creating new list of lists(bucket)
        self.size = 0 #size set to 0, will rehash everything
        
        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value) #Re-insert into new buckets. Calls self._hash method as well


    def get(self, key): #Return the value associated with a key
        index = self._hash(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return v
        return None
    
    def remove(self, key): #Delete a key,value pair from the map
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return
    
    def __len__(self): #Allows accessing of len for map
        return self.size
    
    def __str__(self): #Allows printing the map
        pairs = []
        for bucket in self.buckets:
            for k, v in bucket:
                pairs.append(f"{k}: {v}")
        return "{" + ", ".join(pairs) + "}"

    def keys(self): #Allow returning keys
        for bucket in self.buckets:
            for key, _ in bucket:
                yield key
    
    def values(self): #Allow returning values
        for bucket in self.buckets:
            for _, value in bucket:
                yield value
    
    def items(self): #Allow returning key,value pairs
        for bucket in self.buckets:
            for key, value in bucket:
                yield (key, value)

    def __getitem__(self, key): #Allow bracket access
        value = self.get(key)
        if value is None:
            raise KeyError(f"Key '{key}' not found")
        return value
    
    def __setitem__(self, key, value): #Allow bracket assignment
        self.put(key, value)

    def __delitem__(self, key): #Allow del hm bracket
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return
        raise KeyError(f"Key '{key}' not found")
        
            

    # hm = HashMap()

    # # __setitem__ → allows bracket assignment
    # hm["name"] = "Alice"
    # hm["age"] = 30

    # # __getitem__ → allows bracket access
    # print(hm["name"])  # Alice
    # print(hm["age"])   # 30

    # # __delitem__ → allows deletion with del
    # del hm["age"]

    # # Confirm deletion
    # print("age" in list(hm.keys()))  # False

    # # Try accessing a deleted or missing key
    # try:
    #     print(hm["age"])  # should raise KeyError
    # except KeyError as e:
    #     print("Caught:", e)


            
