class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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