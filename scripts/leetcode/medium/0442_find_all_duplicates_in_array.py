"""
Problem: find all duplicates in array (LeetCode #442)
Link: https://leetcode.com/problems/find-all-duplicates-in-an-array/
Date: 2025-09-24

Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears at most twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant auxiliary space, excluding the space needed to store the output

Approach:
- Tricky again due to time and space constraints. Use the array of nums as a marker for if I've visited  before. Go from each number to
the inex it points to. If it's negative there, then append the original number to the results. If not negative, switch it to negative.

Time complexity: O(n)
Space complexity: O(1)
"""

from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = [] #store our answer(all space alloted)
        for num in nums: #go through each number, using list as our markers
            index = abs(num) - 1 #account for 0 index
            if nums[index] < 0: #if the number at index is - means we visited already
                result.append(abs(num)) #so add to result
            else: #otherwise flip to -
                nums[index] = -nums[index]
        return result
        

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
