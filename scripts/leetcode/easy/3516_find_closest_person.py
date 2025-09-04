"""
Problem: find closest person (LeetCode #3516)
Link: https://leetcode.com/problems/find-closest-person
Date: 2025-09-04

You are given three integers x, y, and z, representing the positions of three people on a number line:

x is the position of Person 1.
y is the position of Person 2.
z is the position of Person 3, who does not move.
Both Person 1 and Person 2 move toward Person 3 at the same speed.

Determine which person reaches Person 3 first:

Return 1 if Person 1 arrives first.
Return 2 if Person 2 arrives first.
Return 0 if both arrive at the same time.
Return the result accordingly.

Approach:
- Trivial, compare the distances between x and z, and y and z. 

Time complexity: O(c)
Space complexity: O(c)
"""

from typing import List

class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        dist_x = abs(z - x)
        dist_y = abs(z - y)
        if dist_x == dist_y:
            return 0
        elif dist_x < dist_y:
            return 1
        else:
            return 2
        

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
