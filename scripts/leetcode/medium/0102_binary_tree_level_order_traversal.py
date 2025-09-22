"""
Problem: binary tree level order traversal (LeetCode #102)
Link: https://leetcode.com/problems/binary-tree-level-order-traversal
Date: 2025-09-22

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Approach:
- Use a queue to hold the items from the next level. When going through that level pop the things off the front of the queue(fifo) and 
append to the level. Append the level to the results afterwards. 

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
from collections import deque

class Solution:
    def levelOrder(self, root) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = deque([root]) #start the queue with the root

        while queue: #while things are in the queue
            level = [] #need to return level by level so this checks per level
            for _ in range(len(queue)): #len queue is how many items are in the next level

                node = queue.popleft() #popleft is a function of deque, removes the front of the queue. so functions like a queue(fifo)
                level.append(node.val) #slap that bad boy's value onto the result

                if node.left: #check for left
                    queue.append(node.left)
                if node.right: #check for right
                    queue.append(node.right) 
            
            result.append(level)

        return result


        

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
