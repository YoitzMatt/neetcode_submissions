# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        
         # get the length of the list 
        start, res = head, head
        len_l = 0
        while start != None:
            len_l += 1
            start = start.next   

        if n == len_l:
            new_head = head.next
            head.next = None
            return new_head 
        
        index = 0
        target = len_l - n
        while head != None:
            if index == target - 1:
                nth = head.next
                head.next = nth.next
                nth.next = None
            head = head.next 
            index += 1
        return res