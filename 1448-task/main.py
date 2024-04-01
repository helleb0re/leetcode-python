# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# my bfs iterative O(n) solution
# n - amount of nodes
def goodNodes(root: TreeNode) -> int:
    buffer = [(root, float("-inf"))]

    res = 0
    while buffer:
        curr_node, last_max_value = buffer.pop()

        if curr_node.val >= last_max_value:
            res += 1
            last_max_value = curr_node.val

        if curr_node.right:
            buffer.append((curr_node.right, last_max_value))

        if curr_node.left:
            buffer.append((curr_node.left, last_max_value))

    return res


# my dfs recursive O(n) solution
def goodNodes(root: TreeNode) -> int:

    def dfs(node, last_max_value):
        if node is None:
            return 0

        res = 0
        if node.val >= last_max_value:
            res += 1
            last_max_value = node.val

        res += dfs(node.right, last_max_value)
        res += dfs(node.left, last_max_value)

        return res

    return dfs(root, root.val)


if __name__ == "__main__":
    root = TreeNode(3, TreeNode(1, TreeNode(3)), TreeNode(4, TreeNode(1), TreeNode(5)))
    assert goodNodes(root) == 4
