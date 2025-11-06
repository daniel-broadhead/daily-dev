"""
Problem: find minimum in rotated sorted array (LeetCode #153)
Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array
Date: 2025-11-06

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Approach:
- Pythonic solution is cheating. return min(nums). So I did it a better way.

Time complexity: O(logn)
Space complexity: O(c)
"""

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                # min is to the right
                left = mid + 1
            else:
                # mid could be the min, so include it
                right = mid
        return nums[left]


# Example test
if __name__ == "__main__":
    # Add test cases
    pass
