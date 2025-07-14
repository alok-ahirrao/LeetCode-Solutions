# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        curr = head
        summ = 0
        list1 = []
        while curr:
            list1.append(curr.val)
            curr= curr.next

        list1 = list1[::-1]
        
        for i in range(len(list1)):
            print(i)
            print(list1[i])
            if list1[i] ==1 :
                summ += 2 ** i

        return summ


        