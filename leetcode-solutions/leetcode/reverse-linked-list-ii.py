# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        z = []
        while(head):
            z.append(head.val)
            head = head.next
        while(left < right):
            z[left-1] , z[right-1] = z[right-1] , z[left-1]
            left+=1
            right-=1
        a = b =ListNode(0)
        for i in z:
            a.next = ListNode(i)
            a = a.next
        return b.next
