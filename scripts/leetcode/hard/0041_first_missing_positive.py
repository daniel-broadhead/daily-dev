"""
Problem: first missing positive (LeetCode #41)
Link: https://leetcode.com/problems/first-missing-positive
Date: 2025-09-23

Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Approach:
- Convert the input to a set. Start a check at 1 and see if the check is in the set. If it is, increase the set. Go until result found.

Time complexity: O(n)
Space complexity: O(1)
"""

from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_set = set(nums) #set of all nums, removes duplicates
        check = 1
        while True: #inifinite loop, only exits when broken, like by the return below
            if check not in nums_set:
                return check
            check += 1
        

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
