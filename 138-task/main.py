from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


# my solution
def copyRandomList(head: "Optional[Node]") -> "Optional[Node]":
    dummy = Node(0)
    curr_new_node, curr_node = dummy, head

    old_node_to_new_node = {}
    while curr_node:
        curr_new_node.next = Node(curr_node.val)
        # link old_node with new_node. Example: OldNode(7) -> NewNode(7)
        old_node_to_new_node[curr_node] = curr_new_node.next

        curr_new_node = curr_new_node.next
        curr_node = curr_node.next

    curr_new_node = dummy.next
    curr_node = head
    while curr_node:
        curr_new_node.random = old_node_to_new_node.get(curr_node.random, None)

        curr_new_node = curr_new_node.next
        curr_node = curr_node.next

    return dummy.next


# optimized (thanks neetcode!)
def copyRandomList(head: "Optional[Node]") -> "Optional[Node]":
    curr_node = head
    old_node_to_new_node = {None: None}
    while curr_node:
        # link old_node with new_node. Example: OldNode(7) -> NewNode(7)
        old_node_to_new_node[curr_node] = Node(curr_node.val)
        curr_node = curr_node.next

    curr_node = head
    while curr_node:
        old_node_to_new_node[curr_node].next = old_node_to_new_node[curr_node.next]
        old_node_to_new_node[curr_node].random = old_node_to_new_node[curr_node.random]

        curr_node = curr_node.next

    return old_node_to_new_node[head]


def printNode(head: Optional[Node]) -> None:
    curr = head
    while curr:
        s = f"{curr.val} -> {curr.random.val if curr.random else 'None'}"
        s += "\n{:^{width}}".format("↓", width=len(s))
        print(s)
        curr = curr.next
    print()


if __name__ == "__main__":
    nodes = [Node(7), Node(13), Node(11), Node(10), Node(1)]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    nodes[0].random = None
    nodes[1].random = nodes[0]
    nodes[2].random = nodes[4]
    nodes[3].random = nodes[2]
    nodes[4].random = nodes[0]
    res = copyRandomList(nodes[0])
    printNode(res)
