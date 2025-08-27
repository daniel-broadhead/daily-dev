"""
Problem: permutation in string (LeetCode #567)
Link: https://leetcode.com/problems/permutation-in-string/

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 
Approach:
- Create hash tables of the frequencies in the strings. For the second string(where I'm checking the substrings) use a sliding window to
look at each window of length s1. 

Time complexity: O(n)
Space complexity: O(1)
"""

from typing import List

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = [0] * 26 #2 hash tables for frequencies of chars
        freq2 = [0] * 26
        for char in s1: #fill first table
            freq1[ord(char) - ord('a')] += 1

        for char in s2[:len(s1)]: #take the first window of len(s1)
            freq2[ord(char) - ord('a')] += 1

        if freq1 == freq2: #check if that first window matches
            return True

        for i in range(len(s1), len(s2)): #starts loop at index len(s1) to include first window, then goes for len(s2) to include all windows
            freq2[ord(s2[i]) - ord('a')] += 1 #add next char to hash
            freq2[ord(s2[i - len(s1)]) - ord('a')] -= 1 #remove last char from hash
            if freq1 == freq2:
                return True
        return  False

        
        
# Example test
if __name__ == "__main__":
    # Add test cases
    pass
