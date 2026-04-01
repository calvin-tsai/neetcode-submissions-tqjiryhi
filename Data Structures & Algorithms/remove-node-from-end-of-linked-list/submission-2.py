# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        temp = head
        for _ in range(n): # move temp n away from curr
            if not temp:
                break
            temp = temp.next
        if not temp:
            return head.next
        while temp.next: # move them both until temp is null meaning curr is at the desired location
            curr = curr.next
            temp = temp.next
        
        curr.next = curr.next.next
        return head