# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        listLen = 0

        curr = head
        while curr:
            listLen += 1
            curr = curr.next

        dummy = ListNode(next=head)

        removalIdx = listLen - n 
        pos = 0
        curr = dummy
        while curr:
            if pos == removalIdx:
                curr.next = curr.next.next
                break

            pos += 1
            curr = curr.next

        return dummy.next
        