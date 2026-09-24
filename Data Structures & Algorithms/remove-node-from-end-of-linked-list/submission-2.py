# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next = head)

        curr = dummy
        for i in range(n + 1):
            curr = curr.next

        removalNode = dummy
        while curr:
            curr = curr.next
            removalNode = removalNode.next

        removalNode.next = removalNode.next.next

        return dummy.next

        
        