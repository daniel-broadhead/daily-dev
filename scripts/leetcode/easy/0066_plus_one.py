"""
Problem: plus one (LeetCode #66)
Link: https://leetcode.com/problems/plus-one/
Date: 2025-08-30

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Approach:
- Beginning at the least sig place, the end of the list. Check if 9. If 9 set to 0 and move up the list. If at end of iteration
add a new place with a 1. If no 9 then add is trivial

Time complexity: O(n)
Space complexity: O(1)
"""

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1): #starting at the end of the list(least sig)
            if digits[i] == 9: #if 9, have to add further up list
                if i == 0: #if at last(first) entry, add a new value
                    digits[i] = 0
                    digits.insert(0, 1)
                    break #exit loop cause done
                digits[i] = 0 #9 + 1 == 10 which is 0 for that place
            else: #if not 9 is trivial
                digits[i] += 1
                break
        return digits #gg
            
# Example test
if __name__ == "__main__":
    # Add test cases
    pass
