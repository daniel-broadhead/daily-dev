"""
Problem: linked list cycle (LeetCode #141)
Link: https://leetcode.com/problems/linked-list-cycle
Date: 2025-09-05

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Approach:
- Relying on the logic that a cycle is essentially a circle. Treat 2 pointers like 2 runners. If the faster runner/pointer lands on the same
position as the slow, then it is a cycle. If not a cycle then this won't happen. Guaranteed to happen if it is a cycle though. 

Time complexity: O(n)
Space complexity: O(1)
"""

from typing import List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        slow = head #2 pointers, like running around a track
        fast = head #the fast moves 2 pos at a time
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: #if fast lands on same as slow(because it's a cycle)
                return True
        return False #not a cycle
        

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
