"""
Problem: reorder list (LeetCode #143)
Link: https://leetcode.com/problems/reorder-list/
Date: 2025-09-06

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed

Approach:
- Using fast and slow pointers, find the middle of the list. Reverse the second list. Merge the two lists together 1 node at a time. 

Time complexity: O(N)
Space complexity: O(C)
"""

from typing import List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head) -> None:
        if not head.next: #cases for no list or list of 1
            return head
        slow, fast = head, head
        while fast and fast.next: #slow fast pointer to find middle of list
            slow = slow.next
            fast = fast.next.next
        #reverse the second half
        prev, curr = None, slow.next
        slow.next = None #splits list
        while curr:#from reverse linked list problem
            nxt = curr.next  #stores normal next
            curr.next = prev #curr points backwards now(to none at init)
            prev = curr #move prev counter up
            curr = nxt #move curr counter to the store
        #merge two halves
        first, second = head, prev
        while second: #while there is second half(would be shorter if not same length)
            tmp1, tmp2 = first.next, second.next #store the normal nexts
            first.next = second #head points to second
            second.next = tmp1 #second points to next first
            first, second = tmp1, tmp2 #restore first, second -- repeat


        """
        Do not return anything, modify head in-place instead.
        """
        

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
