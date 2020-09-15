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
    def getSubtreeHeight(self, root: TreeNode) -> int:
        if root is None:
            return 0

        left_subtree_height = self.getSubtreeHeight(root.left) if root.left else 0
        right_subtree_height = self.getSubtreeHeight(root.right) if root.right else 0

        return max(left_subtree_height, right_subtree_height) + 1

    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True

        left_subtree_height = self.getSubtreeHeight(root.left)
        right_subtree_height = self.getSubtreeHeight(root.right)

        return abs(left_subtree_height - right_subtree_height) <= 1 \
            and self.isBalanced(root.left) and self.isBalanced(root.right)


def main():
    pass


if __name__ == '__main__':
    main()
