"""
Problem: palindrome linked list (LeetCode #234)
Link: https://leetcode.com/problems/palindrome-linked-list
Date: 2025-09-09

Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Approach:
- Use fast and slow pointers to find the middle of the linked list. Reverse the second half of the list(from where the slow pointer ends).
Check each list. 2nd half will be reversed so checking the last one will really be checking the first, and moving forwards. Bit tricky logic to visualize.


Time complexity: O(n)
Space complexity: O(1)
"""

from typing import List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:
        slow = head
        fast = head
        while fast and fast.next: #find the middle of the list
            slow = slow.next
            fast = fast.next.next

        if fast: #if odd length(there is a fast but not a fast.next)
            slow = slow.next #bump slow to the middle value
            
        #now slow is mid. 
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        #now 2nd half is reversed
        check1 = head
        check2 = prev
        while check2:  
            if check1.val != check2.val:
                return False
            check1 = check1.next
            check2 = check2.next
        return True     

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
