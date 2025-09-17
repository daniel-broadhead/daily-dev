"""
Problem: permutation (LeetCode #46)
Link: https://leetcode.com/problems/permutations/
Date: 2025-09-17

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Approach:
- Check each number and index for each spot moving backwards. 

Time complexity: O(n * n!)
Space complexity: O(1)
"""

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [] #hold permutations

        def backtrack(path, used): #recursive helper
            if len(path) == len(nums): #if same length as list
                perms.append(path[:]) #add a slice of it to the perms
                return #move on
            for i in range(len(nums)): #for as many indices as there are nums in list
                if i in used: #if seen that number
                    continue
                path.append(nums[i]) #add that num to the path
                used.add(i) #add index to used set(no duplicates)
                backtrack(path, used) #do it over again
                # reverse the choice 
                path.pop() #take last added thing off
                used.remove(i) #take i out of used to check again
            
        backtrack([], set()) #inits backtrack with a empty dict and empty set for path,used
        return perms
        

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
