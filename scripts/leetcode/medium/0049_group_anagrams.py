"""
Problem: Group anagrams (LeetCode #49)
Link: https://leetcode.com/problems/group-anagrams/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Approach:
- Import the defaultdict from collection. This is useful because it will auto assign values to keys, without needing keys. Create variable
anagrams, and defaultdict(list) which tells it to make a list for each key entry. Iterate through the strs, and sort each word. The sorted word
is the key in the defaultdict and the values are the unsorted words. Return the values from the defaultdict. 

Time complexity: O(n*k logk) (looping over each strs(n) once, and sorting each word is k logk)
Space complexity: O(n*k) (storing n words of k length)
"""

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))
            anagrams[key].append(word)
        return list(anagrams.values())

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
