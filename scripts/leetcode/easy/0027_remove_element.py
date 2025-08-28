"""
Problem: remove element (LeetCode #27)
Link: https://leetcode.com/problems/remove-element/

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.

Approach:
- Very similar to last problem. Did with 0 help which was a win for noob me. Gonna start tracking the date I do these problems on. 
2 pointer problem. Check if right is the value, shift right 1 left if it is. Else if left is value, swap left with right. Else, shift left
1 right. Incrementing count of valid entries. 

Time complexity: O(n)
Space complexity: O(1)
"""

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        right = len(nums) - 1
        left = 0
        count = 0
        while left <= right:
            if nums[right] == val:
                right -= 1
            elif nums[left] == val:
                dummy = nums[left]
                nums[left] = nums[right]
                nums[right] = dummy
                left += 1
                right -= 1
                count += 1
            else:
                count += 1
                left += 1
            print(nums)
        return count

        

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
