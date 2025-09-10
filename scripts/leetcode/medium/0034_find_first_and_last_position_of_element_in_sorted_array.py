"""
Problem: find first and last position of element in sorted array (LeetCode #34)
Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array
Date: 2025-09-10

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Approach:
- Searching with o(logn) time screams binary search. But trickiness lies if the mid element is the desired element.
 Is it the first or last index or in between? So use 2 binary searches! One for the start, and one for the end positions. 


Time complexity: O(logn)
Space complexity: O(1)
"""

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #2 binary searches to find the first and last index
        left = 0
        right = len(nums) - 1
        start = -1
        end = -1
        while left <= right: #find the start pos
            mid = (left + right) // 2
            if nums[mid] == target:
                start = mid
                right = mid -1 #keep looking left
            elif nums[mid] < target:
                left = mid + 1 #keep looking right
            else:
                right = mid - 1 #keep looking left

        left = 0
        right = len(nums) - 1
        while left <= right: #find the end pos
            mid = (left + right) // 2
            if nums[mid] == target:
                end = mid
                left = mid + 1 #keep looking right for end
            elif nums[mid] > target:
                right = mid - 1 #keep looking left
            else:
                left = mid + 1 #keep looking right
        return [start, end]
        

        

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
