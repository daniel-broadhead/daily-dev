"""
Problem: power of two (LeetCode #231)
Link: https://leetcode.com/problems/power-of-two

Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

Approach:
First check if n is 1 (2^0) or 2 (2^1). Return True. check if n is odd or negative. Return false. Recurse with n // 2 until bool. 
Proud of this one needing very little syntax help, and b/c did it while holding napping baby. 

Bonus learned that can use bitwise AND (&) to check instantly. B/c binary powers of 2 are 10000....., and -1 is 0111111..... so
n & (n - 1) is quick trick. 

Time complexity: O(logn)
Space complexity: O(1)
"""

from typing import List

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1 or n == 2:
            return True
        elif n <= 0 or n % 2 != 0: #og missed checking is positive
            return False
        else:
            return self.isPowerOfTwo(n // 2) #og missedreturn statement

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
