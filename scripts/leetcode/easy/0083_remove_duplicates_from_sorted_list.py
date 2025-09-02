"""
Problem: remove duplicates from sorted list (LeetCode #83)
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
Date: 2025-09-02

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Approach:
- If a node and its next node have the same value, have that current node's pointer redirect to the node following. 

Time complexity: O(c)
Space complexity: O(c)
"""

from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head):
        current = head #create variable for current node, so as to not mess up head
        while current and current.next: #while both things exist(ie within linked list)
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
            

        

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
