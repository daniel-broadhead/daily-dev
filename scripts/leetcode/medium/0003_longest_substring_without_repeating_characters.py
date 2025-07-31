"""
Problem: longest substring without repeating characters (LeetCode #0003)
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without duplicate characters

Approach:
- I use a sliding window with two pointers(left and right) to represent the current longest substring without repeating characters. 

Time complexity: O(n)
Space complexity: O(min(n,m))
"""

from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        result = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            result = max(result, right - left + 1)

        return result


# Example test
if __name__ == "__main__":
    # Add test cases
    pass
