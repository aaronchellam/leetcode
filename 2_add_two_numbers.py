from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next





class Solution:

    # Iterate through both lists and perform the addition at each digit.
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a new list node to store the result.
        dummy = ListNode() # empty dummy head
        current = dummy
        carry = 0 # create a variable to store the carry for each addition

        # While there are digits to add or a carry, perform addition.
        while l1 or l2 or carry:
            sum = carry

            if l1:
                sum += l1.val
                l1 = l1.next

            if l2:
                sum += l2.val
                l2 = l2.next


            current.next = ListNode(sum % 10)
            current = current.next
            carry = sum // 10

        return dummy.next





# if __name__ == '__main__':
#     la = ListNode(2)
#     lb = ListNode(4)
#     lc = ListNode(3)
#
#     la.next = lb
#     lb.next = lc
#
#     sol = Solution()
#
#     print(sol.addTwoNumbers(la, la))