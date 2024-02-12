# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current1 = list1
        current2 = list2
        merged = []
        
        while current1:
            merged.append(current1.val)
            current1 = current1.next
                
        while current2:
            merged.append(current2.val)
            current2 = current2.next
        merged.sort()
        
        result = ListNode()
        curr = result
        for i in merged:
            node = ListNode(i)
            curr.next = node
            curr = curr.next
        return result.next
        

        