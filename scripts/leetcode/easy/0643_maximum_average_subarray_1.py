"""
Problem: maximum average subarray 1 (LeetCode #643)
Link: https://leetcode.com/problems/maximum-average-subarray-i/

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
Any answer with a calculation error less than 10-5 will be accepted.

Approach:
- [Explain your approach here]

Time complexity: O(n) 
Space complexity: O(1)
"""

from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k]) #initialize the window to the sum of the first k values
        max_sum = window_sum #initialize the max sum to the current window sum

        for i in range(k, len(nums)): #going through indices(i) of the numbers in the list of nums, starting at the kth index
            window_sum += nums[i] - nums[i - k] #update the window sum to include the ith index and without the i-kth index
            max_sum = max(max_sum, window_sum) #update max_sum to the max of old and new window sum
        
        return max_sum / k #return the max sum and divide by k for average

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
