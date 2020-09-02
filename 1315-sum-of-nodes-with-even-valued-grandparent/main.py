import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def sumNodes(root: TreeNode, parent: TreeNode, grandParent: TreeNode) -> int:
            if root is None:
                return 0

            if type(grandParent) is TreeNode and grandParent.val % 2 == 0:
                return root.val + sumNodes(root.left, root, parent) + sumNodes(root.right, root, parent)

            return sumNodes(root.left, root, parent) + sumNodes(root.right, root, parent)

        return sumNodes(root, None, None)


def main():
    pass


if __name__ == '__main__':
    main()
