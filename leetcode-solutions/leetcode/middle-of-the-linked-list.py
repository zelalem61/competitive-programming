# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        curr = head
        while curr:
            curr = curr.next
            n +=1
        middle = (n // 2)+1
        remo = 1
        result = ListNode()
        curre = result
        while head:
            if remo >= middle:
                curre.next = ListNode(int(head.val))
                curre = curre.next
            head = head.next
            remo += 1
        return result.next

            
            
                
            
        