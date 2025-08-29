"""
Problem: find the index of the first occurrence in a string (LeetCode #28)
Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string
Date: 2025-08-29

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Approach:
- Sick brain is not permitting me to learn the KMP algo(I believe that is the bones of find), so using python find() I can one line this. 

Time complexity: O(n+m)
Space complexity: O(1)
"""

from typing import List

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
        
# Example test
if __name__ == "__main__":
    # Add test cases
    pass
