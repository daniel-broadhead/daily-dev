"""
Problem: length of last word (LeetCode #58)
Link: https://leetcode.com/problems/length-of-last-word
Date: 2025-08-30

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Approach:
- Starting from the end of the list, use 2 loops. First loop to pass the trailing spaces. Second loop to count the chars in the word.

Time complexity: O(n)
Space complexity: O(1)
"""

from typing import List

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #find last non space char, (start loop from rear) and count the letters
        count = 0
        i = len(s) - 1
        while i >= 0 and s[i] == " ": #get past the trailing spaces
            i -= 1
        while i >= 0 and s[i] != " ": #count the chars in that last word
            count += 1
            i -= 1
        return count
            

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
