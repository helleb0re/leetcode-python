from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev_node, curr_node = None, head

    while curr_node:
        tmp = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = tmp

    return prev_node, head


# my solution
def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    prev_node, curr_node, new_head = head, head, head
    last_sub_tail = None

    i = 1
    while curr_node:
        if i % k == 0:
            tmp = curr_node.next
            curr_node.next = None

            new_sub_head, new_sub_tail = reverseList(prev_node)
            new_sub_tail.next = tmp

            if i == k:
                new_head = curr_node

            if last_sub_tail:
                last_sub_tail.next = new_sub_head
            last_sub_tail = new_sub_tail

            prev_node = tmp
            curr_node = tmp
        else:
            curr_node = curr_node.next
        i += 1

    return new_head


# neetcode solution
def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    group_prev = dummy

    def getKth(node, k):
        while node and k > 0:
            node = node.next
            k -= 1
        return node

    while kth := getKth(group_prev, k):
        group_next = kth.next

        # reverse kth part of the list
        prev_node, curr_node = kth.next, group_prev.next
        while curr_node != group_next:
            tmp = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = tmp

        tmp = group_prev.next
        group_prev.next = kth
        group_prev = tmp

    return dummy.next


def printListNode(head: Optional[ListNode]) -> None:
    curr = head
    while curr:
        print(f"{curr.val} ->", end=" ")
        curr = curr.next
    print()


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    res = reverseKGroup(head, 2)
    printListNode(res)
