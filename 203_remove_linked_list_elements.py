from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return None

        if head.val == val:
            # Remove head.

            return self.removeElements(head.next, val)

        tail = self.removeElements(head.next, val)
        head.next = tail
        return head

def list_to_nodelist(list):
    head = ListNode(list[0])
    current_node = head
    for i in range(1, len(list)):
        node = ListNode(list[i])
        current_node.next = node
        current_node = current_node.next

    # print_linked_list(head)


    return head

def print_linked_list(head):
    # Print the list.
    current_node = head
    print("Printing list node:")
    while current_node:
        print(current_node.val)
        current_node = current_node.next


if __name__ == '__main__':
    list = [1, 2, 6, 3, 4, 5, 6]
    node_list = list_to_nodelist(list)
    sol = Solution().removeElements(node_list, 6)
    print_linked_list(sol)
