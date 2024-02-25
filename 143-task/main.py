from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# time: O(n); space: O(n)
def reorderList(head: Optional[ListNode]) -> None:
    if not head:
        return

    tail = head.next
    buffer = []
    r = 0
    while tail:
        buffer.append(tail)
        r += 1
        tail = tail.next

    curr = head
    n = r
    while r > 0:
        tail = buffer.pop()

        tmp = curr.next
        curr.next = tail
        tail.next = tmp
        curr = tail.next

        r -= 2

    if n % 2 == 1:
        curr = curr.next

    curr.next = None


# my solution
# time: O(n); space: O(1)
def reorderList(head: Optional[ListNode]) -> None:
    if not head or not head.next:
        return

    slow, fast = head, head.next
    while fast.next:
        slow = slow.next

        if not fast.next.next:
            fast = fast.next
        else:
            fast = fast.next.next

    curr_node = slow.next
    prev_node = slow.next = None
    while curr_node:
        tmp = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = tmp

    first, second = head, fast
    while second:
        tmp1 = first.next
        tmp2 = second.next

        first.next = second
        second.next = tmp1

        first = tmp1
        second = tmp2


# neetcode solution
# time: O(n); space: O(1)
def reorderList(head: Optional[ListNode]) -> None:
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    second = slow.next
    prev_node = slow.next = None
    while second:
        tmp = second.next
        second.next = prev_node
        prev_node = second
        second = tmp

    first, second = head, prev_node
    while second:
        tmp1, tmp2 = first.next, second.next

        first.next = second
        second.next = tmp1

        first, second = tmp1, tmp2


def printListNode(head: Optional[ListNode]) -> None:
    curr = head
    while curr:
        print(f"{curr.val} ->", end=" ")
        curr = curr.next
    print()


if __name__ == "__main__":
    # head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    # reorderList(head1)
    # printListNode(head1)

    # head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    # reorderList(head2)
    # printListNode(head2)

    # head3 = ListNode(1, ListNode(2))
    # reorderList(head3)
    # printListNode(head3)

    head4 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    reorderList(head4)
    printListNode(head4)
