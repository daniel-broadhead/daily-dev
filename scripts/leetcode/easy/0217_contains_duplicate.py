"""
Problem: Contains Duplicate (LeetCode #217)
Link: https://leetcode.com/problems/contains-duplicate/

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Approach:
- Iterate through the array of integer nums, and return True if any have been seen. If not, store that num in a set for future comparisons.

Time complexity: O(n)
Space complexity: O(n)
"""

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else: 
                seen.add(num)
        return False
        

        

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
