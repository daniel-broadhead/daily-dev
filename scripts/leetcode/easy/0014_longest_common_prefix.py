"""
Problem: longest common prefix (LeetCode #14)
Link: https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Approach:
- Store the first word as a comparison. On second thought could store the shortest word but not sure if that would make a noticeable difference.
Compare each word, character by character to the first word, adding to the prefix when valid, and exiting and returning the prefix when complete or 
missed character encountered.

Time complexity: O(nm)
Space complexity: O(c)
"""

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        hold = strs[0]
        for i in range(len(hold)):
            char = hold[i]
            for word in strs[1:]:
                if i >= len(word) or word[i] != char:
                    return prefix
            prefix += char
        return prefix
                

        
# Example test
if __name__ == "__main__":
    # Add test cases
    pass
