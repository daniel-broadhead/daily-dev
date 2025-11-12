"""
Problem: kth largest element in an array (LeetCode #215)
Link: https://leetcode.com/problems/kth-largest-element-in-an-array
Date: 2025-11-12

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

Approach:
- Heap maintains property that each parent < children. Build a heap from the numbers, and pop any element that makes it longer than the k. 
Return the root afterwards, as that will be the smallest on the heap(or kth largest).

Time complexity: O(n)
Space complexity: O(c)
"""

from typing import List

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
        

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
