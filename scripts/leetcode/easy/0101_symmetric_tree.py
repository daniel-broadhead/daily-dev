"""
Problem: symmetric tree (LeetCode #101)
Link: https://leetcode.com/problems/symmetric-tree
Date: 2025-10-22

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Approach:
- Use deques to check each pair for symmetry. 

Time complexity: O(c)
Space complexity: O(c)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSymmetric(self, root) -> bool:
        if not root:
            return True
        q = deque([(root.left, root.right)]) #start with root's kiddos
        while q:
            t1, t2 = q.popleft() #pop those off and check the first
            if not t1 and not t2: #if both empty, symmetric
                continue
            if not t1 or not t2 or t1.val != t2.val: #conditions for failing
                return False
            q.append((t1.left, t2.right)) #next pairs to check
            q.append((t1.right, t2.left))

        return True
        

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
