"""
Problem: Two Sum (LeetCode #1)
Link: https://leetcode.com/problems/two-sum/description/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Approach:
- Practicing with hashtables, my approach is to store the numbers, and compare the stored numbers to the current index number. 
If the numbers add to the target, return the indices. If not, store the number at the current index.

Time complexity: O(n)
Space complexity: O(n))
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

# Example test
if __name__ == "__main__":
    print(Solution().twoSum([2, 7, 11, 15], 9))
