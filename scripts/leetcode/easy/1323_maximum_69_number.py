"""
Problem: maximum 69 number (LeetCode #1323)
Link: https://leetcode.com/problems/maximum-69-number

You are given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

Approach:
- Use string methods to replace the first 6 with a 9. 

Time complexity: O(1)
Space complexity: O(1)
"""

from typing import List

class Solution:
    def maximum_69_number(self, num):  # Update params
        return int(str(num).replace("6", "9", 1))

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
