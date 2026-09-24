# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverse(head):
            prev, curr = None, head

            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            return prev

        curr = head

        while curr:
            curr.next = reverse(curr.next)
            curr = curr.next
        