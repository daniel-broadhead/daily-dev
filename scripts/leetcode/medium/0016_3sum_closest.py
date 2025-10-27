"""
Problem: 3sum closest (LeetCode #16)
Link: https://leetcode.com/problems/3sum-closest
Date: 2025-10-24

Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Approach:
- I'm fantastic at finding brute force solutions, but struggle at thinking in CS logic, for smartness and efficiency. So the idea is to 
have 2 pointers on the sorted list and check each combination for each item, and find the smallest difference. 

Time complexity: O(?)
Space complexity: O(?)
"""

class Solution:
    def threeSumClosest(self, nums, target: int):
        nums.sort() #first sort the list for two pointer
        closest_sum = float('inf') #init variable
        min_diff = float('inf') #init another variable

        for i in range(len(nums) - 2): #for each set of 3
            left, right = i + 1, len(nums) - 1 

            while left < right: #2 pointer problem
                curr_sum = nums[i] + nums[left] + nums[right] #find the current sum
                diff = abs(curr_sum - target) #check for the difference

                if diff < min_diff: #when found difference is less than current min
                    min_diff = diff #update
                    closest_sum = curr_sum #update

                if curr_sum < target: #adjust left pointer
                    left += 1
                elif curr_sum > target: #adjust right pointer
                    right -= 1
                else: #exact match
                    return curr_sum

        return closest_sum
        
# Example test
if __name__ == "__main__":
    # Add test cases
    pass
