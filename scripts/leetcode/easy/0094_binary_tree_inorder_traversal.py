"""
Problem: binary tree inorder traversal (LeetCode #94)
Link: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2025-09-19

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Approach:
- Recurse through each node's left child. When no more left children, visit parent, then right nodes. 

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
    def inorderTraversal(self, root) -> List[int]:
        result = [] 

        def inorder(node):
            if not node: #when no more node
                return
            inorder(node.left) #first visit the left (repeats until no more left)
            result.append(node.val) #add its value to result (this is also where root gets visited)
            inorder(node.right) #visit the rights

        inorder(root) #start at root
        return result #return result O.o 
        
        
# Example test
if __name__ == "__main__":
    # Add test cases
    pass
