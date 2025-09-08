"""
Problem: maximum product subarray (LeetCode #152)
Link: https://leetcode.com/problems/maximum-product-subarray
Date: 2025-09-08

Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Approach:
- Kadane's algorithm with an extra variable, tracking minimum for when a double negative is encountered. 

Time complexity: O(n)
Space complexity: O(1)
"""

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far = nums[0] #essentially kadane's algo, but with extra element
        min_so_far = nums[0] #this min tracking can account for encountered negatives cancelling
        result = nums[0]
        for num in nums[1:]:
            temp_max = max_so_far #hold prev max
            temp_min = min_so_far #hold prev min
            max_so_far = max(num, num * temp_max, num * temp_min)
            min_so_far = min(num, num * temp_max, num * temp_min)
            result = max(max_so_far, result)
        return result


        
# Example test
if __name__ == "__main__":
    # Add test cases
    pass
