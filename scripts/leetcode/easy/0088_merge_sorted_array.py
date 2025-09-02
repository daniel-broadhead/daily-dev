"""
Problem: merge sorted array (LeetCode #88)
Link: https://leetcode.com/problems/merge-sorted-array/
Date: 2025-09-02

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the 
last n elements are set to 0 and should be ignored. nums2 has a length of n.

Approach:
- Starting at the end of each list(m, n), see which value is larger, and insert that at the end of nums1(m + n).

Time complexity: O(n)
Space complexity: O(c)
"""

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j, k = m - 1, n - 1, m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
# Example test
if __name__ == "__main__":
    # Add test cases
    pass
