"""
Problem: Palindrome Number (LeetCode #9)
Link: https://leetcode.com/problems/palindrome-number/

Given an integer x, return true if x is a palindrome, and false otherwise.

Approach:
- Convert the integer to a string and compare the first and last digits, stepping closer together. Return true if true.

Time complexity: O(n)
Space complexity: O(1)
"""

from typing import List

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
