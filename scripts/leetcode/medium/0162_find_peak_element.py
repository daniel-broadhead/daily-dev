"""
Problem: find peak element (LeetCode #162)
Link: https://leetcode.com/problems/find-peak-element

A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

Approach:
- Another BS problem. Check if the middle element is greater than the middle plus 1 element. Look at the greater half and repeat until peak found.


Time complexity: O(logn)
Space complexity: O(1)
"""

from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left


# Example test
if __name__ == "__main__":
    # Add test cases
    pass
