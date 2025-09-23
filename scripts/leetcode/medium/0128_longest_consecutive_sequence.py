"""
Problem: longest consecutive sequence (LeetCode #128)
Link: https://leetcode.com/problems/longest-consecutive-sequence
Date: 2025-09-23

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Approach:
- Convert nums to a set for o(1) lookup time. Find first num that doesnt have n-1 in the set, and start the sequence. Go through all 
nums in sequence and update the length for consecutive sequences and return the longest length.

Time complexity: O(n)
Space complexity: O(1)
"""

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int: #cant use python sort cuz thats cheating yo
        num_set = set(nums) #remove duplicates and can find in o1 time
        longest = 0 #init to 0
        for num in num_set: #for each number in the set
            if num - 1 not in num_set: #only start counting if at start of a sequence
                length = 1
                while num + length in num_set: #check for each number while extending seqn
                    length += 1
                longest = max(longest, length)
        return longest


        

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
