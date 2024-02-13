# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        dic = {}
        curA = headA
        while curA:
            dic[curA] = 1
            curA = curA.next
        curB = headB
        while curB:
            if curB in dic:
                return curB
            curB = curB.next
        