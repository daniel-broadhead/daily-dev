"""
Problem: find pivot index (LeetCode #724)
Link: https://leetcode.com/problems/find-pivot-index/

Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

Approach:
- First approach was On^2 and that is inefficient. Second approach involves a running sum count. First calc the total sum, and init 
left sum to 0. Then enumerate through the list and compare the left sum to the total sum - prev left sum - current number. If true return i


Time complexity: O(n)
Space complexity: O(1)
"""

from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            if left_sum == total_sum - left_sum - num:
                return i
            left_sum += num
        return -1
        
# Example test
if __name__ == "__main__":
    # Add test cases
    pass
