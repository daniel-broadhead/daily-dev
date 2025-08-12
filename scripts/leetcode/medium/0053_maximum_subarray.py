"""
Problem: maximum subarray (LeetCode #53)
Link: https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the subarray with the largest sum, and return its sum.

Approach:
- I initially tried treating this like a sliding windows problem which ended in disaster. The correct soln is called Kadane's algorithm,
and iterates through the list from start to end, checking if each value is larger than the current sum. If it is then it resets the current sum
to that value. This locates the greatest subarray.

Time complexity: O(n)
Space complexity: O(1)
"""

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0] #init current to whatever first value is
        largest_sum = nums[0] #init to whatever first value is
        
        for num in nums[1:]: #for each value starting at index1(second value)
            current_sum = max(num, current_sum + num) #compare if the value alone is larger than previous sum
            largest_sum = max(largest_sum, current_sum) #largest_sum resets to large positives when found
        return largest_sum
        
# Example test
if __name__ == "__main__":
    # Add test cases
    pass
