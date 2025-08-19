"""
Problem: number of zero-filled subarrays (LeetCode #2348)
Link: https://leetcode.com/problems/number-of-zero-filled-subarrays

Given an integer array nums, return the number of subarrays filled with 0.

A subarray is a contiguous non-empty sequence of elements within an array.

Approach:
Keep track of previous zeroes for each index behind current element. sum those up and  return sum

Time complexity: O(?)
Space complexity: O(?)
"""

from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        subarrays = 0
        prev_zeroes = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                prev_zeroes += 1
                subarrays += prev_zeroes
            else:
                prev_zeroes = 0
        return subarrays

                
        

        

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
