"""
Problem: top k frequent elements (LeetCode #347)
Link: https://leetcode.com/problems/top-k-frequent-elements
Date: 2025-11-13

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Approach:
- Counter counts all the times a variable appears. Python makes heapq easy for returning k most frequent. 

Time complexity: O(logn)
Space complexity: O(logn)
"""

from typing import List

import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = Counter(nums) #counter package gets count of each num

        largest_k = heapq.nlargest(k, counts.keys(), key = counts.get) # type: ignore #returns k largest from counts iterable, using counts.get for comparison
        #counts.items is the key/number, and counts.get is the # of times seen

        return largest_k

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
