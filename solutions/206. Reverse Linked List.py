# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        else:
            cur = head
            nxt = head.next
            head.next = None
            while nxt is not  None:
                cur = nxt
                nxt = nxt.next
                cur.next = head
                head = cur
            return head
