# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle point of the list
        slow, fast = head, head.next
        #O(n) time
        while fast and fast.next: # while either fast is null or fast is at the end
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        prev = slow.next = None
        while second: #reverse the second list
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        #merge two halves
        first = head #beginning of first
        second = prev #end of second
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
