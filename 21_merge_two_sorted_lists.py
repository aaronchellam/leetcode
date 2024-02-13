# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        current = dummy

        # Iterate through both lists until one of them becomes empty.
        while list1 and list2:
            # Compare the values of the nodes and merge in ascending order.
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next

            else:
                current.next = list2
                list2 = list2.next

            # Move the current pointer to the next node in the mergd list.
            current = current.next

        # If there are remaining nodes in list1 or list2, append them to the merged list.
        if list1:
            current.next = list1
        else:
            current.next = list2

        return dummy.next





        # p1 = list1
        # p2 = list2
        #
        # # newlist = list1 if p1.val <= p2.val else list2
        #
        # if p1.val <= p2.val:
        #     newlist = p1
        #     p1 = p1.next
        # else:
        #     newlist = p2
        #     p2 = p2.next
        #
        # while not list1 and not list2:
        #     if p1.val <= p2.val or not p2.val:
        #         newlist.next = p1
        #         list1 = list1.next
        #     else:
        #         newlist.next = list2
        #         list2 = list2.next


