# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=0
        temp = head
        curr=[]
        while head!= None:
            l+=1
            head=head.next
        print(l)
        s = l //2 -1
        while s >=0:
            temp = temp.next
            s -= 1
        print(temp)
        return temp

        