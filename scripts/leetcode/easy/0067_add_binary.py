"""
Problem: add binary (LeetCode #67)
Link: https://leetcode.com/problems/add-binary/
Date: 2025-09-01

Given two binary strings a and b, return their sum as a binary string.

Approach:
- Reverse both strings. Zip strings together and look character by character, considering 3 logic cases and append results together, then
convert from list to string

Time complexity: O(c)
Space complexity: O(c)
"""

from typing import List
from itertools import zip_longest

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0 # to carry over when a value grows
        result = [] #list which will be conv to string at end

        for x, y in zip_longest(reversed(a), reversed(b), fillvalue = '0'): #allows zip to go to longest, reverse a and b to start at end
            x, y = int(x), int(y) #convert to int for addition
            if x == 1 and y == 1: #3 cases, with 2 subcases each
                if carry == 1:
                    result.append('1')
                    carry = 1
                else:
                    result.append('0')
                    carry = 1
            
            elif x == 1 or y == 1:
                if carry == 1:
                    result.append('0')
                    carry = 1
                else:
                    result.append('1')
                    carry = 0
            
            else:
                if carry == 1:
                    result.append('1')
                    carry = 0
                else:
                    result.append('0')
                    carry = 0
        
        if carry == 1:
            result.append('1')
        
        return "".join(reversed(result)) #convert from list to string


# Example test
if __name__ == "__main__":
    # Add test cases
    pass
