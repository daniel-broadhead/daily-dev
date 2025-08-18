"""
Problem: contains duplicate ii (LeetCode #219)
Link: https://leetcode.com/problems/contains-duplicate-ii/

Given an integer array nums and an integer k, return true if there are two distinct indices i and j 
in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Approach:
- Using a hashmap, keep track of the last index a number was seen at. When encountering a number that is in the hashmap, check for the 
condition with k. Update hashmap and proceed if needed.

Time complexity: O(n)
Space complexity: O(n)
"""

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_seen = {} #hashmap for last time a num was seen
        for i, num in enumerate(nums): #enumerate through list of nums
            if num in last_seen and i - last_seen[num] <= k: #check for conditions
                    return True #win
            last_seen[num] = i #if num not in hashmap, update hashmap for num
        return False #win


# Example test
if __name__ == "__main__":
    # Add test cases
    pass
