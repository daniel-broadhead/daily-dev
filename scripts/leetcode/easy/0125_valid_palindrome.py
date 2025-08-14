"""
Problem: valid palindrome (LeetCode #125)
Link: https://leetcode.com/problems/valid-palindrome/

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Approach:
- First remove the non-alphanumeric characters with the re package. Then convert all uppercase into lowercase with text.lower().
Finally reverse the string with slicing[::-1](start at end and step backwards by 1). Return true if equal.

Time complexity: O(n)
Space complexity: O(1)
"""

from typing import List

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', s) #replaces all characters not in brackets with empty string '' from input s
        lower_cleaned = cleaned.lower() #lowercases the cleaned
        reversed_string = lower_cleaned[::-1] #reverses the lower_cleaned
        return lower_cleaned == reversed_string

        

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
