"""
Problem: ransom note (LeetCode #383)
Link: https://leetcode.com/problems/ransom-note/

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Approach:
- I am proud of myself for this one b/c I needed minimal help to get it working, and debugged on my own. Small wins. Place all the letters
from the magazine string into a dictionary. Increasing count for each letter. For each letter in ransom note, check if it is in dictionary
and if count is more than 0. If loop through successfully, return True. 

Time complexity: O(m + n)
Space complexity: O(1)
"""

from typing import List

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_letters = {}
        for letter in magazine:
            if letter in mag_letters:
                mag_letters[letter] += 1
            else:
                mag_letters[letter] = 1
        for letter in ransomNote:
            if letter in mag_letters:
                if mag_letters[letter] == 0:
                    return False
                mag_letters[letter] -= 1
            else:
                return False
        return True

        

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
