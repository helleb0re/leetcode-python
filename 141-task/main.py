from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def hasCycle(head: Optional[ListNode]) -> bool:
    slow, fast = head, head

    while fast:
        slow = slow.next
        fast = fast.next.next if fast.next else fast.next

        if slow == fast != None:
            return True

    return False


if __name__ == "__main__":
    head = ListNode(3)
    curr_node = head
    curr_node.next = ListNode(2)
    curr_node = curr_node.next
    save_node = curr_node
    curr_node.next = ListNode(0)
    curr_node = curr_node.next
    curr_node.next = ListNode(4)
    curr_node = curr_node.next
    curr_node.next = save_node
    assert hasCycle(head)

    head = ListNode(3, ListNode(2, ListNode(0, ListNode(4))))
    assert not hasCycle(head)
