"""
Problem: find the duplicate number (LeetCode #287)
Link: https://leetcode.com/problems/find-the-duplicate-number/
Date: 2025-09-24

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.

Approach:
- The tricky part here is solving the problem with the given reqs. Constant time and not modifying the array. W/out those I could just create
a seen map. But. So the algo is the use the tortoise and hard idea. If they both run, they run until they find each other in a loop. Reset
slow to the start of the track, and make them have the same space. They will meet at the duplicate(start of loop) at same time.

Time complexity: O(n)
Space complexity: O(1)
"""

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True: #finding the cycle within this list
            slow = nums[slow] #value points to next index, like a linked list
            fast = nums[nums[fast]] #like above but faster
            if slow == fast: #cycle found
                break #leave that loop
        slow = nums[0] #reset the slow to the start
        while slow != fast: #fast is now the same # of steps from start of loop(duplicate) as slow
            slow = nums[slow] #so they move same pace
            fast = nums[fast]
        return slow

        
# Example test
if __name__ == "__main__":
    # Add test cases
    pass
