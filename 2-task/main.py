from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getNodeValue(node: Optional[ListNode]) -> int:
    return 0 if node is None else node.val


def goToNextNode(node: Optional[ListNode]) -> Optional[ListNode]:
    return node if node is None else node.next


# iterative
def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    curr_node = dummy
    overflow = 0

    while l1 or l2 or overflow:
        res_of_add = getNodeValue(l1) + getNodeValue(l2) + overflow
        overflow = res_of_add // 10

        curr_node.next = ListNode(res_of_add % 10)
        curr_node = curr_node.next

        l1, l2 = goToNextNode(l1), goToNextNode(l2)

    return dummy.next


# recursive
def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    curr_node = dummy

    def helper(node1, node2, overflow):
        if node1 is None and node2 is None and overflow == 0:
            return

        res_of_add = getNodeValue(node1) + getNodeValue(node2) + overflow
        overflow = res_of_add // 10

        nonlocal curr_node
        curr_node.next = ListNode(res_of_add % 10)
        curr_node = curr_node.next

        helper(goToNextNode(node1), goToNextNode(node2), overflow)

    helper(l1, l2, 0)

    return dummy.next


def printListNode(head: Optional[ListNode]) -> None:
    curr = head
    while curr:
        print(f"{curr.val} ->", end=" ")
        curr = curr.next
    print()


if __name__ == "__main__":
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    res = addTwoNumbers(l1, l2)
    printListNode(res)

    l1 = ListNode(
        9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))
    )
    l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    res = addTwoNumbers(l1, l2)
    printListNode(res)

    l1 = ListNode(2, ListNode(4, ListNode(9)))
    l2 = ListNode(5, ListNode(6, ListNode(4, ListNode(9))))
    res = addTwoNumbers(l1, l2)
    printListNode(res)
