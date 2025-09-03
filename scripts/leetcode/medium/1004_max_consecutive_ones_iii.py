"""
Problem: max consecutive ones iii (LeetCode #1004)
Link: https://leetcode.com/problems/max-consecutive-ones-iii
Date: 2025-09-03

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Approach:
- Sliding window approach where I maintain the # of zeroes in the subarray. When the number is too high I move the left index until I encounter
another zero. 

Time complexity: O(n)
Space complexity: O(1)
"""

from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        max_len = 0
        zero_counter = 0
        for right in range(len(nums)): #moving the right end of the window
            if nums[right] == 0:
                zero_counter += 1
            while zero_counter > k: #moving the left end of the window
                if nums[left] == 0: #check for 0, because will be moving past that spot
                    zero_counter -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len




        

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
