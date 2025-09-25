"""
Problem: find all numbers disappeared in an array (LeetCode #448)
Link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
Date: 2025-09-25

Given an array nums of n integers where nums[i] is in the range [1, n],
 return an array of all the integers in the range [1, n] that do not appear in nums

Approach:
- Trivial if using extra space or more than O(n), so we gon do constant space and O(n). Use array as pointers and negate numbers at indices
if the index is present as a value in the list. Go through the array and check for positive values. Add + 1 to the index and append to result.


Time complexity: O(n)
Space complexity: O(c)
"""

from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums: #use array as a list of pointers, marking indices as - if present
            idx = abs(num) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]

        result = []

        for i in range(len(nums)): #check for negative indices, return positive
            if nums[i] > 0:
                result.append(i + 1) #i + 1 because 0th index
        
        return result

        

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
