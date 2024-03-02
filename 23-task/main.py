from typing import Optional, List
from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# O(k*n) solution
def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    dummy = ListNode()
    curr_node = dummy
    MAX_VALUE = 10**4 + 1

    while True:
        min_node = ListNode(MAX_VALUE)
        min_node_index = -1

        for i, node in enumerate(lists):
            if node and min_node.val > node.val:
                min_node = node
                min_node_index = i

        if min_node_index == -1:
            break

        curr_node.next = min_node
        curr_node = curr_node.next
        lists[min_node_index] = lists[min_node_index].next

    return dummy.next


def mergeTwoLists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    curr_node = dummy
    while l1 and l2:

        if l1.val <= l2.val:
            curr_node.next = l1
            l1 = l1.next
        else:
            curr_node.next = l2
            l2 = l2.next

        curr_node = curr_node.next

    if l1:
        curr_node.next = l1
    elif l2:
        curr_node.next = l2

    return dummy.next


# O(n*logk) solution
def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    d = deque(lists)

    while len(d) > 1:
        l1, l2 = d.popleft(), d.popleft()

        new_l = mergeTwoLists(l1, l2)

        d.append(new_l)

    return d[0] if d else None


def printListNode(head: Optional[ListNode]) -> None:
    curr = head
    while curr:
        print(f"{curr.val} ->", end=" ")
        curr = curr.next
    print()


if __name__ == "__main__":
    head1 = ListNode(1, ListNode(4, ListNode(5)))
    head2 = ListNode(1, ListNode(3, ListNode(4)))
    head3 = ListNode(2, ListNode(6))
    res = mergeKLists([head1, head2, head3])
    printListNode(res)

    res = mergeKLists([None, None])
    printListNode(res)
