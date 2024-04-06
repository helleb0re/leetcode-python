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
        res = []

        def preorder_dfs(node):
            if node is None:
                res.append("null")
                return

            res.append(str(node.val))
            preorder_dfs(node.left)
            preorder_dfs(node.right)

        preorder_dfs(root)

        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        buffer = data.split(",")
        count = 0

        def dfs():
            nonlocal count
            if buffer[count] == "null":
                count += 1
                return None

            curr_node = TreeNode(int(buffer[count]))
            count += 1
            curr_node.left = dfs()
            curr_node.right = dfs()

            return curr_node

        return dfs()


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
    root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    # root = TreeNode(1)
    codec = Codec()
    db = codec.serialize(root)
    print(db)
    rroot = codec.deserialize(db)
    printTree(rroot)
