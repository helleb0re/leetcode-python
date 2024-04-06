from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        buffer = deque([root])
        res = ""
        while buffer:
            curr_node = buffer.popleft()

            if curr_node:
                res += str(curr_node.val) + ","

                buffer.append(curr_node.left)
                buffer.append(curr_node.right)

            else:
                res += "null,"

        return res[:-1]

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        root = None

        buffer = data.split(",")[::-1]
        queue = deque([])

        while buffer:
            curr_node_val = buffer.pop()

            curr_node = (
                TreeNode(int(curr_node_val)) if curr_node_val != "null" else None
            )

            if queue:
                match queue[0][1]:
                    case "wait_left_child":
                        queue[0][0].left = curr_node
                        queue[0][1] = "wait_right_child"
                    case "wait_right_child":
                        queue[0][0].right = curr_node
                        queue[0][1] = "complete"
                    case _:
                        raise RuntimeError()

                if queue[0][1] == "complete":
                    queue.popleft()

            if curr_node is not None:
                queue.append([curr_node, "wait_left_child"])
                if root is None:
                    root = curr_node

        return root


def printTree(root):
    buffer = [root]

    while buffer:
        tmp_buffer = []
        for elem in buffer:
            print(elem.val, end=" ")

            if elem.left:
                tmp_buffer.append(elem.left)

            if elem.right:
                tmp_buffer.append(elem.right)
        print()

        buffer.clear()
        buffer += tmp_buffer


if __name__ == "__main__":
    # root = TreeNode(
    #     5,
    #     TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
    #     TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))),
    # )
    # root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    root = TreeNode(1)
    codec = Codec()
    db = codec.serialize(root)
    print(db)
    rroot = codec.deserialize(db)
    printTree(rroot)
