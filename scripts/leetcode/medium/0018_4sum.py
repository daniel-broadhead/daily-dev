"""
Problem: 4sum (LeetCode #18)
Link: https://leetcode.com/problems/4sum
Date: 2025-10-27

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Approach:
- Fix 2 numbers using nested loops, and then do 2 pointers to find all the potential solns, skipping duplicates.

Time complexity: O(n^3)
Space complexity: O(c)
"""

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 3): #fix the first number
            if i > 0 and nums[i] == nums[i - 1]: #skip duplicates
                continue

            for j in range(i + 1, n - 2): #fix the second number
                if j > i + 1 and nums[j] == nums[j - 1]: #skip duplicates
                    continue

                left, right = j + 1, n - 1

                while left < right: #2 pointers to find solns
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])

                        while left < right and nums[left] == nums[left + 1]: #skip duplicates
                            left += 1
                        
                        while left < right and nums[right] == nums[right - 1]: #skip duplicates
                            right -= 1

                        left += 1
                        right -= 1
                    
                    elif total < target:
                        left += 1
                    
                    else:
                        right -= 1

        return result
        
# Example test
if __name__ == "__main__":
    # Add test cases
    pass
