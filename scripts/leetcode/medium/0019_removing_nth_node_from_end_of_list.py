"""
Problem: removing nth node from end of list (LeetCode #19)
Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
Date: 2025-09-06

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Approach:
- Count the number of nodes in the list. Move pointer to the counter - n - 1 and remove that node, by assigning the prev node's next to 
next.next. Return head. 

Time complexity: O(2l)
Space complexity: O(c)
"""

from typing import List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int):
        left = 0
        right = head
        counter = 0
        new_head = head
        while right: #find how many nodes there are
            right = right.next
            counter += 1 #at end of loop, counter should store how many nodes
        if n == counter: #for when return the first 
            return head.next
        while left < counter - n - 1: #move left pointer to the counter - nth node
            left += 1
            new_head = new_head.next

        new_head.next = new_head.next.next

        return head #returning listwithout the deletion
        

        

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
