"""
Problem: sqrt(x) (LeetCode #69)
Link: https://leetcode.com/problems/sqrtx/
Date: 2025-09-02

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

#NICE

Approach:
- Binary search all the values less than x. Check if the middle value * itself == x. Adjust parameters as needed.

Time complexity: O(logn)
Space complexity: O(1)
"""

from typing import List

class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif (mid * mid) < x:
                left = mid + 1
            else:
                right = mid - 1
        return right
        
# Example test
if __name__ == "__main__":
    # Add test cases
    pass
