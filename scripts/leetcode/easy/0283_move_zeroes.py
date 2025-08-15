"""
Problem: move zeroes (LeetCode #283)
Link: https://leetcode.com/problems/move-zeroes/

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Approach:
- This was surprisingly difficult for me to visualize. First attempt involved poping the 0s, and appending them to the end. That failed
because the iteration wouldn't account for the pop changing the indices. Successful attempt was using two pointers and switching non zeroes
with the farthest left zero.

Time complexity: O(n)
Space complexity: O(1)
"""

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        last = 0 #init index to start of list
        for i in range(len(nums)): #for each index
            if nums[i] != 0: #if the value at the index is 0, do nothing and move on. if it isn't 0...
                nums[i], nums[last] = nums[last], nums[i] #swap the number with the farthest left 0
                last += 1 #move last(farthest left 0) 1 index right
                #return nothing
        
# Example test
if __name__ == "__main__":
    # Add test cases
    pass
