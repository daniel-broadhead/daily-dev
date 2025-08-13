"""
Problem: power of three (LeetCode #326)
Link: https://leetcode.com/problems/power-of-three

[Write a brief description or paste the original prompt here.]

Approach:
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.

Time complexity: O(log3n)
Space complexity: O(1)
"""

from typing import List

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
