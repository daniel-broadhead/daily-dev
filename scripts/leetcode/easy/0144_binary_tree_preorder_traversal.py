"""
Problem: binary tree preorder traversal (LeetCode #144)
Link: https://leetcode.com/problems/binary-tree-preorder-traversal
Date: 2025-09-20

Given the root of a binary tree, return the preorder traversal of its nodes' values.

Approach:
- Using stacks for the iteration, first examine the root. Then visit the right node and append to stack, then the left node. This will ensure
correct preorder when returning result.

Time complexity: O(n)
Space complexity: O(c)
"""

from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root) -> List[int]:
        if not root:
            return []
        stack, result = [root], [] #python lists are essentially stacks
        while stack:
            node = stack.pop() #order is root
            result.append(node.val)
            if node.right: #right added first to stack so will be last
                stack.append(node.right)
            if node.left: #left added after right to stack so appended value before right
                stack.append(node.left)
        return result #result is root - left - right


        

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
