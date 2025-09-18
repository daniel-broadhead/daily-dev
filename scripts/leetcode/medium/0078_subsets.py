"""
Problem: subsets (LeetCode #78)
Link: https://leetcode.com/problems/subsets
Date: 2025-09-18

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Approach:
- Very similar to permutations(46). Add subsets to the result as iterate and recurse through the nums. Backtrack when reach end of path.

Time complexity: O(?)
Space complexity: O(?)
"""

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(start, path): #backtrack is also dfs which i also need to practice
            result.append(path[:]) #add copy of current path to results
            for i in range(start, len(nums)):
                path.append(nums[i]) #append to path
                backtrack(i + 1, path) #move to next index with current path
                path.pop() #when path ends, pop last elements. will pop again if needed
        backtrack(0, []) #starts backtrack with info. 
        return result #win

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
