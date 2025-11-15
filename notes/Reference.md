# Packages
    - Counter: 
        counts = Counter(nums) # is same as

        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

    - Lambda key
        key = lambda x: x[1] #this tells to use the 1th index for the key for comparing, whatever that comparison is, rather than the 0th index. so it overrides the base of using x[0] for the key. useful for comparing dict entries by value, for example, rather than key.

    - Heapq:
        heappush and heappop are the operations
        Default has largest things sink to bottom (min-heap)
        heap[0] always smallest(with minheap)
        structured like a tree, with property that parent > children
        heappop removes the root
        negate the value to make a max heap