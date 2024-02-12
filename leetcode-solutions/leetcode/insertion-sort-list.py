# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        pointer = head
        while pointer:
            res.append(pointer.val)
            pointer = pointer.next
        
        res.sort()
        
        pointer = head
        i = 0
        while pointer:
            pointer.val = res[i]
            i+= 1
            pointer = pointer.next
        
        return head
        