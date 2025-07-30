#The following is my first attempt at creating an arraylist class in python. Func includes appending, resizing, retrieving and setting data, 
#deleting and inserting, as well as python functionality  (arr[0], for example)

class ArrayList:
    def __init__(self):
        self.capacity = 4 #How much space is allocated
        self.size = 0 #Number of items in the arraylist
        self.array = [None] * self.capacity #The internal list that holds the values

    def append(self, value):
        if self.size == self.capacity:
            self._resize()  #Leading underscore signifies this is an internal use only. Not req'd, just for readability. 
        self.array[self.size] = value
        self.size += 1

    def _resize(self):
        self.capacity = self.capacity * 2
        new_array = [None] * self.capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def get(self, index): #Retrieve the value at an index
        if 0 <= index < self.size:
            return self.array[index]
        else:
            raise IndexError("Index out of bounds")
        
    def set(self, index, value): #Set the value at an index
        if 0 <= index < self.size:
            self.array[index] = value
        else:
            raise IndexError("Index out of bounds")
        
    def remove(self, index):#Remove an index, shifting all items following the index to the left and decreasing the size by 1
        if 0 <= index < self.size:
            for i in range(index, self.size -1):
                self.array[i] = self.array[i + 1]
            self.array[self.size - 1] = None
            self.size -= 1
        else:
            raise IndexError("Index out of bounds")
        
    def insert(self, index, value):
        if 0 <= index <= self.size:
            if self.size == self.capacity:
                self._resize()
            for i in range(self.size, index, -1):
                self.array[i] = self.array[i - 1]
            self.array[index] = value
            self.size += 1
        else:
            raise IndexError("Index out of bounds")

#The following functions allow treating the class closer to like a python list, with accessing data with brackets, and len, and iterating
    def __getitem__(self, index):
        if 0 <= index < self.size:
            return self.array[index]
        else :
            raise IndexError ("Index out of bounds")

    def __setitem__(self, index, value):
        if 0 <= index < self.size:
            self.array[index] = value
        else:
            raise IndexError ("Index out of bounds")
    
    def __len__(self):
        return self.size
    
    def __iter__(self):
        for i in range(self.size):
            yield self.array[i]

#Test case
arr = ArrayList()
arr.append(5)
arr.append(7)
arr.append(10)
arr.append(15)
arr.insert(2, 20)
arr.remove(1)
for x in arr:
    print(x)#(output: 5, 20, 10, 15)
