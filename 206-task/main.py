from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# iterative
def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return

    prev_node, curr_node = head, head.next
    prev_node.next = None
    while curr_node:
        tmp = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = tmp

    return prev_node


# recursive
def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None or head.next is None:
        return head

    new_head = reverseList(head.next)

    next_node = head.next
    curr_node = head

    next_node.next = curr_node
    curr_node.next = None

    return new_head


def printListNode(head: Optional[ListNode]) -> None:
    curr = head
    while curr:
        print(f"{curr.val} ->", end=" ")
        curr = curr.next
    print()


if __name__ == "__main__":
    head1 = ListNode(1, ListNode(2, ListNode(3)))
    res1 = reverseList(head1)
    printListNode(res1)

    head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    res2 = reverseList(head2)
    printListNode(res2)

    head3 = ListNode(1)
    res3 = reverseList(head3)
    printListNode(res3)

    head4 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    res4 = reverseList(head4)
    printListNode(res4)

    head5 = ListNode(1, ListNode(2))
    res5 = reverseList(head5)
    printListNode(res5)
