from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# TRICKS:
#
# * preorder ALWAYS has the node first. But you don't know the size of either branch.
# * inorder ALWAYS has the left branch to the left of the node, and right branch right of the node. So now you know the size of each branch.
# Take those information and break the arrays into subproblems, based on the size.


# my O(n*2n) -> O(n^2) solution
def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if not preorder and not inorder:
        return None

    root = TreeNode(preorder[0])

    # divide tree into left and right subtrees
    # by inorder array
    left_inorder, right_inorder = [], []
    right_inorder_set = set()
    is_left_subtree = True
    for i in range(len(inorder)):
        if inorder[i] == root.val:
            is_left_subtree = False
        else:
            if is_left_subtree:
                left_inorder.append(inorder[i])
            else:
                right_inorder.append(inorder[i])
                right_inorder_set.add(inorder[i])

    # divide preorder array according to
    # new left and right inorder arrays
    left_preorder, right_preorder = [], []
    for i in range(1, len(preorder)):
        if preorder[i] in right_inorder_set:
            right_preorder.append(preorder[i])
        else:
            left_preorder.append(preorder[i])
    # create left and right nodes of the root by recursive
    root.left = buildTree(left_preorder, left_inorder)
    root.right = buildTree(right_preorder, right_inorder)

    return root


# enhance previous solution
def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if not preorder and not inorder:
        return None

    root = TreeNode(preorder[0])

    delimiter = inorder.index(root.val)  # O(n)
    # divide tree into left and right subtrees
    # by inorder array
    left_inorder, right_inorder = inorder[:delimiter], inorder[delimiter + 1 :]

    # divide preorder array according to
    # new left and right inorder arrays
    left_preorder, right_preorder = (
        preorder[1 : delimiter + 1],
        preorder[delimiter + 1 :],
    )

    # create left and right nodes of the root by recursive
    root.left = buildTree(left_preorder, left_inorder)
    root.right = buildTree(right_preorder, right_inorder)

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
    root = buildTree(preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7])
    printTree(root)
