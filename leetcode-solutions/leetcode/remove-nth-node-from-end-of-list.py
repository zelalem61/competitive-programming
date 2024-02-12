# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        cur = head
        while cur:
            size+=1
            cur = cur.next
        target = size - n
        if target == 0:
            head = head.next
            return head
        newCur = head
        while target > 1:
            newCur = newCur.next
            target-=1
        newCur.next = newCur.next.next
        return head