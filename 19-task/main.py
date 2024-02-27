from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# my solution (only explanation-1)
def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    slow_pointer, fast_pointer = head, head
    prev_slow_pointer = None

    k = 0
    while fast_pointer:
        fast_pointer = fast_pointer.next

        if k < n:
            k += 1
            continue

        prev_slow_pointer = slow_pointer
        slow_pointer = slow_pointer.next

    if prev_slow_pointer is None:
        head = slow_pointer.next
    else:
        prev_slow_pointer.next = slow_pointer.next

    return head


# neetcode solution (explanation-1 and -2)
def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    fake_head = ListNode(0, head)
    slow_pointer, fast_pointer = fake_head, head

    for _ in range(n):
        fast_pointer = fast_pointer.next

    while fast_pointer:
        fast_pointer = fast_pointer.next
        slow_pointer = slow_pointer.next

    slow_pointer.next = slow_pointer.next.next
    return fake_head.next


def printListNode(head: Optional[ListNode]) -> None:
    curr = head
    while curr:
        print(f"{curr.val} ->", end=" ")
        curr = curr.next
    print()


if __name__ == "__main__":
    head1 = ListNode(1, ListNode(2, ListNode(3)))
    res1 = removeNthFromEnd(head1, 3)
    printListNode(res1)

    head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    res2 = removeNthFromEnd(head2, 5)
    printListNode(res2)

    head3 = ListNode(1)
    res3 = removeNthFromEnd(head3, 1)
    printListNode(res3)

    head4 = ListNode(
        1,
        ListNode(
            2,
            ListNode(
                3,
                ListNode(
                    4,
                    ListNode(
                        5,
                        ListNode(
                            6, ListNode(7, ListNode(8, ListNode(9, ListNode(10))))
                        ),
                    ),
                ),
            ),
        ),
    )
    res4 = removeNthFromEnd(head4, 8)
    printListNode(res4)

    head5 = ListNode(1, ListNode(2))
    res5 = removeNthFromEnd(head5, 2)
    printListNode(res5)
