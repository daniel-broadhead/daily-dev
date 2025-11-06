"""
Problem: Search in rotated sorted array (LeetCode #33)
Link: https://leetcode.com/problems/search-in-rotated-sorted-array
Date: 2025-11-05

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Approach:
- Really weird conceptually at first, but works fine with binary search. Just check which half is still sorted, because one always will be. Then
scan the sorted half for the target. Repeat until target found.

Time complexity: O(logn)
Space complexity: O(c)
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            #if mid is target 
            if nums[mid] == target:
                return mid

            # 2 cases, left or right half is sorted

            if nums[left] <= nums[mid]: #left half sorted
                if nums[left] <= target < nums[mid]: #target is on left half
                    right = mid - 1 #now examine the left half
                else:
                    left = mid + 1
            else: #right half sorted
                if nums[mid] < target <= nums[right]: #target is on right half
                    left = mid + 1
                else:
                    right = mid - 1
        return - 1

        

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
