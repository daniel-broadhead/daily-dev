"""
Problem: search in rotated sorted array ii (LeetCode #81)
Link: https://leetcode.com/problems/search-in-rotated-sorted-array-ii
Date: 2025-11-06

There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.

Approach:
- Much like problem 33. Check which half is sorted, see if target fits in that range. Check if it does, look other side if not. But check for 
duplicates before that and shrink list if left, mid, and right have same number value, with index check.

Time complexity: O(logn)
Space complexity: O(c)
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1

        while left <= right: 
            mid = (left + right) // 2

            if nums[mid] == target:
                return True
            
            while left < right and nums[left] == nums[mid] == nums[right]: #difference from 33, shrink list if numbers are the same. has list bounds check too.
                left += 1
                right -= 1
            
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False

        

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
