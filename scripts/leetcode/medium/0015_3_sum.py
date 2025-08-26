"""
Problem: 3 sum (LeetCode #15)
Link: https://leetcode.com/problems/3sum/

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets

Approach:
- Using math that x + y + z = 0 is same as y + z = - x, set x, and 2 sum y and z. Do that for all x. 

Time complexity: O(n^2)
Space complexity: O(n)
"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #sort list 
        solution_set = [] #be returning a list of solutions
        n = len(nums) 
        for i in range(n): #for each item on the list
            if i > 0 and nums[i] == nums[i - 1]: #check for duplicates
                continue #skip duplicates

            target = -nums[i] # nums[i] + nums[j] + nums[k] = 0 rearranges to nums[j] + nums[k] = -nums[i]
            j = i + 1 
            k = n - 1
            while j < k: 
                current_sum = nums[j] + nums[k] #convenience
                if current_sum == target: #soln found
                    solution_set.append([nums[i], nums[j], nums[k]])
                    j += 1 #move pointers
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]: #check for dups
                        j += 1
                    while j < k and nums[k] == nums[k + 1]: # '' 
                        k -= 1
                elif current_sum < target: #need make current sum bigger so move j
                    j += 1
                else:# need smaller, move k
                    k -= 1 
        
        return solution_set

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
