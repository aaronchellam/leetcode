from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_linkedlist(list):
    if len(list) == 0:
        return None

    next_node = list_to_linkedlist(list[1:])
    return ListNode(val=list[0], next=next_node)


def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    size = 0
    current = head
    while current is not None:
        size += 1
        current = current.next

    middle_index = (size // 2) + 1

    current = head
    current_position = 1

    while current_position < middle_index:
        current_position += 1
        current = current.next

    return current


def middleNode2(head: Optional[ListNode]) -> Optional[ListNode]:
    # Use two pointers - one traverses the linked list faster than the others.
    fast = slow = head

    while fast and fast.next:
        fast, slow = fast.next.next, slow.next
    return slow


mid_node = middleNode(list_to_linkedlist([1, 2, 3, 4, 5]))

print(mid_node.val)
print(mid_node.next.val)
