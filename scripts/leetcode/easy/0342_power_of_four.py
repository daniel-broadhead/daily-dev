"""
Problem: power of four (LeetCode #342)
Link: https://leetcode.com/problems/power-of-four

Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x

Approach:
- Basically the same approach as power of three. Almost works with the power of two bitwise trick, but needs some extra code.

Time complexity: O(logn)
Space complexity: O(1)
"""

from typing import List

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        #all powers of 4 are powers of 2, except 2. 
        if n < 1: #first check if n is less than 1, if so is false.
            return False
        while n % 4 == 0: #as long as n can be moduled by 4 with no remainder
            n //= 4 #update n to n divided by 4
        return n == 1 #return true if becomes 1. 

        

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
