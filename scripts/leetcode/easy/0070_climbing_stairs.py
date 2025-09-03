"""
Problem: climbing stairs (LeetCode #70)
Link: https://leetcode.com/problems/climbing-stairs
Date: 2025-09-03

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Approach:
- Using a dynamic programming approach, like I learned in class, I notice the pattern. Then I store values for the base cases, and add
the values for the other cases as it goes, so as to not need to remath each time. 

Time complexity: O(n)
Space complexity: O(n)
"""

from typing import List

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: #n ways if n is 2 or less
            return n
        dp = [0] * (n + 1) #0th index is unused, n + 1 to account for python indexing
        dp[1], dp[2] = 1, 2 #store these base cases
        for i in range(3, n + 1): #iterate after base cases
            dp[i] = dp[i - 1] + dp[i - 2] #fibo sequence
        return dp[n]
        

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
