"""
Problem: reverse linked list (LeetCode #206)
Link: https://leetcode.com/problems/reverse-linked-list
Date: 2025-09-05

Given the head of a singly linked list, reverse the list, and return the reversed list.

Approach:
- Change each next pointer to the item behind it. 

Time complexity: O(n)
Space complexity: O(n)
"""

from typing import List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            nxt = curr.next #store the next for use
            curr.next = prev #currents next pointer is now backwards
            prev = curr #move prev pointer up
            curr = nxt #move curr pointer up
        return prev
        
# Example test
if __name__ == "__main__":
    # Add test cases
    pass
