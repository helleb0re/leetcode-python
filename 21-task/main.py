from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    fake_head_new_list = ListNode()
    curr_node_new_list = fake_head_new_list

    while list1 and list2:

        if list1.val <= list2.val:
            curr_node_new_list.next = list1
            list1 = list1.next
        else:
            curr_node_new_list.next = list2
            list2 = list2.next

        curr_node_new_list = curr_node_new_list.next

    if list1:
        curr_node_new_list.next = list1
    elif list2:
        curr_node_new_list.next = list2

    return fake_head_new_list.next


def printListNode(head: Optional[ListNode]) -> None:
    curr = head
    while curr:
        print(f"{curr.val} ->", end=" ")
        curr = curr.next
    print()


if __name__ == "__main__":
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    printListNode(list1)
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    printListNode(list2)
    res1 = mergeTwoLists(list1, list2)
    printListNode(res1)
