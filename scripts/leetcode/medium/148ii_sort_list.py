"""
Problem: sort list (LeetCode #148ii)
Link: https://leetcode.com/problems/sort-list/description/
Date: 2025-09-12

Given the head of a linked list, return the list after sorting it in ascending order.

Approach:
- This time I am using a merge sort practice, since that is effective for linked lists and I need practice. 

Time complexity: O(logn)
Space complexity: O(logn)
"""

from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head
        #1st split the list
        mid = self.get_middle(head)
        right_half = mid.next #uses above half
        mid.next = None #now the list is split

        #sort each half
        left_sorted = self.sortList(head)
        right_sorted = self.sortList(right_half)

        #merge the sorteds
        return self.merge(left_sorted, right_sorted)

    #first helper function to find middle
    def get_middle(self, head):
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow #slow is middle of list
    
    #second helper function, to merge the lists
    def merge(self, left, right):
        dummy = ListNode(0)
        tail = dummy

        while left and right:
            if left.val <= right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        tail.next = left if left else right
        return dummy.next

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
