"""
Problem: convert integer to sum of two no-zero integers (LeetCode #1317)
Link: https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers
Date: 2025-09-08

No-Zero integer is a positive integer that does not contain any 0 in its decimal representation.

Given an integer n, return a list of two integers [a, b] where:

a and b are No-Zero integers.
a + b = n
The test cases are generated so that there is at least one valid solution. If there are many valid
 solutions, you can return any of them.

Approach:
- Initially I went with a numbers only logic which took the module of 10 and checked for +/- 1 or 2. That didn't work very well for later 
test cases. So I looped over all ints less than n, and checked i, and n - i for no zeroes. I converted a and b to str to check for 0.

Time complexity: O(n)
Space complexity: O(1)
"""

from typing import List

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            a, b = i, n - i
            if "0" in str(a) or "0" in str(b):
                continue
            return a, b
        

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
