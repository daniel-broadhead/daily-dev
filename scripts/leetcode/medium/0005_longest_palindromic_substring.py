"""
Problem: Longest palindromic substring (LeetCode #5)
Link: https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, return the longest palindromic substring in s.

Approach:
- Expand outwards from each character, checking if left and right are equal. Compare these substrings to the longest found.

Time complexity: O(n^2)
Space complexity: O(n)
"""

from typing import List

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_from_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1: right]
        longest = ""
        for i in range(len(s)):
            p1 = expand_from_center(i, i)
            p2 = expand_from_center(i, i + 1)
            if len(p1) > len(longest):
                longest = p1
            if len(p2) > len(longest):
                longest = p2
        return longest

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
