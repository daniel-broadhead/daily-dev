"""
Problem: binary tree postorder traversal (LeetCode #145)
Link: https://leetcode.com/problems/binary-tree-postorder-traversal/
Date: 2025-09-20

Given the root of a binary tree, return the postorder traversal of its nodes' values

Approach:
- Postorder traversal is left, right, root. Using a stack to avoid the trivial recursive solution, we first visit the root. Then we append 
the left then right to the stack. Stacks are lifo, so when appending the values to the result it is returned in root - right - left, which
when reversed gives the correct order.

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
    def postorderTraversal(self, root) -> List[int]:
        if not root:
            return []
        stack, result = [root], []
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result[::-1] #reverses the root - right - left to the correct postorder of left - right - root
        

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
