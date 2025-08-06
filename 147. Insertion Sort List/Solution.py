# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        h=head
        while h:
            l.append(h.val)
            h=h.next 
        h=head
        l.sort()
        i=0
        while h:
            h.val=l[i]
            i+=1 
            h=h.next 
        return head

        