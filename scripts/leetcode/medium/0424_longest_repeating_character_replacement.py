"""
Problem: longest repeating character replacement (LeetCode #424)
Link: https://leetcode.com/problems/longest-repeating-character-replacement

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Approach:
- Maintain the count of characters inside the window. The current valid window is sized to whatever the most frequent char is - the allowed switches.


Time complexity: O(n)
Space complexity: O(1)
"""

from typing import List
from collections import defaultdict #enables avoiding key error for dict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = defaultdict(int) #keep dict of the count of each char found
        left = 0 #left index 
        max_freq = 0 #keep track of  the maxfreq of a char
        best = 0 #maintain the best substring found

        for right, char in enumerate(s): #checking each char while maintaining right
            char_count[char] += 1 #increase count
            max_freq = max(max_freq, char_count[char]) #determine max

            while (right - left + 1) - max_freq > k: #if window size - chars to replace is more than allowed
                char_count[s[left]] -= 1 #shrink window
                left += 1 #shrink window
            
            best = max(best, right - left + 1) #check best against current window size
        
        return best

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
