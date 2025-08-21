"""
Problem: search insert position (LeetCode #35)
Link: https://leetcode.com/problems/search-insert-position

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.



Approach:
- Classic binary search, good practice for me w/my background. Set left and right to the ends of the list. Mid is the middle of the list.
Check middle of list and adjust the left or right depending on if middle is lower or higher than target. 

Time complexity: O(logn)
Space complexity: O(1)
"""

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left      
# Example test
if __name__ == "__main__":
    # Add test cases
    pass
