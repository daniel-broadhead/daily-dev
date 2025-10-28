"""
Problem: 4sum II (LeetCode #454)
Link: https://leetcode.com/problems/4sum-ii/
Date: 2025-10-28

Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

Approach:
- Since the target is 0, it works best to find all the sums where a+b = -(c + d) and it works best to do that with a hashmap. I originally 
missed the target being 0, and so was stuck for a good bit. 

Time complexity: O(n^2)
Space complexity: O(n^2)
"""

from typing import List
from collections import Counter

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = 0
        ab_sum = Counter(a + b for a in nums1 for b in nums2)
        for c in nums3:
            for d in nums4:
                count += ab_sum.get(-(c + d), 0)
        return count
        
# Example test
if __name__ == "__main__":
    # Add test cases
    pass
