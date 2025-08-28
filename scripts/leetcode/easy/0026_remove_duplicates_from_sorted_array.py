"""
Problem: remove duplicates from sorted array (LeetCode #26)
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.

Approach:
- Have a counter of the last unique element seen. Iterate through list, and when a new unique element is found, shift the counter 1 to the 
right and change the value at that index to the new unique. Return count of unique + 1 at the end, to reflect unique elements. 

Time complexity: O(n)
Space complexity: O(1)
"""

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: #empty list case
            return 0
        
        unique = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[unique]:
                unique += 1
                nums[unique] = nums[i]
        return unique + 1

        
        

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
