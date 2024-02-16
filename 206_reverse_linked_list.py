# Definition for singly-linked list.
from utils.linked_list_utils import list_to_nodelist, print_linked_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:


        def reverse_recursive(current, prev):
            # Check if the current node is None.
            # If it is, return the previous node.
            if not current:
                return prev

            next_node = current.next
            current.next = prev
            return reverse_recursive(next_node, current)

        return reverse_recursive(head, None)


if __name__ == '__main__':
    list = list_to_nodelist([1,2,3])
    sol = Solution().reverseList(list)
    print_linked_list(sol)