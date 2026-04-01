# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 3 -> 2 -> 1
        # 6 -> 5 -> 4
        # 3 + 6 -> 2 + 5 -> 1 + 4 = 9 -> 7 -> 5

        # 9 -> 4
        # 9 -> 
        # 9 + 9 -> 1 + 4 + null (0) ->
        # 8 -> 5 ->

        curr1 = l1
        curr2 = l2
        carry = 0
        res = ListNode()
        prev = res
        #O(m + n) t
        #O(1) s
        while curr2 or curr1 or carry: #as long as one is not null, we continue
            if not curr1:
                add1 = 0
            else:
                add1 = curr1.val
            if not curr2:
                add2 = 0
            else:
                add2 = curr2.val

            val = (carry + add1 + add2) % 10
            carry = (carry + add1 + add2) // 10

            prev.next = ListNode(val)
            prev = prev.next
            
            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None
        return res.next






            