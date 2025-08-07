"""
Problem: minimum size subarray sum (LeetCode #209)
Link: https://leetcode.com/problems/minimum-size-subarray-sum/

Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is 
greater than or equal to target. If there is no such subarray, return 0 instead.

Approach:
- My initial approach was a brute force approach, calculating the sum of each subarray in the array, using for start in len, for end in len,
but that was inefficient. Continuing practice with the sliding window shows its efficiency. I init window sum and left to 0, and the size 
of the min subarray to inf. Then expand the size of the window until its value is greater than or equal to target. While true, shrink the
window by moving left + 1. Check if that is the new min size and save, then keep on. Return the min value after complete iteration, or 0.

Time complexity: O(n)
Space complexity: O(1)
"""

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window_sum = 0 #init to 0
        min_length = float('inf') #everything is less than inf
        left = 0 #counter to 0, used in while loop
        for right in range(len(nums)): #for every right value in subarray
            window_sum += nums[right] #window sum grows with value of current right
            
            while window_sum >= target: #when window is greater or equal than target:
                min_length = min(min_length, right - left + 1) #check if min length is smaller than last min length. right - left + 1 b/c python [] doesnt include end bracket. 
                window_sum -= nums[left] #shrink value of window sum by subtracting current left value
                left += 1 #shift left 1 to the right
            
        return min_length if min_length != float('inf') else 0

        

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
