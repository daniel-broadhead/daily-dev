"""
Problem: Valid Anagram (LeetCode #242)
Link: https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Approach:
- First compare that the lengths of the two strings are equal. They must be for a valid anagram. Next create an empty array of 26 boxes.
Use ord(ch1) - ord('a') to get usuable indices of the boxes. Iterate using zip through both strings, adding to the array if a letter is in
s, subtracting if the letter is in t. After iteration check if the count in each box is 0, if true, it's a valid anagram.

Time complexity: O(n)
Space complexity: O(1)
"""

from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): #Check if lengths are equal. 
            return False
        count = [0] * 26 #Create empty array of 26 boxes
        for ch1, ch2 in zip(s, t): #Zip iterates through both s and t, and groups the vars at each index together. Must be same len
            count[ord(ch1) - ord('a')] += 1 #ord returns unicode point, so use ord-ord to get usable indices
            count[ord(ch2) - ord('a')] -= 1 #adding and subtracting from array lets net 0 = same char count for that box
        return all(c == 0 for c in count) #return true if each box is 0


# Example test
if __name__ == "__main__":
    # Add test cases
    pass
