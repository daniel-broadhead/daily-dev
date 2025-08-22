"""
Problem: first bad version (LeetCode #278)
Link: https://leetcode.com/problems/first-bad-version

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Approach:
- Binary search through the versions until finding the first bad. Do this by setting left to 1, and right to n. Mid is found with 
left + right // 2. Use the API to check the mid. Update left/right according to results.

Time complexity: O(logn)
Space complexity: O(1)
"""

from typing import List
# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
